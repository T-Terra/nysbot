import requests
import os
from dotenv import load_dotenv


load_dotenv()

def get_latest_workflow_status():
    url = f"https://api.github.com/repos/{os.getenv('GITHUB_OWNER')}/{os.getenv('GITHUB_REPO')}/actions/runs"
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["workflow_runs"]:
            latest_run = data["workflow_runs"][0]
            return {
                "name": latest_run["name"],
                "status": latest_run["status"],  # queued, in_progress, completed
                "conclusion": latest_run["conclusion"],  # success, failure, cancelled
                "created_at": latest_run["created_at"],
                "updated_at": latest_run["updated_at"],
                "url": latest_run["html_url"]
            }
        return {"error": "Nenhum workflow encontrado"}
    return {"error": f"Erro na API: {response.status_code}"}
