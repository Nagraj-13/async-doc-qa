
# Async Document Q&A Microservice

An **easy-to-deploy**, **production-ready** microservice built with **FastAPI**, **SQLAlchemy (async)** and **asyncio** that lets you:

1. **Upload** text documents  
2. **Ask questions** about them  
3. **Receive answers** in the background (simulating an LLM)  

Whether you’re prototyping an AI feature or building a real-world backend, this service gives you all the wiring you need—database, background tasks, logging and Docker support—so you can focus on your business logic.

---

## 🚀 Key Features

- **Upload & Retrieve Documents**  
  Store any text document (title + content) and fetch it by ID.
- **Asynchronous Q&A**  
  Post a question to a document and get a simulated answer in the background—no blocking your HTTP threads!
- **Flexible Database**  
  Switch between **SQLite** (for local/dev) and **PostgreSQL** (for staging/production) via a single `DB_TYPE` environment variable.
- **Custom Logging**  
  Built-in structured logger to track events, errors, and background tasks.
- **Docker-First**  
  Comes with a `Dockerfile` and `docker-compose.yml` for zero-hassle containerization.
- **Health Checks & Extensible**  
  `/health` endpoint for uptime monitoring, plus a clean code structure inspired by real-world microservices.

---

## 🛠️ Tech Stack

| Layer         | Technology                               |
| ------------- | ---------------------------------------- |
| Web Framework | [FastAPI](https://fastapi.tiangolo.com)  |
| ORM           | [SQLAlchemy (Async)](https://docs.sqlalchemy.org) |
| DB Drivers    | [`aiosqlite`](https://pypi.org/project/aiosqlite) / [`asyncpg`](https://pypi.org/project/asyncpg) |
| Config        | [`python-dotenv`](https://pypi.org/project/python-dotenv) |
| Async Tasks   | Python’s built-in `asyncio`              |
| Container     | Docker & Docker Compose                  |

---

## 📦 Project Structure

```text
/
├── app/
│   ├── main.py           # FastAPI app & lifespan events
│   ├── routes/api.py     # All HTTP routes
│   ├── models.py         # SQLAlchemy ORM models
│   ├── schemas.py        # Pydantic request/response schemas
│   ├── database.py       # Async engine & session factory
│   ├── services/
│   │   └── question_service.py  # Simulated LLM logic
│   ├── logger.py         # Custom logger setup
│   └── util.py           # Helpers (e.g. random sleep time)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example


---

## ⚙️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Nagraj-13/async-doc-qa.git
cd async-doc-qa
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

Copy the example file and modify:

```bash
cp .env.example .env
```

Edit **`.env`**:

```ini
# Choose your database: "sqlite" or "postgres"
DB_TYPE=sqlite

# SQLite settings (only if DB_TYPE=sqlite)
SQLITE_PATH=./dev.db

# Postgres settings (only if DB_TYPE=postgres)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=docqa
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

## 🚀 Running Locally

```bash
uvicorn app.main:app --reload
```

* **Swagger UI**:  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc**:       [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🐳 Docker & Docker-Compose

1. **Build & Start**

   ```bash
   docker-compose up --build
   ```

2. **Endpoints**

   * Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   * PostgreSQL (if used): port 5432 on `db` service

3. **Stop & Clean**

   ```bash
   docker-compose down
   ```

---

## 📖 API Usage

### **1. Create Document**

```http
POST /documents/
Content-Type: application/json

{
  "title": "Async Processing 101",
  "content": "Asynchronous programming allows..."
}
```

* **Response**:

  ```json
  { "id": 1, "title": "...", "content": "..." }
  ```

### **2. Get Document**

```http
GET /documents/{doc_id}
```

* **Response**: Document object or 404

### **3. Ask a Question**

```http
POST /documents/{doc_id}/question
```

```json
{ "question": "What is async processing?" }
```

* **Initial Response**:

  ```json
  {
    "id": 2,
    "document_id": 1,
    "question": "...",
    "status": "pending",
    "answer": null,
    "created_at": "2025-08-01T12:00:00Z"
  }
  ```
* **Answer** becomes available after a short delay.

### **4. Get Question & Answer**

```http
GET /questions/{q_id}
```

* **Response**:

  ```json
  {
    "id": 2,
    "document_id": 1,
    "question": "...",
    "status": "answered",
    "answer": "This is a generated answer to your question.",
    "created_at": "..."
  }
  ```

### **5. Health Check**

```http
GET /health
```

* **Response**: `{ "status": "ok" }`

---

## 📝 Custom Logging

All routes and background tasks log to the console by default:

```python
from app.logger import logger

logger.info("Your log message here")
```

Logs look like:

```
[2025-08-01 12:22:31] [INFO] doc_qa_logger – Creating document: …
```

You can easily swap or extend handlers (e.g. file, external service) in `app/logger.py`.

---




