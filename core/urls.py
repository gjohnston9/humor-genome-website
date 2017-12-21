from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('view_joke/', views.view_joke, name='view_joke'),
    path('view_joke/<slug:joke_id>/', views.view_joke, name='view_joke'),
    path('rate/<slug:joke_id>/', views.rate, name='rate'),
]
