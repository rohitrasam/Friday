from django.urls import path
from .views import *


urlpatterns = [
    
    path("upload_to_db/", upload_to_db, name="upload-to-db"),
]