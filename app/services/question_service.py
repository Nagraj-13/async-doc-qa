import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Question
from sqlalchemy import update
from app.util import get_random_time
async def simulate_llm_answer(question_id: int, session: AsyncSession):
    sim_time = get_random_time();
    await asyncio.sleep(sim_time)
    stmt = (
        update(Question)
        .where(Question.id == question_id)
        .values(
            answer=f"This is a generated answer to your question.",
            status="answered"
        )
    )
    await session.execute(stmt)
    await session.commit()
