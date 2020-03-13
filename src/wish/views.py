from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wish
import  datetime
from .forms import WishForm
@login_required
def index(request):
    wishes = Wish.objects.filter(granted=0, user=request.user)
    wishes_were_granted = Wish.objects.filter(granted=1)
    print(wishes_were_granted)

    context = {
        'wishes': wishes,
        'wishes_were_granted': wishes_were_granted
    }
    return render(request, 'wish/index.html', context)

def create(request):
    if request.method == 'POST':
        wish_form = WishForm(request.POST)
        if wish_form.is_valid():
            Wish.objects.create(item=request.POST['item'],description=request.POST['description'], user=request.user)
            return redirect('/wish')
    else:
        wish_form = WishForm
    context = {
        'wish_form':wish_form
    }
    return render(request, 'wish/create.html', context)

def edit(request, id):
    wish = Wish.objects.get(id=id)
    if request.method == 'POST':
        wish.item = request.POST['item']
        wish.description = request.POST['description']
        wish.save()
        return redirect('/wish')

    context= {
        'wish': wish
    }
    return render(request, 'wish/edit.html', context)

def delete(request, id):
    wish = Wish.objects.get(id=id)
    wish.delete()
    return redirect('/wish')

def granted(request, id):
    wish = Wish.objects.get(id=id)
    wish.granted = 1
    wish.granted_date = datetime.datetime.now()
    wish.save()
    return redirect('/wish')

def newfunc():
    pass
