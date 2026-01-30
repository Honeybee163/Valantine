from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'home.html')


def quiz(request):
    return render(request,'quiz.html')

def purpose(request):
    return render(request,'purpose.html')

def received(request):
    # When accessed directly, just show the fallback message
    return render(request, 'received.html', {'message': None})

def describe(request):
    return render(request,'describe.html')

def question(request):
    return render(request,'question.html')




def final(request):
    if request.method == 'POST':
        note = request.POST.get('note')

        if note:
            # 🔥 SAVE TO DATABASE
            ProfileMessage.objects.create(
                message=note
            )

            # 🔥 THEN render page
            return render(request, 'received.html', {'message': note})

    return render(request, 'final.html')
