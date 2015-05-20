from django.db import models

class Comment(models.Model):
	id = models.IntegerField(default=0, primary_key=True)
	body = models.CharField(max_length = 500)
	score_ratio = models.FloatField()
	prior_score = models.IntegerField()
	current_score = models.IntegerField()
	subreddit = models.CharField(max_length = 100)
	writer = models.CharField(max_length = 500)
	write_time = models.DateTimeField('date published')

# Create your models here.
