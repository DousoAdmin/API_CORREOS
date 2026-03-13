import smtplib
import ssl
from email.message import EmailMessage

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.configuracion_correo import ConfiguracionCorreo
from ..schemas.email import EmailSendRequest

router = APIRouter(prefix="/emails", tags=["emails"])


def _get_active_configuracion(db: Session) -> ConfiguracionCorreo | None:
    # Grab the first active configuration (estado == 1). Adjust criteria as needed.
    return (
        db.query(ConfiguracionCorreo)
        .filter(ConfiguracionCorreo.estado == 1)
        .order_by(ConfiguracionCorreo.id.desc())
        .first()
    )


@router.post("/send")
def send_email(request: EmailSendRequest, db: Session = Depends(get_db)):
    db_config = _get_active_configuracion(db)
    if not db_config:
        raise HTTPException(status_code=404, detail="No active mail configuration found")

    if not db_config.remitente or not db_config.remitente.correo_remitente:
        raise HTTPException(status_code=400, detail="The active configuration does not have a valid sender (remitente) configured")

    message = EmailMessage()
    message["Subject"] = request.asunto
    message["From"] = db_config.remitente.correo_remitente
    message["To"] = request.destinatario
    message.set_content(request.cuerpo)

    use_ssl = bool(db_config.usa_ssl)
    use_tls = bool(db_config.usa_tls)

    try:
        if use_ssl:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(db_config.servidor_smtp, db_config.puerto, context=context) as server:
                server.login(db_config.usuarios_smtp, db_config.clave_smtp)
                server.send_message(message)
        else:
            with smtplib.SMTP(db_config.servidor_smtp, db_config.puerto) as server:
                if use_tls:
                    server.starttls(context=ssl.create_default_context())
                server.login(db_config.usuarios_smtp, db_config.clave_smtp)
                server.send_message(message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")

    return {"message": "Email sent"}
