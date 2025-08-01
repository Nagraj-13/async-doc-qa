from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import models, schemas
from app.services.question_service import simulate_llm_answer
from app.logger import logger 
import asyncio

router = APIRouter()

@router.post("/documents/", response_model=schemas.DocumentOut)
async def create_document(doc: schemas.DocumentCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Creating document: {doc.title}")
    new_doc = models.Document(**doc.dict())
    db.add(new_doc)
    await db.commit()
    await db.refresh(new_doc)
    logger.debug(f"Document created with ID: {new_doc.id}")
    return new_doc

@router.get("/documents/{doc_id}", response_model=schemas.DocumentOut)
async def get_document(doc_id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"Fetching document with ID: {doc_id}")
    result = await db.get(models.Document, doc_id)
    if not result:
        logger.warning(f"Document with ID {doc_id} not found")
        raise HTTPException(404, "Document not found")
    return result

@router.post("/documents/{doc_id}/question", response_model=schemas.QuestionOut)
async def ask_question(doc_id: int, q: schemas.QuestionCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Received question for document {doc_id}: {q.question}")
    question = models.Question(document_id=doc_id, question=q.question)
    db.add(question)
    await db.commit()
    await db.refresh(question)
    logger.debug(f"Question stored with ID: {question.id}")
    asyncio.create_task(simulate_llm_answer(question.id, db))
    return question

@router.get("/questions/{q_id}", response_model=schemas.QuestionOut)
async def get_question(q_id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"Fetching question with ID: {q_id}")
    result = await db.get(models.Question, q_id)
    if not result:
        logger.warning(f"Question with ID {q_id} not found")
        raise HTTPException(404, "Question not found")
    return result

@router.get("/health")
async def health_check():
    logger.info("Health check triggered")
    return {"status": "ok"}
