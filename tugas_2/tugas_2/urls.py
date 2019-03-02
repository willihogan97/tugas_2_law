"""testRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from login.views import loginMethod
from users.views import usersMethod
from comment.views import commentMethod

urlpatterns = [
    url(r'^login', loginMethod.login),
    url(r'^user/register', usersMethod.register),
    url(r'^user/getUsers', usersMethod.getUsers),
    url(r'^comment/createComment', commentMethod.create),
	url(r'^comment/getCommentById', commentMethod.getById),
    url(r'^comment/getComment', commentMethod.getAll),
    url(r'^comment/deleteComment', commentMethod.delete),
    url(r'^comment/updateComment', commentMethod.update),
]
