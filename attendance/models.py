from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=30)
    Confirm_Paswword= models.CharField(max_length=30)



    
    def __str__(self):
        return self.Username


class studentdetail(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=30,null=True) 
    middle_name = models.CharField(max_length=30,null=True) 
    last_name = models.CharField(max_length=40,null=True) 
    date_of_birth = models.DateField(null=True,)
    grade = models.CharField(max_length=30)
    parent_number = models.IntegerField()
    profile_pic = models.ImageField(null=True,)
     


    def __str__(self):
        return self.first_name        




class attendancedetail(models.Model):
    S_id = models.IntegerField()
    date = models.DateField(null=True,)
    status = models.CharField(max_length=30)
    
     


    def __str__(self):
        return self.status               