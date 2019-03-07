from django.urls import path
from search.views import query_search, article_detail

app_name = 'search'
urlpatterns = [
    path('', query_search, name='query_search'),
    path('article/<int:ArticleID>/', article_detail, name='article_detail')
]
