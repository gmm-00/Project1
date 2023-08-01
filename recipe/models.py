from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(default='example@example.com')
    recipe_name = models.CharField(max_length=50, null=True, default=None)
    recipe_des = models.TextField()
    recipe_image = models.ImageField(upload_to='media', null=True)
    recipe_count = models.IntegerField(default=1)

    def __str__(self):
        return self.recipe_name




class Department(models.Model):
    department=models.CharField(max_length=50)



    class Meta:
        ordering = ['department']




    def __str__(self):
        return self.department




class StudentID(models.Model):
    student_id=models.CharField(max_length=20)


    class Meta:
        ordering = ['student_id']

    def __str__(self):
        return self.student_id




class Student(models.Model):
    department=models.ForeignKey(Department, related_name ='depart' ,on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID,related_name='studentid',on_delete=models.CASCADE)

    student_name=models.CharField(max_length=20)
    student_email=models.EmailField(unique=True)
    sutdent_age=models.IntegerField(default=18)
    student_address=models.TextField()



    class Meta:
        ordering = ['student_name']
        verbose_name='student'



    def __str__(self):
        return self.student_name







