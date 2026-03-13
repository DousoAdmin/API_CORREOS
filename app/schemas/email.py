from pydantic import BaseModel, EmailStr


class EmailSendRequest(BaseModel):
    asunto: str
    cuerpo: str
    destinatario: EmailStr
