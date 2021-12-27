from django.urls import path, include

from storage_model.views import StorageView

app_name = 'storage'
urlpatterns = [
    path('storage/', StorageView.as_view()),


]