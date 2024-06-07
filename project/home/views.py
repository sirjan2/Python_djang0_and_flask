from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question,Choice
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
def index(request):
    latest_questions=Question.objects.order_by('-pub_date')[:5]
        # for question in latest_questions:
    #     print(question.question_text)

    # output = ", ".join([q.question_text for q in latest_questions])

    # questions_text=[]

    # for question in latest_question:
    #         questions_text.append(question.question_text)

    # output='<br>'.join(questions_text)

    # return HttpResponse(output)
    return render(request,'home/index.html',{'latest_questions':latest_questions})

def detail(request,question_id):
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question not found")
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'home/detail.html',{'question':question})

    # return HttpResponse("You're looking at the question %s." % question_id)



def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
    except(KeyError, Choice.DoesNotExist):
        return HttpResponse("Error occured data not found or invalid data")
    return HttpResponse("Thanks for voting  for "+selected_choice.choice_text+" in "+question.question_text+".")

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"home/results.html",{'question':question})
    