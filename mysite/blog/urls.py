from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('contact', contact, name='contact'),
    path('', HomeNews.as_view(), name='home'),
    path('news/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('blog/add-news/', CreateNews.as_view(), name='add_news'),
]
