from django.contrib.auth.urls import url
from . import views
urlpatterns = [
    url(r'^list/',views.list,name='list'),
    url(r'^create/',views.create_question,name='create'),
    url(r'^create_blog/',views.create_blog,name='create_blog'),
    url(r'^myblog/',views.myblog,name='myblog'),
    url(r'^allblog/',views.allblog,name='allblog'),
    url(r'^index/',views.home,name='bloghome'),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.delete),
    url(r'^update/(?P<pk>[0-9]+)/$',views.update,name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/$',views.myoneblog),
    url(r'^details/(?P<pk>[0-9]+)/$',views.alloneblog)
]