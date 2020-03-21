from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'rocklog'

urlpatterns = [
    path('', views.index, name='index'),
    # path('index/', views.index, name='index'),
    # path('home', views.index, name='home'),
    # path('logout', views.logout),

    path('videoid/<str:artist>/<str:song>/', views.videoid, name='videoid'),
    # path('logout/', views.hamster_logout, name='hamster_logout'),
    path(r'^logout/$', LogoutView.as_view(), {'next_page': '/', 'redirect_field_name': '/', 'template_name': '/'}, name='hamster_logout'),
]
