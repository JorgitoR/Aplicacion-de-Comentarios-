from django.conf.urls import url 

from .views import(

	post_idd, 
	comentario_id,
	eliminarComentarios

)

urlpatterns = [
	
	url(r'^post_id/(?P<pk>\d+)/$', post_idd, name="post_idd"),
	url(r'^comentario_id/(?P<pk>\d+)/$', comentario_id, name="comentario_id"),

	url(r'^eliminar/(?P<id>\d+)/$', eliminarComentarios, name="eliminar"),
]