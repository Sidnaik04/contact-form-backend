from fastapi import APIRouter, Depends, HTTPException, Request
from app.core.limiter import limiter
from sqlalchemy.orm import Session
from app.schemas.contact import ContactCreate
from app.db.deps import get_db
from app.models.contact import Contact
from app.workers.tasks import send_contact_emails
import logging

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/contact")
@limiter.limit("5/hour")
async def submit_contact(
    request: Request, payload: ContactCreate, db: Session = Depends(get_db)
):
    try:
        contact = Contact(
            name=payload.name, email=payload.email, message=payload.message
        )

        db.add(contact)
        db.commit()
        db.refresh(contact)

        # trigger async email
        send_contact_emails.delay(payload.name, payload.email, payload.message)

        return {"success": True, "message": "Thank you! We received your message."}

    except Exception as e:
        logger.error(f"Error submitting contact form: {str(e)}")

        return {
            "success": False,
            "message": "Something went wrong. Please try again later.",
        }
