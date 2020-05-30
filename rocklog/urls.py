from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'rocklog'

urlpatterns = [
    path('', views.index, name='index'),
    path('saved', views.saved_songs, name='saved'),
    path('upload/<str:b64_payload>', views.upload_new_song),
    path('toggle_save/<int:song_id>', views.toggle_save, name='save_song'),
    path('videoid/<str:artist>/<str:song>/', views.videoid, name='videoid'),
    path('logout', LogoutView.as_view(), name='logout'),

    # rest api + react
    path('api/stream/', views.StreamEntryList.as_view()),
]
