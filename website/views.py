from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {'title':'Mikey', 'content':'salam da'}
    return render(request, 'website/index.html', context)

