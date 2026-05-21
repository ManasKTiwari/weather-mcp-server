# Weather MCP Server By M Kumar

A local Python MCP server using FastMCP and OpenWeather API.

---

## Prerequisites

- Python 3.10+
- Node.js
- OpenWeather API Key

---

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-mcp-server.git
cd weather-mcp-server
```

---

## Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create `.env`

```env
OPENWEATHER_API_KEY=your_api_key
```

---

## Run MCP Server

```bash
python server.py
```

---

## Launch MCP Inspector

```bash
mcp dev server.py
```

---

## MCP Inspector Settings

| Field | Value |
|---|---|
| Transport | stdio |
| Command | python |
| Arguments | server.py |

---

## Test Tool

Tool:

```text
get_weather
```

Input:

```json
{
  "city": "Indore"
}
```

Expected Result:

```json
{
  "city": "Indore",
  "weather": "clear sky",
  "temperature": 34,
  "humidity": 21
}
```
