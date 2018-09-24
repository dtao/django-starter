"""{{project_name}} URL Configuration
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from project import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', include(('accounts.urls', 'accounts'), namespace='account')),
    path('admin/', admin.site.urls),
]

# Note: don't include static URL patterns in production.
urlpatterns += staticfiles_urlpatterns()
