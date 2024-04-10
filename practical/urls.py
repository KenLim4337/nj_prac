from django.urls import path
from . import views, api

app_name= 'practical' 


urlpatterns = [
    path('', views.home, name='home'),
    
    # API
    path('api/articles/<int:article_id>/get/', api.get_article, name='get_article'),
    path('api/articles/<int:article_id>/remove/', api.remove_article, name='remove_article'),
    path('api/articles/<int:article_id>/edit/', api.edit_article, name='edit_article'),
    path('api/articles/add/', api.add_article, name='add_article'),
    path('api/articles/<int:article_id>/comments/add/', api.add_comment, name='add_comment')
]