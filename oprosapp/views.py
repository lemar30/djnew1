from django.shortcuts import render, redirect
from .forms import PeopleForm
from django.http import HttpResponse


def index(request):
    form = PeopleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'oprosapp/index.html', context={"form": form})

