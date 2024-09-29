from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from meal_provider import MealProvider
from calendar import day_name
from datetime import datetime

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

meal_provider = MealProvider()

@app.get("/meal", response_class=HTMLResponse)
async def root(day: int = Query(None, description="Day of the week (1-7)")):
    # Add the CSS link to the HTML head
    css_link = '<link rel="stylesheet" href="/static/css/style.css">'
    
    if day is None or day < 1 or day > 7:
        return RedirectResponse(url="/menu")
        
    day_name_result = day_name[day - 1]
    meal = meal_provider.get_meal(day)
    return f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {css_link}
        </head>
        <body>
            <h1>Meal for {day_name_result}</h1>
            <p>{meal}</p>
        </body>
    </html>
    """
    
@app.get("/menu", response_class=HTMLResponse)
async def root():
    # Add the CSS link to the HTML head
    css_link = '<link rel="stylesheet" href="/static/css/style.css">'
    
    links = "\n".join([f'<p><a href="/meal?day={i}">{d}</a></p>' for i, d in enumerate(day_name, 1)])
    return f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {css_link}
        </head>
        <body>
            <h1>Welcome to meal plan</h1>
            <p>Choose from the days below:</p>
            {links}
        </body>
    </html>
    """

@app.get("/", response_class=RedirectResponse)
async def home():
    current_day = datetime.now().weekday() + 1  # Monday is 1, Sunday is 7
    return RedirectResponse(url=f"/meal?day={current_day}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
