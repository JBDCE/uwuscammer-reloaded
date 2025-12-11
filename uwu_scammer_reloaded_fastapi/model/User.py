from sqlmodel import SQLModel, Field, DateTime

class User(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    browsername: str
    ipaddress: str
    connection_timestamp: DateTime
    uploaded: DateTime
