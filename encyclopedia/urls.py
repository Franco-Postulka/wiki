from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry>', views.search, name='search'),
    path('search_bar',views.search_bar, name='search_bar')
]
