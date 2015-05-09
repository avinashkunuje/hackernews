from django.forms import ModelForm 
from stories.models import Story

class StoryForm(ModelForm):
	class Meta:
		fields = "__all__"
		model = Story
		exclude=('points','moderator',)