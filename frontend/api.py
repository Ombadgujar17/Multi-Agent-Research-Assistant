import requests

BASE_URL = "http://127.0.0.1:8000"


def research(query: str):
    response = requests.post(
        f"{BASE_URL}/research",
        json={"query": query},
    )

    response.raise_for_status()

    return response.json()