from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry>', views.search, name='search'),
    path('search_bar',views.search_bar, name='search_bar'),
    path('new_page',views.new_page, name='new_page'),
    path('save_page',views.save_page, name='save_page'),
    path('edit_page',views.edit_page, name='edit_page'),
    path('save_edit',views.save_edit, name='save_edit'),
    path('random_page',views.random_page, name='random_page'),
]
