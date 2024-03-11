from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True,blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=200)
    age = models.IntegerField(default=0,null=False)

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"


