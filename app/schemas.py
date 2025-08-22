from pydantic import BaseModel

class ProgramBase(BaseModel):
    name: str
    description: str

class ProgramCreate(ProgramBase):
    pass

class ProgramUpdate(ProgramBase):
    pass

class Program(ProgramBase):
    id: int
    class Config:
        orm_mode = True

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    subject: str

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    class Config:
        orm_mode = True
