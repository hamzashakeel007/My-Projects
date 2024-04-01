from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("search/", views.search, name="search"),
    path('new/', views.new_entry, name='new_entry'),
    path('save/', views.save_entry, name='save_entry'),
    path("<str:title>/edit", views.edit_entry, name="edit_entry"),
    path('random/', views.random, name='random'),
]
