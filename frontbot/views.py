from django.shortcuts import render
from django.http import JsonResponse


from .get_data_github import get_latest_workflow_status


# Create your views here.
def index(request):
    status_info = get_latest_workflow_status()
    return render(request, 'frontbot/index.html', {'workflow': {'name': status_info['name'], 'url': status_info['url']}})

def ajaxStatus(request):
    status_info = get_latest_workflow_status()
    return JsonResponse({'workflow': status_info})