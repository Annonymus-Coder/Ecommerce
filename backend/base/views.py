from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def getRouts(request):
    return JsonResponse('Hello', safe=False)


