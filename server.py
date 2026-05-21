import os
import requests

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

# Create MCP server
mcp = FastMCP("WeatherServer")

# Read API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")


@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get current weather for a city
    """

    if not API_KEY:
        return "API key not configured"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return f"Failed to fetch weather for {city}"

    data = response.json()

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return (
        f"Weather in {city}: "
        f"{weather}, "
        f"Temperature: {temp}°C, "
        f"Humidity: {humidity}%"
    )


if __name__ == "__main__":
    mcp.run()
