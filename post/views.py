from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
'''
FVC (function-based view) - представления, основанные на функциях
CBV (class based view) - представления, основанные на классах
'''

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World~!")

def current_date_view(request):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current date and time: {current_date}")

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbuy user")

def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')