# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     # path('saved/', views.saved_movies, name='saved_movies'),
#     # path('saved/<str:category>/', views.saved_category, name='saved_category'),
#     path('saved/', views.saved_movies, name='saved_movies'),  # For all saved movies
#     path('saved/<str:category>/', views.saved_movies, name='saved_movies_by_category'),
#     path('save/', views.save_movie, name='save_movie'),
#     path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('accounts/login/', views.login_view),
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),

#     path('save_movie/', views.save_movie, name='save_movie'),

#     path('saved/', views.saved_movies_all, name='saved_movies_all'),
#     path('saved/<str:category>/', views.saved_movies, name='saved_movies'),

#     path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Redirect login required users properly
    path('accounts/login/', views.login_view),  # Needed for @login_required redirection

    # Movie saving
    path('save_movie/', views.save_movie, name='save_movie'),

    # Saved collections
    path('saved/', views.saved_movies_all, name='saved_movies_all'),  # All collections
    path('saved/<str:category>/', views.saved_movies, name='saved_movies'),  # By category: movie, anime, series

    # Delete
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
]
