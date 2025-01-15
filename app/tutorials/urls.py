from django.urls import path
from tutorials import views
from .views import IndexView

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),  
    path('api/tutorials/', views.tutorial_list),
    path('api/tutorials/<int:pk>/', views.tutorial_detail),
    path('api/tutorials/published/', views.tutorial_list_published),
]