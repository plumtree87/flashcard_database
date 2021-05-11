from django.db import models

# Create your models here.


class FlashCard(models.Model):
    word = models.CharField(max_length=500)
    definition = models.CharField(max_length=1000)
    collection = models.ForeignKey('flashcards.Collection', default=None, on_delete=models.CASCADE)


class Collection(models.Model):
    title = models.CharField(max_length=100)


