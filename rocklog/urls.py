from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'rocklog'

urlpatterns = [
    path('', views.index, name='index'),
    path('saved', views.saved_songs, name='saved'),
    path('videoid/<str:artist>/<str:song>/', views.videoid, name='videoid'),
    path('toggle_save_song/<int:song_id>', views.toggle_save_song, name='save_song'),

    path('logout', LogoutView.as_view(), name='hamster_logout'),
]
