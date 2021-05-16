from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.singleblog, name='singleblog'),
    path('contact', views.contact_us, name='contact'),
    path('contact-us', views.regis, name='regis'),
]