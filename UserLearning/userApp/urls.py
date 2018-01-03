from django.conf.urls import url
from userApp import views

#TEMPLATE URLS!
app_name = 'userApp'
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^userLogin/$',views.userLogin,name='userLogin'),
]