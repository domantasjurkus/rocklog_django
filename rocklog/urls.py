from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'rocklog'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/<str:payload>', views.upload_new_song),
    path('videoid/<str:artist>/<str:song>/', views.videoid, name='videoid'),

    path('saved', views.saved_songs, name='saved'),
    path('toggle_save/<int:song_id>', views.toggle_save, name='save_song'),

    path('logout', LogoutView.as_view(), name='logout'),
]
