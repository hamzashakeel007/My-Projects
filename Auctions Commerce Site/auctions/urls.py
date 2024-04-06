from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create/', views.create_listing, name='create_listing'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('listing/<int:listing_id>/close/', views.close_listing, name='close_listing'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/remove/<int:listing_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('place_bid/<int:listing_id>/', views.place_bid, name='place_bid'),
    path('add_comment/<int:listing_id>/', views.add_comment, name='add_comment'),
    path('my_listings/', views.my_listings, name='my_listings'),
    path('categories/', views.categories, name='categories'),
    path('categories/<str:category>/', views.category_listings, name='category_listings')
]
