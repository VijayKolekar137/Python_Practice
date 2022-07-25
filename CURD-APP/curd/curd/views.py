from django.shortcuts import render
from curd.models import curdst
from django.contrib import messages

def stdisplay(request):
    results = curdst.objects.all()
    return render(request,"Index.html",{"curdst":results})

def student(request):
    if request.method == "POST":
        if request.POST.get('stname') and request.POST.get('stmail') and request.POST.get('staddress') and request.POST.get('stmobile') and request.POST.get('stgender'):
            savest = curdst()
            savest.stname=request.POST.get('stname')
            savest.stmail=request.POST.get('stmail')
            savest.staddress=request.POST.get('staddress')
            savest.stmobile=request.POST.get('stmobile')
            savest.stgender=request.POST.get('stgender')
            savest.save()
            messages.success(request,"The Record"+savest.stname"is saved successfully..!")
            return render(request,"Create.html")
    else:
            return render(request,"Create.html")