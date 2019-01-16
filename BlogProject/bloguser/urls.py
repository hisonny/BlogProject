from django.contrib.auth.urls import url
from . import views

urlpatterns =[
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^register/$',views.register,name='user_register'),
    url(r'^home/',views.home,name='userhome'),
    url(r'^get_code/',views.get_code,name='code'),
    url(r'^myinfo/',views.myinfo,name='myinfo'),
    url(r'^updateinfo/',views.updateinfo,name='updateinfo'),
    url(r'^updatepasswd/',views.updatepasswd,name='updatepasswd')



]