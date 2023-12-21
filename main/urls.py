from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.DrugListAPIView.as_view()),
    path('drug/<int:pk>/', views.DrugRetrieveAPIView.as_view()),
    path('clinic/', views.ClinicListAPIView.as_view())
]
