from django.shortcuts import render, redirect
from .models import Pupil
from .forms import PupilForm


def addpupil(request):
    if request.method == 'POST':
        form = PupilForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('glav')
            except:
                pass
    else:
        form = PupilForm()
        return render(request, 'index2.html', {'form': form})

def glav(request):
    pupils = Pupil.objects.all()
    return render(request, 'show2.html', {'pupils':pupils})

def editpupil(request, id):
    pupil = Pupil.objects.get(id=id)
    return render(request, 'edit2.html', {'pupil':pupil})

def updatepupil(request, id):
    pupil = Pupil.objects.get(id=id)
    form = PupilForm(request.POST, instance=pupil)
    if form.is_valid():
        form.save()
        return redirect('glav')
    return render(request, 'edit2.html', {'pupil': pupil})

def deletepupil(request, id):
    pupil = Pupil.objects.get(id=id)
    pupil.delete()
    return redirect('glav')
