from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def greet(request):
    if request.method == 'POST':
        name = request.POST['name']
        return render(request, 'greet.html', {'name': name})
    return render(request, 'index.html')
