from django.shortcuts import render,redirect
from .forms import RegisterForm

def register(req):
    redirect_to = req.POST.get('next', req.GET.get('next', ''))
    if req.method=='POST':
        form=RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')

    else:
        form=RegisterForm()
    return render(req,'users/register.html',context={'form':form})


def index(req):
    return render(req,'index.html')

# Create your views here.
