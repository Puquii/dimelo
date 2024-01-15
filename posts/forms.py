from django.forms import ModelForm
from .models import Posts

class CreatePost(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'link', 'og_price', 'price', 'description']