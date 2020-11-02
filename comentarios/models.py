# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import  GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from django.core.urlresolvers import reverse
from django.conf import settings

class ComentariosManager(models.Manager):

	def filtro_por_instancia(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id   = instance.id 
		qs = super(ComentariosManager, self).filter(content_type=content_type, object_id=obj_id)
		return qs

class Comentarios(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	texto   = models.TextField(verbose_name="Comentario")

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id    = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	tiempo = models.DateTimeField(auto_now_add=True)

	objects = ComentariosManager()

	def get_absolute_url(self):
		return reverse("comentario_id", kwargs={"pk": self.pk})

	def __unicode__(self):
		return self.texto[:15]

	class Meta:
		ordering = ['-tiempo']