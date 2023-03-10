import os
import requests
import inquirer

questions = [inquirer.List("type",message="List pages or databases?",choices=["page", "database"])]

# import json


answer = inquirer.prompt(questions)

NOTION_INTEGRATION_TOKEN = os.environ["NOTION_INTEGRATION_TOKEN"]
NOTION_API_BASE_URL = "https://api.notion.com/v1"
headers = {
    "Authorization": f"Bearer {NOTION_INTEGRATION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

search_params = {"filter": {"value": answer["type"], "property": "object"}}
response = requests.post(
    f"{NOTION_API_BASE_URL}/search", json=search_params, headers=headers
)
data = response.json()
print(data)
page_ids = []

for item in data["results"]:
    page_ids.append(item["id"])

print(page_ids)
