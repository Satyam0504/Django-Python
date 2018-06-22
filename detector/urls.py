from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'user/$',views.user, name='user'),
    url(r'login/$',views.login_view,name='login_view'),
    url(r'input/$',views.input_user,name='input_user'),
    url(r'detect/$',views.detect,name='detect'),
    url(r'admin/$',views.admin, name='admin'),
]
