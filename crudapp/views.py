from django.shortcuts import render, redirect
from crudapp.models import Student
from crudapp.forms import Studentform


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = Studentform()
        return render(request, 'index.html', {'form': form})


def show(request):
    students = Student.objects.all()
    return render(request, 'show.html', {'students': students})


def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/show')


def update(request, id):
    student = Student.objects.get(id=id)
    form = Studentform(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'student': student})
