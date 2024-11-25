# src/weather/tools/weather_tool.py
import requests
import os
from crewai.tools import BaseTool
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class WeatherTool(BaseTool):
    name: str = "WeatherTool"
    description: str = (
        "Esta ferramenta fornece a temperatura atual de uma cidade especificada.\n"
        "Entrada: nome da cidade como string.\n"
        "Saída: uma string descrevendo a temperatura atual na cidade."
    )

    def _run(self, city: str) -> str:
        api_key = os.getenv("OPEN_WEATHER_API_KEY")
        if not api_key:
            return "Erro: Chave da API não encontrada. Verifique se a variável OPEN_WEATHER_API_KEY está definida no arquivo .env."
        
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric',
            'lang': 'pt'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            return f"A temperatura atual em {city} é {temperature}°C."
        else:
            return f"Erro ao obter dados da API: {response.status_code} - {response.json().get('message', '')}"

    async def _arun(self, city: str) -> str:
        # Implementação assíncrona, se necessário
        return self._run(city)



