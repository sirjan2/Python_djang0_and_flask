from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     products = [
#         {"name": "Product 1", "price": 10.00},
#         {"name": "Product 2", "price": 20.00},
#         {"name": "Product 3", "price": 30.00},
#         {"name": "Product 4", "price": 40.00},
#         {"name": "Product 5", "price": 50.00},
#     ]
#     return render(request,'home.html',{'products':products})

# def products(request):
#     return HttpResponse("This is products page")
def detail(request,question_id):
        return HttpResponse("You're looking at the question %s." % question_id)

def results(request,question_id):
        respsonse = "You're looking at the results of question %s."
        return HttpResponse(respsonse % question_id)

def vote(request, question_id):
        return HttpResponse("You're voting on question %s." %question_id)