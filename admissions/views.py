from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.views.generic import View
from admissions.models import Teacher
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

#function based views , class based views

#functionbased
@login_required
def homepage(request):
    return render(request,"index.html")

def logoutUser(request):
    return render(request,'logout.html')
# To add admission
@login_required
def addadmission(request):
    #code to implement
    #return HttpResponse("This is add admission view")
    form=StudentModelForm
    studentform={'form':form}

    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request,'admissions/addadmission.html',studentform);


# To see the count of admissions
@login_required
def admissionsReport(request):
    #code to implement
    #return HttpResponse("This is admission report view")

    # get all the records from the table
    #store it in dictionary student

    result = Student.objects.all();
    students = {'allstudents':result}
    return render(request,'admissions/admissionsReport.html',students);
@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return admissionsReport(request)
@login_required
@permission_required('admissions.change_student') #add,delete,change,view(crud)
def updateStudent(request,id):
    s=Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict={'form':form}

    if request.method=='POST':
        form=StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admissionsReport(request)


    return render(request,'admissions/update-admission.html',dict)
            #code to implement
            #return HttpResponse("This is add admission view")
@login_required
def addVendor(request):

    form=VendorForm
    vform={'form':form}

    if request.method=='POST':
        form=VendorForm(request.POST)
        if form.is_valid():
            #implementation of hidden variables
            n=form.cleaned_data['name']
            a=form.cleaned_data['address']
            c=form.cleaned_data['contact']
            i=form.cleaned_data['item']

            request.session['name']=n;
            request.session['address']=a;
            request.session['contact']=c;
            request.session['item']=i;
            return homepage(request)

    return render(request,'admissions/addVendor.html',vform);

class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1>Hello This is first class based View</h1>")


class TeacherRead(ListView):
    model=Teacher
class GetTeacher(DetailView):
    model=Teacher
class AddTeacher(CreateView):
    model=Teacher
    fields=('name','subject','exp','contact')
class UpdateTeacher(UpdateView):
    model=Teacher
    fields=('name','contact')
    #success_url
class DeleteTeacher(DeleteView):
    model=Teacher
    success_url=reverse_lazy('listteachers')
