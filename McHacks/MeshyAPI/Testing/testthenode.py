import requests
from config import API_KEY, IMGUR_CLIENT_ID

task_id = "018d4ca6-45e7-7046-b253-3fc7e6b8603d"
headers = {
    "Authorization": API_KEY
}

response = requests.get(
    f"https://api.meshy.ai/v1/image-to-3d/{task_id}",
    headers=headers,
)
response.raise_for_status()
print(response.json())
