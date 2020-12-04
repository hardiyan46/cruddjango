from django.shortcuts import render

def crud (request):
    context = {}
    return render(request, 'crudapp/crud.html', context)

def crudbu (request):
    context = {}
    return render(request, 'crudapp/crudbu.html', context)

def logbook(request):
    context = {}
    return render (request, 'crudapp/logbook.html', context)