from sqlmodel import SQLModel, Session, create_engine
from typing import Annotated
from fastapi import Depends

sqlite_url = f"sqlite:///database.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# No idea what any of this session business is doing yet...
def get_session():
    with Session(engine) as session:
        print("What is this?")
        yield session
SessionDep = Annotated[Session, Depends(get_session)]
