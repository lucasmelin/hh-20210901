from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import xmltodict
import json
import xml

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/convertxml")
async def convertxml(input_xml: str = Form(...)):
    try:
        output_json = json.dumps(xmltodict.parse(input_xml), indent=4)
    except xml.parsers.expat.ExpatError:
        output_json = "Error: Invalid XML"
    return {"input_xml": input_xml, "output_json": output_json}


@app.post("/convertjson")
async def convert(input_json: str = Form(...)):
    try:
        output_xml = xmltodict.unparse(json.loads(input_json), pretty=True)
    except json.decoder.JSONDecodeError:
        output_xml = "Error: Invalid JSON"
    return {"output_xml": output_xml, "input_json": input_json}


@app.get("/", response_class=HTMLResponse)
async def convert(request: Request):
    return templates.TemplateResponse("convert.html", {"request": request})
