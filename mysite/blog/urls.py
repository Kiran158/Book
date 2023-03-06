from . import views
from django.urls import path
from blog.views import Error404View

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('book-list/', views.MyListView.as_view(), name='book-list'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('update/<slug:pk>/', views.UpdatePost.as_view(), name='update'),
    path('delete/<slug:pk>/', views.DeletePost.as_view(), name='delete'),
    path('post-detail/<slug:pk>/', views.PostDetail.as_view(), name='post-detail'), 
    path('404/', Error404View.as_view(), name='error_404'),
]

