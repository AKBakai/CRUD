from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
    else:
        form = StudentForm()
        return render(request, 'index1.html', {'form': form})

def home(request):
    students = Student.objects.all()
    return render(request, 'show1.html', {'students':students})

def editstudent(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit1.html', {'student':student})

def updatestudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit1.html', {'student': student})

def deletestudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')
