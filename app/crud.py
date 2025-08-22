from sqlalchemy.orm import Session
from . import models, schemas

# Программы
def get_programs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Program).offset(skip).limit(limit).all()

def get_program(db: Session, program_id: int):
    return db.query(models.Program).filter(models.Program.id == program_id).first()

def search_programs(db: Session, name: str):
    return db.query(models.Program).filter(models.Program.name.contains(name)).all()

def create_program(db: Session, program: schemas.ProgramCreate):
    db_program = models.Program(**program.dict())
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

def update_program(db: Session, program_id: int, program: schemas.ProgramUpdate):
    db_program = get_program(db, program_id)
    if db_program:
        for key, value in program.dict().items():
            setattr(db_program, key, value)
        db.commit()
        db.refresh(db_program)
    return db_program

def delete_program(db: Session, program_id: int):
    db_program = get_program(db, program_id)
    if db_program:
        db.delete(db_program)
        db.commit()
    return db_program

#  Преподаватели
def get_teachers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Teacher).offset(skip).limit(limit).all()

def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

def search_teachers(db: Session, subject: str):
    return db.query(models.Teacher).filter(models.Teacher.subject.contains(subject)).all()

def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def update_teacher(db: Session, teacher_id: int, teacher: schemas.TeacherUpdate):
    db_teacher = get_teacher(db, teacher_id)
    if db_teacher:
        for key, value in teacher.dict().items():
            setattr(db_teacher, key, value)
        db.commit()
        db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = get_teacher(db, teacher_id)
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return db_teacher
