from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'content/index.html')

def slam(request):
    if request.method == 'GET':
        return render(request, 'content/slam.html', {'form': SlamForm()})
    else:
        try:
            form = SlamForm(request.POST)
            slam = form.save(commit=False)
            slam.save()
            return redirect('view')
            #newtodo.user = request.user

        except ValueError:
            return render(request, 'content/slam.html', {'form': SlamForm(), 'error': 'Bad data passed in. Try again.'})

def view(request):
    a = Slamm.objects.filter()
    # user1 = Devi.objects.all
    return render(request, 'content/viewing.html', {'a1': a})

def display(request):
    x = get_object_or_404(Slamm, pk=page)
    if request.method == "GET":
        form = SlamForm(instance=x)
        return render(request, 'content/display.html', {'x': x, 'form': form})
    else:
        try:
            form = SlamForm(instance=x)
            form.save()
            return redirect('view')
        except ValueError:
            return render(request, 'content/display.html', {'x': x, 'form': form})
