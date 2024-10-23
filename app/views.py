from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insertSchool(request):
    

    if request.method=="POST":
        sn=request.POST['sn']
        SO=School.objects.get_or_create(school_name=sn)
        return HttpResponse(f'{sn} is created')
    return render(request, 'insertSchool.html')



def insertStudent(request):
    LSO=School.objects.all()
    d={'LSO':LSO}#listSchoolOBjects

    if request.method=='POST':
        #return HttpResponse(request.POST['tn'])
    
        sn=request.POST['sn']
        SO=School.objects.get(school_name=sn)
        n=request.POST['n']
        id=request.POST['id']
        c=request.POST['c']
        e=request.POST['e']
        d=request.POST['d']
        STO=Student.objects.get_or_create(school_name=SO,Name=n, id=id,cls=c,email=e, doj=d)
        return HttpResponse(f'{n} is created')
    return render(request, 'insertStudent.html', d)





def selectMultiple(request):
    LSO=School.objects.all()
    d={'LSO': LSO}

    if request.method=="POST":
        MSN=request.POST.getlist('sn')#multipleSchoolName
        EQLS=Student.objects.none()#emptyQueryListSet
        for school in MSN:
            EQLS=EQLS|Student.objects.filter(school_name=school)
        d1={'EQLS':EQLS}
        return render(request, 'displayStudent.html', d1)
    return render(request, 'selectMultiple.html', d)


def checkBox(request):
    LSO=School.objects.all()
    d={'LSO': LSO}
 
 
    return render(request, 'checkBox.html', d)