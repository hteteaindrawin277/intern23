from . import views
from django.urls import path
#from .views import HomePageView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    #path('upload/', views.image_upload_view,name='upload')
    #path("", HomePageView.as_view(), name="home"),

]