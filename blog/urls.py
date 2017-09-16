from django.conf.urls import url
from django.contrib import admin
from blog.views import EmailView, ArticleCreateView,ArticleDetailView,ArticleListView,ArticleMonthArchiveView,ArticleYearArchiveView
from django.conf.urls import url
from django.views.generic.dates import ArchiveIndexView

from blog.models import Article

app_name ='blog'

urlpatterns = [
    url(r"^$", EmailView.as_view(), name="index"),
    url(r"^create/$", ArticleCreateView.as_view(), name="create"),
	url(r"^list/$", ArticleListView.as_view(), name="list"),
	url(r"^detail/(?P<pk>\d+)/$", ArticleDetailView.as_view(), name="detail"),


    url(r'^archive/$',
        ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
        name="article_archive"),


    url(r'^(?P<year>[0-9]{4})/$',
        ArticleYearArchiveView.as_view(),
        name="article_year_archive"),


    # Example: /2012/aug/
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',
        ArticleMonthArchiveView.as_view(),
        name="archive_month"),
    # Example: /2012/08/
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        ArticleMonthArchiveView.as_view(month_format='%m'),
        name="archive_month_numeric"),


]
