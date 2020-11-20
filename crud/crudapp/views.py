def crudapp (request):
    context = {}
    return render(request, 'crudapp/crud.html', context)

def crudbu (request):
    context = {}
    return render(request, 'crudapp/crudbu.html', context)