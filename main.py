from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import xmltodict
import json
import xml

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/convert")
async def convert(input_xml: str = Form(...)):
    try:
        output = json.dumps(xmltodict.parse(input_xml), indent=4)
    except xml.parsers.expat.ExpatError:
        output = "Error: Invalid XML"
    return {"input_xml": input_xml, "output_json": output}


@app.get("/", response_class=HTMLResponse)
async def convert(request: Request):
    return templates.TemplateResponse("convert.html", {"request": request})
