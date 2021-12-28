from django.urls import path

from storage_model.views import StorageView, CategoryView, UpdateCountView

app_name = 'storage'
urlpatterns = [
    path('storage/', StorageView.as_view()),
    path('storage/<int:pk>', StorageView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
    path('updateCount/<int:pk>', UpdateCountView.as_view()),

]