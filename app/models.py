from django.db import models

# Create your models 


class School(models.Model):
    school_name=models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.school_name
class Student(models.Model):
    school_name=models.ForeignKey(School, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    id=models.CharField(max_length=100, primary_key=True)
    cls=models.IntegerField()
    email=models.EmailField(blank=True, null=True)
    doj=models.DateField()

    def __str__(self):
        return self.Name