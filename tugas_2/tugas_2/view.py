from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add(request):
  if request.method == 'POST':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    a = body['a']
    b = body['b']
    hasil = a + b
    return JsonResponse({"a" : a, "b" : b, "hasil" : hasil})