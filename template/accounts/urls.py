from django.urls import include, path

from accounts import views

urlpatterns = [
    path('', include(('django.contrib.auth.urls', 'django.contrib.auth'), namespace='auth')),
    path('register', views.register, name='register'),
]
