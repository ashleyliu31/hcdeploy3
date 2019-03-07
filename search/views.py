from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import cross_currents, cross_currents_article_detail
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, TrigramSimilarity
from django.db.models.functions import Greatest

def query_search(request):
	articles = cross_currents.objects.all()
	search_term = ''
	
	if 'most_recent' in request.GET:
		articles = articles.order_by('-Pub_Year')
	if 'least_recent' in request.GET:
		articles = articles.order_by('Pub_Year')
	if 'keyword' in request.GET:
		search_term = request.GET['keyword']
		articles = articles.annotate(similarity=Greatest(TrigramSimilarity('Title', search_term), TrigramSimilarity('Content', search_term))).filter(similarity__gte=0.03).order_by('-similarity')
		if request.GET.get('a-z') == 'True':
			articles = articles.order_by('Title')
	context = {'articles': articles, 'search_term': search_term}
	return render(request, 'query_search.html', context)

def article_detail(request, ArticleID):
	ArticleID = get_object_or_404(cross_currents_article_detail, ArticleID=ArticleID)
	context = {'ArticleID':ArticleID}
	return render(request, 'article_detail.html', context)
