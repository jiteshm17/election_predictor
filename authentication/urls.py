from django.urls import path, include
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register_user/', views.register_user, name='register_user'),
    path('register_party/', views.register_party, name='register_party'),
    path('group/', include('group.urls')),
    path('news/', include('news_items.urls')),

]
