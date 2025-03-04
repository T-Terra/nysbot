from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponse


from .get_data_github import get_latest_workflow_status


def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin, login_url='/admin/')
def index(req):
    status_info = get_latest_workflow_status()
    return render(req, 'frontbot/index.html', {'workflow': {'name': status_info['name'], 'url': status_info['url']}})

def response_bot(req):
    print(req)
    return HttpResponse(req)