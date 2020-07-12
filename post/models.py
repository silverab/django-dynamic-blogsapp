from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, blank=False)
	description = models.CharField(max_length=1000, blank=False)
	post_date = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.title