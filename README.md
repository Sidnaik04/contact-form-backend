# 📬 Contact Form Backend (FastAPI + Celery)

A minimal yet production-inspired backend project for handling contact form submissions with **async email processing**, **rate limiting**, and **clean architecture**.

---

## 🚀 Features

* ✅ REST API using FastAPI
* ✅ Input validation with Pydantic
* ✅ PostgreSQL database integration (SQLAlchemy)
* ✅ Async email sending using Celery + Redis
* ✅ Email testing via Mailtrap (no real emails sent)
* ✅ Rate limiting (5 requests per IP/hour)
* ✅ Structured logging & error handling
* ✅ Simple frontend (HTML + JS)

---

## 🧠 Architecture Overview

```
Frontend → FastAPI API → PostgreSQL (store data)
                         ↓
                    Celery Queue (Redis)
                         ↓
                  Background Worker → Send Emails
```

---

## 🛠️ Tech Stack

| Layer       | Technology              |
| ----------- | ----------------------- |
| Backend     | FastAPI                 |
| Validation  | Pydantic                |
| Database    | PostgreSQL + SQLAlchemy |
| Queue       | Redis                   |
| Async Tasks | Celery                  |
| Email       | SMTP (Mailtrap for dev) |
| Testing     | Pytest                  |
| Frontend    | HTML, CSS, JavaScript   |

---

## 📦 Project Structure

```
contact-form-backend/
│
├── app/
│   ├── api/            # Routes
│   ├── schemas/        # Pydantic models
│   ├── db/             # DB config & models
│   ├── workers/        # Celery setup & tasks
│   ├── utils/          # Email utility
│   ├── core/           # Config, limiter
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── tests/
│
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd contact-form-backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/contact_db

REDIS_URL=redis://localhost:6379/0

EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_PORT=2525
EMAIL_USER=your_mailtrap_username
EMAIL_PASSWORD=your_mailtrap_password
FROM_EMAIL=test@example.com
DEV_EMAIL=test@example.com
```

---

### 5️⃣ Start Services (Postgres + Redis)

```bash
docker compose up -d
```

---

### 6️⃣ Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 7️⃣ Start Celery Worker

```bash
celery -A app.workers.tasks worker --loglevel=info
```

---

### 8️⃣ Run Frontend

Open:

```
frontend/index.html
```

---

## 📡 API Endpoint

### POST `/api/contact`

#### Request Body:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, this is a test message."
}
```

#### Success Response:

```json
{
  "success": true,
  "message": "Thank you! We received your message."
}
```

---

## 🔐 Validation Rules

* Name: required (1–100 chars)
* Email: valid email format
* Message: 10–1000 characters

---

## 🚦 Rate Limiting

* Limit: **5 requests per IP per hour**
* Returns:

```json
{
  "detail": "Rate limit exceeded"
}
```

---

## 📧 Email System

* Emails are processed **asynchronously** using Celery
* Two emails are generated:

  * Confirmation email → User
  * Notification email → Developer
* Mailtrap is used for safe testing (emails appear in dashboard)

---

## 🧪 Testing

Run tests using:

```bash
pytest
```

---

## ⚠️ Notes

* Mailtrap does not send real emails (used for testing only)
* Switch to Gmail SMTP or SendGrid for production
* Ensure Redis and PostgreSQL are running before starting the app

---

