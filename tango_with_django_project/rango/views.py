from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Summer.'}
    return render(request, 'rango/about.html', context=context_dict)
    #return HttpResponse("<a href='http://127.0.0.1:8000/rango/'> Rango says that this is the about page<a>")
