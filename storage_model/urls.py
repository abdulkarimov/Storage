from django.urls import path, include
from storage_model.views import StorageView, CategoryView

app_name = 'storage'
urlpatterns = [
    path('storage/', StorageView.as_view()),
    path('storage/<int:pk>', StorageView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),

]