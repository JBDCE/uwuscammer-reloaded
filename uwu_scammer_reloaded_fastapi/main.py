from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

class CreditCard(BaseModel):
    card_num: str
    expiry_date: str
    cvs: int

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
        },
    )


@app.post("/upload")
async def upload_details(card_num, expiry, cvs):
    # TODO Validate Client side inputs
    credit_card = CreditCard(
        card_num=card_num,
        expiry_date=expiry,
        cvs=cvs,
    )
    # TODO Write Result to Database
    print(credit_card)
    # TODO Tell client about success maybe
    return
