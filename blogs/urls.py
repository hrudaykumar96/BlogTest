from django.urls import path
from .views import home, createBlogs, updateBlogs, deleteBlog

urlpatterns = [
    path('home/',home, name='home' ),
    path('create/',createBlogs, name='create' ),
    path('update/',updateBlogs, name='update' ),
    path('delete/',deleteBlog, name='delete' ),
]