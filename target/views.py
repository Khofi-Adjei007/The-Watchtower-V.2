from django.shortcuts import render



# Create your views here.
def subjectCards(request):
    return render(request,'subjectCards.html')