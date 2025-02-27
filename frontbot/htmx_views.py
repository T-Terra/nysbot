from django.shortcuts import render


from .get_data_github import get_latest_workflow_status, trigger_workflow


def check_status_button(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/button_trigger.html', {'workflow': {'status': status_info['status']}})

def check_status(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/check_bot_status.html', {'workflow': {'status': status_info['status']}})

def check_conclusion(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/check_bot_conclusion.html', {'workflow': {'conclusion': status_info['conclusion']}})

def check_created_at(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/check_bot_created_at.html', {'workflow': {'created_at': status_info['created_at']}})

def check_updated_at(req):
    status_info = get_latest_workflow_status()
    return render(req, 'partials/htmx_components/check_bot_updated_at.html', {'workflow': {'updated_at': status_info['updated_at']}})

def trigger_view(req):
    status_info = trigger_workflow()
    return render(req, 'partials/htmx_components/button_disabled.html', {'status_code': status_info})