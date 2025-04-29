from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from .models import Student
# Create your views here.

def index(request):
    return render(request, 'students/index.html',{

    'students':Student.objects.all()            
        })

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form data directly to the database
            form.save()

            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()

    # Render the form for a GET request or after an invalid POST
    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, id):
    student = Student.objects.get(pk=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  # Save the changes to the database
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)

    # Render the form, whether it's a GET request or an invalid POST
    return render(request, 'students/edit.html', {
        'form': form
    })

def delete(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")

    if request.method == "POST":
        student.delete()
        return HttpResponseRedirect(reverse('index'))
    
    return HttpResponseRedirect(reverse('index'))
