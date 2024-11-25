from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()

# Uncomment the following line to use an example of a custom tool
from src.weather.tools.weather_tool import WeatherTool

@CrewBase
class WeatherCrew():
    """Weather Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[WeatherTool()],
            verbose=True
        )

    @task
    def weather_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Cria a Weather Crew"""
        return Crew(
            agents=self.agents,  # Criado automaticamente pelo decorador @agent
            tasks=self.tasks,    # Criado automaticamente pelo decorador @task
            process=Process.sequential,
            verbose=True,
        )