from django.urls import path
from blog.views import BlogList, BlogDetail

urlpatterns = [
    path('blogs/', BlogList.as_view()),  
    path('blogs/<str:pk>/', BlogDetail.as_view()),  
]

