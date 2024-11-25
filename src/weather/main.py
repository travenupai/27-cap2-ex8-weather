# main.py
#!/usr/bin/env python
import sys
import time
import warnings

from weather.crew import WeatherCrew

warnings.filterwarnings("ignore", category=SyntaxWarning)

def run():
    """
    Executa a crew.
    """
    # Solicita o nome da cidade ao usuário
    city_name = input("Informe o nome da cidade: ")

    inputs = {
        'city': city_name
    }

    WeatherCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Weather().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Weather().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Weather().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
