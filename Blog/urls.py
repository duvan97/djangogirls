from django.conf.urls import url, include
from Blog.views import listpost, detalle, List


urlpatterns = [
    url(r'^$', List.as_view(), name='lista_art'),
    url(r'^detalle/(?P<id>[\d]+)', detalle, name='detalle'),
]
