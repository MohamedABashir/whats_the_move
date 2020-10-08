from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from WhereTheMove.settings import MEDIA_ROOT

from PIL import Image

import os
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	img = models.ImageField(default='default.jpg', upload_to='profile_pics')
	bio = models.CharField(default='', blank=True,max_length=500)
	# location = models.CharField(max_length=30)
	def __str__(self):
		return f'{self.user.username} Profile'
		
	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)
	# 	try:
	# 		image = Image.open(self.img.path)
	# 		if image.height > 300 or image.width > 300:
	# 			output_size = (300, 300)
	# 			image.thumbnail(output_size)
	# 			image.save(self.img.path)
	# 	except:
	# 		pass
			# I will fix it later:(
	def get_absolute_url(self):
		return reverse('profile')
	def get_public_url(self):
		return reverse('user_events',kwargs={'pk':self.pk, 'username':self.user.username})
