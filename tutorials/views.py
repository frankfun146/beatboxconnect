from django.shortcuts import render

# Create your views here.


def tutorials(request):
    context = {}
    return render(request, 'tutorials/tutorials.html', context)


def tutorial_detail(request, sound_name):
    context = {'sound_name': sound_name}
    return render(request, 'tutorials/tutorial_detail.html', context)
