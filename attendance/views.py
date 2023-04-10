from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.template import loader
import pandas as pd
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from attendance.models import studentdetail,attendancedetail
from .forms import CreateUserForm


# SIGNUP
def signupPage(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context = {'form':form}
    
    return render(request, 'signup.html', context)



#LOGIN 
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    
    return render(request, 'login.html')    


#Dashboard
def homePage(request):
    return render(request, "home.html")    

#this is for adding students 
def studentpage(request):
    
   if request.method == 'POST':
       print(request.POST)
    
       studentdetail.objects.create(
        student_id= request.POST['Student_id'],
        first_name= request.POST['First_Name'],
        middle_name= request.POST['Middle_Name'],
        last_name = request.POST['Last_Name'],
        date_of_birth = request.POST['Date_of_Birth'],
        grade= request.POST['Grade'],
        parent_number = request.POST['Parent_Number'],
        profile_pic = request.POST['Profile_Pic'],
                                           
        )
      
       students= studentdetail.objects.all()
        
        
       
    
    
       context = {
        'students': students
    }
    
       return render(request,'studentrecord.html',context)






       
       
       
   return render(request,'students.html') 


#showing the details of the added students
def displayPage(request):

    students= studentdetail.objects.all()
    context = {
        'students': students
    }
    return render(request, "studentrecord.html",context)

    


#this is for marking the attendance       
def attendancePage(request):

    if request.method == 'POST':
       print(request.POST)
    
       attendancedetail.objects.create(
        S_id= request.POST['Student_Id'],
        date = request.POST['Date'],
        status= request.POST['Status'],)
      
       attendance= attendancedetail.objects.all()
        
        
       
    
    
       context = {
        'attendance': attendance
    }
    
       return render(request, 'attendancerecord.html', context)






       
       
       
   
    return render(request, "markattendance.html")



#showing the attendance Record 
def attendanceRecordPage(request):
    attendance= attendancedetail.objects.all()
        
        
       
    
    
    context = {
        'attendance': attendance
        }
    
    return render(request, "attendancerecord.html",context)    

# downloading the attendance record
def downloadData(request):
    students = attendancedetail.objects.all()
    data = []

    for student in students:
        data.append({
            "S_id":student.S_id,
            "date":student.date,
            "status":student.status
            

        })
    pd.DataFrame(data).to_csv("attendance.csv")
    return JsonResponse({
        

    })


#creating link for loading the edit.html page so that we can see 
def editpage(request, Id):
  students= studentdetail.objects.get(student_id = Id)
  templates = loader.get_template('edit.html')
  context = {
    'students': students
  }
  return HttpResponse(templates.render(context, request))
  

#student details can be edit
def editrecord(request, id):
    first= request.POST['first'],
    middle= request.POST['middle'],
    last = request.POST['last'],
    birthdate = request.POST['birthdate'],
    grade= request.POST['grade'],
    number = request.POST['number'],

    students = studentdetail.objects.get(student_id=id)

    
    students.first_name= first 
    students.middle_name=middle  
    students.last_name = last
    students.date_of_birth= birthdate
    students.grade = grade
    students.parent_number= number 
    
    students.save()
    
    return HttpResponseRedirect(reverse('record'))
