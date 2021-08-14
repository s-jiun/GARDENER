from django.contrib import auth
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.member_del, name='signout'),

    path('update/', views.member_modification, name='update'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/<int:pk>/follow', views.follow_list, name='follow'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('myprofile', views.my_profile, name='my_profile'),
    path('', views.start_page, name="start_page"),
    path('following_ajax/', views.following_ajax, name='following_ajax'),
    path('follow_ajax/', views.follow_ajax, name='follow_ajax'),
    path('find_id/', views.find_id, name='find_id'),
    path('profile/<int:pk>/my_pick', views.liked_posts, name='my_pick'),
    path('accounts/login/', views.login, name='account_login'),
    # path('profile/<int:pk>/my_scrab_plant', views.my_scrab_plant, name='my_scrab_plant'),
]
