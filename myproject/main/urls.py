from django.urls import path
from . import views as MAIN_V

urlpatterns = [
    path('',MAIN_V.home, name="home"),
    path('about/',MAIN_V.about, name="about"),
    path('contact/',MAIN_V.contact, name="contact"),
    path('posts/<int:id>/<int:roll>/',MAIN_V.posts, name="posts")
]
