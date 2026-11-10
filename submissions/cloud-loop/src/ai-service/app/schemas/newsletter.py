from pydantic import BaseModel, EmailStr, Field

class NewsletterSubscribeRequest(BaseModel):
    email: EmailStr = Field(..., description="Subscriber email address")

class NewsletterSubscribeResponse(BaseModel):
    ok: bool = True
    email: str
    message: str = "Successfully subscribed to Cloud-Loop opportunity alerts."
