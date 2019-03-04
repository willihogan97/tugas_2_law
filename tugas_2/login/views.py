from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import User
import requests

class loginMethod :
	@csrf_exempt
	def login(request):
	  	if request.method == 'POST':
		    body_unicode = request.body.decode('utf-8')
		    body = json.loads(body_unicode)
		    username = body['username']
		    password = body['password']
		    url = "https://oauth.infralabs.cs.ui.ac.id/oauth/token"
		    data = {"username": username, "password": password, "grant_type": "password", "client_id": "nCpJE0ZFYp7YMlyVok0ughAPQgFlfk2w", "client_secret": "J7QOAJ1To5Rjt4S7tOeBwKNyY0Eb6RLI"}
		    r = requests.post(url, data = data)
		    if r.status_code == 401 :
		    	return JsonResponse({"status" : "error", "description": "Unauthorized wrong username or password"}, status=401)
		    else :
		    	json_data = r.json()
		    	request.session['access_token'] = json_data['access_token']
		    	return JsonResponse({
					"status" : "ok", 
					"token" : json_data['access_token']
			    })
	  	else :
	  		return JsonResponse({"status" : "error", "description": "Method not allowed"})
