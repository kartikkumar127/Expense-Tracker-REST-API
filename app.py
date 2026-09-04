from datetime import date
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./expenses.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    category = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    expense_date = Column(Date, nullable=False)


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API", version="1.0.0")


class ExpenseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    category: str = Field(min_length=1, max_length=50)
    amount: float = Field(gt=0)
    expense_date: date


class ExpenseUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    category: Optional[str] = Field(default=None, min_length=1, max_length=50)
    amount: Optional[float] = Field(default=None, gt=0)
    expense_date: Optional[date] = None


class ExpenseResponse(ExpenseCreate):
    id: int

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}


@app.post("/expenses", response_model=ExpenseResponse, status_code=201)
def create_expense(payload: ExpenseCreate):
    db = SessionLocal()
    try:
        expense = Expense(**payload.model_dump())
        db.add(expense)
        db.commit()
        db.refresh(expense)
        return expense
    finally:
        db.close()


@app.get("/expenses", response_model=list[ExpenseResponse])
def list_expenses(
    category: Optional[str] = Query(default=None),
    limit: int = Query(default=100, ge=1, le=500)
):
    db = SessionLocal()
    try:
        query = db.query(Expense)
        if category:
            query = query.filter(Expense.category == category)
        return query.order_by(Expense.expense_date.desc()).limit(limit).all()
    finally:
        db.close()


@app.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int):
    db = SessionLocal()
    try:
        expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        return expense
    finally:
        db.close()


@app.put("/expenses/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, payload: ExpenseUpdate):
    db = SessionLocal()
    try:
        expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")

        for key, value in payload.model_dump(exclude_unset=True).items():
            setattr(expense, key, value)

        db.commit()
        db.refresh(expense)
        return expense
    finally:
        db.close()


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    db = SessionLocal()
    try:
        expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")

        db.delete(expense)
        db.commit()
        return {"message": "Expense deleted successfully"}
    finally:
        db.close()


@app.get("/expenses/summary/by-category")
def category_summary():
    from sqlalchemy import func

    db = SessionLocal()
    try:
        rows = (
            db.query(Expense.category, func.sum(Expense.amount).label("total_amount"))
            .group_by(Expense.category)
            .order_by(func.sum(Expense.amount).desc())
            .all()
        )
        return [{"category": category, "total_amount": float(total)} for category, total in rows]
    finally:
        db.close()
