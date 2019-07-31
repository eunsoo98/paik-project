from django.shortcuts import render

def index(request):
    return render(request, 'mysite/index.html')

def blogleftsidebar(request):
    return render(request, 'mysite/blogleftsidebar.html')

def activity(request):
    return render(request, 'mysite/activity.html')

def education(request):
    return render(request, 'mysite/education.html')

def finance(request):
    return render(request, 'mysite/finance.html')

def translation(request):
    return render(request, 'mysite/translation.html')

def travel(request):
    return render(request, 'mysite/travel.html')

def welfare(request):
    return render(request, 'mysite/welfare.html')