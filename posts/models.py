from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    og_price =models.IntegerField()
    price = models.IntegerField()
    description =models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title