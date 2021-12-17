from django.urls import path, include


app_name = 'salary'
urlpatterns = [
    path('api/', include('salary.api.urls', namespace='api')),
]