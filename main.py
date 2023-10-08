from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from utils import util


app = FastAPI()
templates = Jinja2Templates(directory="templates")
weatherstack_api_key = "28d8465feea245e37fde2d8feb2b5502"

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")

cities = {
    "New York": "40.7128  -74.0060",
    "London": "51.5074  -0.1278",
    "Paris": "48.8566  2.3522",
    "Tokyo": "35.6762  139.6503",
    "Sydney": "-33.8651  151.2093",
    "Rio de Janeiro": "-22.9068  -43.1729",
    "Dubai": "25.2048  55.2708",
    "Mumbai": "19.0760  72.8777",
    "Hong Kong": "22.3193  114.1694",
    "Singapore": "1.3521  103.8198",
    "Toronto": "43.6532  -79.3832",
    "Berlin": "52.5200  13.4050",
    "Moscow": "55.7558  37.6173",
    "Beijing": "39.9042  116.4074",
    "Bangkok": "13.7563  100.5018",
    "Cairo": "30.0444  31.2357",
    "Istanbul": "41.0082  28.9784",
    "São Paulo": "-23.5505  -46.6333",
    "Mexico City": "19.4326  -99.1332",
    "New Delhi": "28.6139  77.2090"
}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # client_host = request.client.host
    location = util.getLocation()
    status, weather = util.get_weather(weatherstack_api_key, location['city'].lower(), 'm', True)
    if status == 200:
        return templates.TemplateResponse("home.html", {"request": request, "cities": cities, "weather": weather})
    else:
        error = {"error": "Could not retrieve weather data."}
        # If the response status code is not 200, then render the error.html template with an error message
        return templates.TemplateResponse("home.html", {"request": request, "cities": cities, "weather": error})


@app.post("/weather", response_class=HTMLResponse)
async def weather(request: Request, location: str = Form(...), units: str = "m"):
    status, weather = util.get_weather(weatherstack_api_key, location, units)
    if status == 200:
        # Render the weather.html template with the weather data dictionary as context
        return templates.TemplateResponse("weather.html", {"request": request, "weather": weather})

    else:
        # If the response status code is not 200, then render the error.html template with an error message
        return templates.TemplateResponse("error.html",
                                          {"request": request, "error": "Could not retrieve weather data."})

