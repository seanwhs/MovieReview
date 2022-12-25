from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name = "about"),
    path('call_to_signup/', views.call_to_signup, name="call_to_signup"),
    path('signup', views.signup, name='signup'),
    path('movie/<str:movie_id>', views.movie_details, name="movie_details"),
    path('movie/<str:movie_id>/create_review', views.create_review, name="create_review"),
    path('review/<str:review_id>', views.update_review, name="update_review"),
    path('review/<str:review_id>/delete_review', views.delete_review, name='delete_review'),
]
