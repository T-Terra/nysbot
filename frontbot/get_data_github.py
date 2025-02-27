import requests
import os
from dotenv import load_dotenv
from django.http import JsonResponse


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
        return JsonResponse({"error": "Nenhum workflow encontrado"})
    return JsonResponse({"error": f"Erro na API: {response.status_code}"})

def trigger_workflow():
    url = f"https://api.github.com/repos/{os.getenv('GITHUB_OWNER')}/{os.getenv('GITHUB_REPO')}/actions/workflows/{os.getenv('GITHUB_WORKFLOW_FILE')}/dispatches"
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {"ref": os.getenv('GITHUB_BRANCH')}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 204:
        return response.status_code
    else:
        return JsonResponse({"error": f"Erro ao iniciar workflow: {response.text}"})