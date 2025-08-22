from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.requests import Request
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# HTML Главная
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    programs = crud.get_programs(db)
    teachers = crud.get_teachers(db)
    return templates.TemplateResponse("index.html", {"request": request, "programs": programs, "teachers": teachers})

# Программы
@app.get("/api/programs", response_model=list[schemas.Program])
def list_programs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_programs(db, skip, limit)

@app.get("/api/programs/{program_id}", response_model=schemas.Program)
def get_program(program_id: int, db: Session = Depends(get_db)):
    db_program = crud.get_program(db, program_id)
    if not db_program:
        raise HTTPException(status_code=404, detail="Program not found")
    return db_program

@app.post("/api/programs", response_model=schemas.Program)
def create_program(program: schemas.ProgramCreate, db: Session = Depends(get_db)):
    return crud.create_program(db, program)

@app.put("/api/programs/{program_id}", response_model=schemas.Program)
def update_program(program_id: int, program: schemas.ProgramUpdate, db: Session = Depends(get_db)):
    db_program = crud.update_program(db, program_id, program)
    if not db_program:
        raise HTTPException(status_code=404, detail="Program not found")
    return db_program

@app.delete("/api/programs/{program_id}", response_model=schemas.Program)
def delete_program(program_id: int, db: Session = Depends(get_db)):
    db_program = crud.delete_program(db, program_id)
    if not db_program:
        raise HTTPException(status_code=404, detail="Program not found")
    return db_program

@app.get("/api/programs/search/", response_model=list[schemas.Program])
def search_programs(name: str, db: Session = Depends(get_db)):
    return crud.search_programs(db, name)

#  Преподаватели
@app.get("/api/teachers", response_model=list[schemas.Teacher])
def list_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_teachers(db, skip, limit)

@app.get("/api/teachers/{teacher_id}", response_model=schemas.Teacher)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id)
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@app.post("/api/teachers", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db, teacher)

@app.put("/api/teachers/{teacher_id}", response_model=schemas.Teacher)
def update_teacher(teacher_id: int, teacher: schemas.TeacherUpdate, db: Session = Depends(get_db)):
    db_teacher = crud.update_teacher(db, teacher_id, teacher)
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@app.delete("/api/teachers/{teacher_id}", response_model=schemas.Teacher)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.delete_teacher(db, teacher_id)
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@app.get("/api/teachers/search/", response_model=list[schemas.Teacher])
def search_teachers(subject: str, db: Session = Depends(get_db)):
    return crud.search_teachers(db, subject)
