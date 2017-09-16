from django.db import models
import django

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})