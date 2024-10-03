from django.urls import path
from django.apps import apps
from .crud_generator import generate_crud_urls

urlpatterns = []

app = apps.get_app_config('testapp')
for model in app.get_models():
    urlpatterns += generate_crud_urls(model, app.label)
  