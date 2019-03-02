from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Comment
from datetime import datetime, date, time
import pytz

class commentMethod :
	@csrf_exempt
	def create(request):
	  if request.method == 'POST':
	    body_unicode = request.body.decode('utf-8')
	    body = json.loads(body_unicode)
	    comment = body['comment']
	    newComment = Comment(comment=comment, createdBy="admin", createdAt=datetime.now(), updatedAt=datetime.now())
	    newComment.save()
	    return JsonResponse({
	    	"status" : "ok", 
	    	"data": {
		    	"id" : newComment.id, 
		    	"comment" : newComment.comment, 
		    	"createdBy": newComment.createdBy, 
		    	"createdAt": newComment.createdAt, 
		    	"updatedAt": newComment.updatedAt
	    	}
	    })
	    
	@csrf_exempt
	def delete(request):
	  if request.method == 'HAPUS':
	  	body_unicode = request.body.decode('utf-8')
	  	body = json.loads(body_unicode)
	  	id = body['id']
	  	comment_list = list(Comment.objects.filter(id=id))
	  	if (len(comment_list) != 0) :
	  		Comment.objects.filter(id=id).delete()
	  		return JsonResponse({"status" : "ok"})
	  	else :
	  		return JsonResponse({"status" : "error", "description": "Id Not Found"})
	    
	@csrf_exempt
	def update(request):
	  if request.method == 'UBAH':
	    body_unicode = request.body.decode('utf-8')
	    body = json.loads(body_unicode)
	    id = body['id']
	    newComment = body['comment']
	    comment_list = list(Comment.objects.filter(id=id))
	    if (len(comment_list) != 0) :
	    	comment_list[0].comment = newComment
	    	comment_list[0].updatedAt = datetime.now()
	    	comment_list[0].save()
	    	return JsonResponse({
	    		"status" : "ok", 
	    		"data": {
	    			"id" : comment_list[0].id, 
					"comment" : comment_list[0].comment, 
					"createdBy": comment_list[0].createdBy, 
					"createdAt": comment_list[0].createdAt, 
				 	"updatedAt": comment_list[0].updatedAt
				}
			})
	    else :
	    	return JsonResponse({"status" : "error", "description": "Id Not Found"})

	@csrf_exempt
	def getById(request):
	  if request.method == 'GET':
	  	id = int(request.GET.get('id'))
	  	comment_list = list(Comment.objects.filter(id=id))
	  	if (len(comment_list) != 0) :
	  		return JsonResponse({
		    	"status" : "ok", 
		    	"data": {
			    	"id" : comment_list[0].id, 
			    	"comment" : comment_list[0].comment, 
			    	"createdBy": comment_list[0].createdBy, 
			    	"createdAt": comment_list[0].createdAt, 
			    	"updatedAt": comment_list[0].updatedAt
			    	}
			    })
	  	else :
	  		return JsonResponse({"status" : "error", "description": "Id Not Found"})
	    
	@csrf_exempt
	def getAll(request):
	  if request.method == 'GET':
	  	page = int(request.GET.get('page'))
	  	limit = int(request.GET.get('limit'))
	  	createdBy = str(request.GET.get('createdBy'))
	  	startDate = request.GET.get('startDate')
	  	endDate = request.GET.get('endDate')
	  	startDateArr = startDate.split("-")
	  	endDateArr = endDate.split("-")
	  	timeNow = time(0, 0)
	  	dateStart = date(int(startDateArr[0]), int(startDateArr[1]), int(startDateArr[2]))
	  	dateEnd = date(int(endDateArr[0]), int(endDateArr[1]), int(endDateArr[2]))
	  	datetimeStart = datetime.combine(dateStart, timeNow)
	  	datetimeEnd = datetime.combine(dateEnd, timeNow)
	  	comment_list = list(Comment.objects.filter(updatedAt__lte=datetimeEnd, updatedAt__gte=datetimeStart, createdBy=createdBy))
	  	if len(comment_list) != 0 :
	  		data = []
	  		for comment in comment_list :
	  			json = {
	  				"id" : comment.id, 
			    	"comment" : comment.comment, 
			    	"createdBy": comment.createdBy, 
			    	"createdAt": comment.createdAt, 
			    	"updatedAt": comment.updatedAt
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
	    