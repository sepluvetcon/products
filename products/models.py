from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	price = models.PositiveIntegerField()

	def __str__(self):
		return self.title
