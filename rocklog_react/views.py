from django.shortcuts import render

def app(request):
    return render(request, 'rocklog_react/index.html')
    