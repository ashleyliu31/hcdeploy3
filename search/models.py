from django.db import models
from django.urls import reverse

class cross_currents(models.Model):
    ArticleID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=500)
    Author = models.CharField(max_length=200, null=True)
    Journal = models.CharField(max_length=500, null=True)
    Pub_Year = models.IntegerField(null=True)
    Issue = models.IntegerField(null=True)
    Link = models.URLField(max_length=800, null=True)
    Content = models.TextField()

    class Meta:
    	db_table = 'cross_currents'

    def __str__(self):
    	return f'{self.Title}, {self.Author}, {self.Journal}, {self.Pub_Year}, {self.Issue}'
    def get_absolute_url(self):
    	return reverse('article-detail', args=[str(self.ArticleID)])

class cross_currents_article_detail(models.Model):
    ArticleID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=500)
    Author = models.CharField(max_length=200, null=True)
    Journal = models.CharField(max_length=500, null=True)
    Pub_Year = models.IntegerField(null=True)
    Issue = models.IntegerField(null=True)
    Link = models.URLField(max_length=800, null=True)
    Content = models.TextField()

    class Meta:
        db_table = 'cross_currents'

    def __str__(self):
        return f'{self.Title}, {self.Author}, {self.Journal}, {self.Pub_Year}, {self.Issue}, {self.Content}'

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.ArticleID)])
