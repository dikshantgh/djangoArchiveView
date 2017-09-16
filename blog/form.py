from blog.models import Article
from django import forms
class ArticleForm(forms.ModelForm):

	
	#choices = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Article
		fields = ['title','pub_date']
