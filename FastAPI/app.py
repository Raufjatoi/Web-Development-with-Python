from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, FastAPI!"})

@app.get("/form/", response_class=HTMLResponse)
def show_form(request:Request):
    return templates.TemplateResponse("form.html", {"request":request})

@app.get("/rauf/", response_class=HTMLResponse)
def greet_rauf(request:Request):
    return templates.TemplateResponse("rauf.html", {"request": request, "message": "Hello, Abdul Rauf"})

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    print("Running on http://localhost:8000")