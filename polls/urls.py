from django.urls import path

from . import views
from . import admin_views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_guest_session/', views.new_guest_session, name='new_guest_session'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('admin/polls/results/', admin_views.results, name='results'),
]
