from django.shortcuts import render
from blog.models import Article
from django.views.generic.edit import CreateView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.views.generic import TemplateView, DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from blog.form import ArticleForm
# Create your views here.


class EmailView(TemplateView):
	template_name = "blog/email.html"


class ArticleListView(ListView):

    # lists all question type
    model = Article
    template_name = "blog/list.html"
    context_object_name ="type_list"

        

class ArticleDetailView(DetailView):

    model =  Article
    template_name = "blog/detail.html"
    context_object_name = "type_list"


class ArticleCreateView(CreateView):


    form_class = ArticleForm
    template_name = "blog/create.html"
    

class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True
