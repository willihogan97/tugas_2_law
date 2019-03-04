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
    url(r'^users/register', usersMethod.register),
    url(r'^users/getUsers', usersMethod.getUsers),
    url(r'^comments/createComment', commentMethod.create),
	url(r'^comments/getCommentById', commentMethod.getById),
    url(r'^comments/getComment', commentMethod.getAll),
    url(r'^comments/deleteComment', commentMethod.delete),
    url(r'^comments/updateComment', commentMethod.update),
]
