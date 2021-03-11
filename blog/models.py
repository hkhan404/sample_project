from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Categories"

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=255)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post_detail", args=[str(self.pk)])