from django.conf import settings


def common_settings(request):
    return {
        'APPLICATION_NAME': settings.APPLICATION_NAME
    }
