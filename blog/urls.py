from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
]