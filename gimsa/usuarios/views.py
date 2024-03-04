from django.shortcuts import get_object_or_404, render

def index(req):
    return render(req,'index.html')


