from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import TODO
# Create your views here.
def index(req):
    todo = TODO.objects.all()
    if req.method=='POST':
        title = req.POST['title']
        if(len(title)==0):
            return redirect('/')
        new_todo = TODO(title=title)
        new_todo.save()
        messages.success(req,'Event added successfully!')
        return redirect('/')

    return render(req,'index.html',{'todos':todo})

def delete(req,pk):
    to_be_deleted = TODO.objects.get(id=pk)
    to_be_deleted.delete()
    return redirect('/')
    