from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
import requests

class usersMethod :
	@csrf_exempt
	def register(request):
		if request.method == 'POST':
			body_unicode = request.body.decode('utf-8')
			body = json.loads(body_unicode)
			displayName = body['displayName']
			url = "https://oauth.infralabs.cs.ui.ac.id/oauth/resource"
			if 'access_token' in request.session:
				access_token = request.session['access_token']
				headers = {"Authorization": "Bearer " + access_token}
				r = requests.get(url, headers=headers)
				if r.status_code != 401 :
					search_user = list(User.objects.filter(displayName=displayName))
					if len(search_user) == 0 :
						search_user_id = list(User.objects.filter(userId=r.json()['user_id']))
						if len(search_user_id) == 0 :
							newUser = User(userId=r.json()['user_id'], displayName=displayName)
							newUser.save()
							return JsonResponse({
								"status" : "ok", 
								"userId" : newUser.userId, 
								"displayName" : newUser.displayName
						    })
						else :
							return JsonResponse({
								"status" : "error",
								"description": "You've already registered under username " + search_user_id[0].displayName
						    })
					else :
						return JsonResponse({
					    	"status" : "error", 
					    	"description" : "User already exist"
					    })
				else :
					return JsonResponse({"status" : "error", "description": "Unauthorized please login first"}, status=401)
			else :
				return JsonResponse({"status" : "error", "description": "Unauthorized please login first"}, status=401)
		else :
			return JsonResponse({"status" : "error", "description": "Method not allowed"})

	@csrf_exempt
	def getUsers(request):
	  	if request.method == 'GET':
	  		url = "https://oauth.infralabs.cs.ui.ac.id/oauth/resource"
	  		if 'access_token' in request.session:
		  		access_token = request.session['access_token']
		  		headers = {"Authorization": "Bearer " + access_token}
		  		r = requests.get(url, headers=headers)
		  		if r.status_code != 401 :
		  			page = int(request.GET.get('page'))
		  			limit = int(request.GET.get('limit'))
		  			user_list = list(User.objects.all())
		  			if len(user_list) != 0 :
		  				data = []
		  				for user in user_list :
		  					json = {
		  						"userId" : user.userId,
		  						"displayName" : user.displayName
		  						}
		  					data.append(json)
		  				data = data[(page-1)*limit: (page-1)*limit+limit]
		  				if len(data) != 0 :
		  					return JsonResponse({
								"status" : "ok",
								"page" : page,
								"limit" : limit,
								"total" : len(data), 
								"data": data
							})
		  				else :
		  					return JsonResponse({"status" : "error", "description": "Page exceeded the limit"})
		  			else :
		  				return JsonResponse({"status" : "error", "description": "Comment not found in the time range or createdBy fields"})
		  		else : 
		  			return JsonResponse({"status" : "error", "description": "Unauthorized please login first"}, status=401)
		  	else :
		  		return JsonResponse({"status" : "error", "description": "Unauthorized please login first"}, status=401)
	  	else :
	  		return JsonResponse({"status" : "error", "description": "Method not allowed"})