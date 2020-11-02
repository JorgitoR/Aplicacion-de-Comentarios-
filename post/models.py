# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.conf import settings
from django.db.models.signals import pre_save, post_save

from django.utils.text import slugify

from django.contrib.contenttypes.models import ContentType
from comentarios.models import Comentarios

from django.core.urlresolvers import reverse

class Post(models.Model):

	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	texto   = models.TextField(max_length=200, blank=True, null=True)
	slug    = models.SlugField(unique=True, blank=True)
	tiempo  = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse("post_idd", kwargs={"pk": self.pk})

	def comentarios(self):
		instance = self
		qs = Comentarios.objects.filtro_por_instancia(instance)
		return qs

	def get_content_type(self):
		content_type = ContentType.objects.get_for_model(Post)
		return content_type

def nueva_url(instance, url=None):

	slug = slugify(instance.texto)

	if url is not None:
		slug = url

	qs = Post.objects.filter(slug=slug).order_by("-id")

	if qs.exists():
		nueva_url_si = "%s-%s"%(slug, qs.first().id)
		return nueva_url(instance, url=nueva_url_si)
	return slug

def url_creada(sender, instance, *args, **kwargs):

	if not instance.slug:

		print("My nombre es %s y tengo %s" % ('Jorgito', 20))

		instance.slug = nueva_url(instance)

pre_save.connect(url_creada, sender=Post)
