# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post

def inicio(request):

	todos_los_post = Post.objects.all()

	context = {

		'post':todos_los_post

	}

	return render(request, 'inicio.html', context)