from django.urls import path

from . import views

app_name = 'rocklog'
urlpatterns = [
    # non-generic views
    path('', views.index, name='index'),
    
    # path('<int:question_id>/', views.detail, name='detailhamster'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote')
]