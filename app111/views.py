from django.shortcuts import render

# Create your views here.
def sky(request):
    return render(request,'sky.html')
