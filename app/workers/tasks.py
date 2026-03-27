import asyncio
from app.workers.celery_app import celery
from app.utils.email import send_email
import os
from datetime import datetime

DEV_EMAIL = os.getenv("DEV_EMAIL")


@celery.task
def send_contact_emails(name, email, message):
    async def _send():
        # 1. Confirmation email to user
        await send_email(
            to_email=email,
            subject="Thank you for contacting us",
            text_content=f"Hi {name},\n\nWe received your message:\n\n{message}",
            html_content=f"""
                <h3>Hi {name},</h3>
                <p>Thank you for reaching out!</p>
                <p><strong>Your message:</strong></p>
                <p>{message}</p>
            """,
        )

        # Add delay to respect rate limits
        await asyncio.sleep(2)

        # 2. Notification email to developer
        await send_email(
            to_email=DEV_EMAIL,
            subject="New Contact Form Submission",
            text_content=f"""
                Name: {name}
                Email: {email}
                Message: {message}
                Time: {datetime.utcnow()}
            """,
            html_content=f"""
                <h3>New Contact Submission</h3>
                <p><b>Name:</b> {name}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Message:</b> {message}</p>
                <p><b>Time:</b> {datetime.utcnow()}</p>
            """,
        )

    asyncio.run(_send())
