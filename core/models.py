from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Joke(models.Model):
    joke_id = models.CharField(primary_key=True, max_length=6)
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=2000)
    ups = models.IntegerField()
    downs = models.IntegerField()
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        db_table = 'reddit_jokes' ### Reddit crawler inserts jokes into this table
