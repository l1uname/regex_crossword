from django.urls import path
from . import views

app_name = 'puzzle'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('square',views.square_view,name='square'),
    path('hexagon',views.hexagon_view,name='hexagon'),
    path('board',views.board_view,name='board'),
    path('hexboard',views.hexboard_view,name='hexboard'),
    path('documentation',views.documentation_view,name='documentation'),
    path('congratulations',views.congrats_view,name='congrats'),
]

