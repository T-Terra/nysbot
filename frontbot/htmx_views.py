from django.shortcuts import render


from .get_data_github import get_latest_workflow_status

def check_status(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/check_bot_status.html', {'workflow': {'status': status_info['status']}})

def check_conclusion(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/check_bot_conclusion.html', {'workflow': {'conclusion': status_info['conclusion']}})

def check_created_at(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/check_bot_created_at.html', {'workflow': {'created_at': status_info['created_at']}})