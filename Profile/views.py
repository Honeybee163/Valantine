from django.shortcuts import render,redirect
from .models import Message

# Create your views here.
def home(request):
    return render(request,'home.html')


def quiz(request):
    return render(request,'quiz.html')

def purpose(request):
    return render(request,'purpose.html')

def received(request):
    message = Message.objects.all()
    return render(request,'received.html',{'message':message})

def describe(request):
    return render(request,'describe.html')

def question(request):
    return render(request,'question.html')


def final(request):
    if request.method == 'POST':
        note = request.POST.get('note')

        if note:  # safety check
            Message.objects.create(message=note)
            return redirect('received')

    return render(request, 'final.html')
