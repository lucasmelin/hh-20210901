from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/form", response_class=HTMLResponse)
async def printform(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    password: str = Form(...),
    city: str = Form(...),
    province: str = Form(...),
    postal: str = Form(...),
):
    print(
        f"""
    First Name: {first_name}
    Last Name: {last_name}
    Password: {password}
    City: {city}
    Province: {province}
    Postal Code: {postal}
        """
    )
    return templates.TemplateResponse("form.html", {"request": request})


@app.get("/form", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
