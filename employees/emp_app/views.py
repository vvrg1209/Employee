from django.shortcuts import  redirect
from . models import Employee
from django.contrib.auth import logout as lgs
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Display the index page
def index(request):
    return render(request,'index.html')

# Display all employees in a tabular format
def all_emp(request):
    emps=Employee.objects.all()
    context={"emps":emps}
    return render(request,'all_emp.html',context)

# Add a new employee to the database
def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['Last_name']
        age = request.POST['age']
        dept = request.POST['department']
        if (first_name!='' and last_name!='' and age!='' and dept!=''):
            # Create and save the new employee to the database
            new_emp = Employee(first_name=first_name, last_name=last_name, age=age, dept=dept)
            new_emp.save()
            success_message = "Employee added successfully."
            return render(request, 'add_emp.html', {'success_message': success_message})
        else:
            error_message = "Invalid data entered or any feild is not entered"
            return render(request, 'add_emp.html', {'error_message': error_message})
    else:
        return render(request,'add_emp.html')

#Removing a employee from database
def remove_emp(request):
    emps = Employee.objects.all()
    context = {"emps": emps}
    if request.method == 'POST':
        selected_employee_name = request.POST.get('dropdown')
        try:
            selected_employee = get_object_or_404(Employee,
                                                  first_name=selected_employee_name.split()[0],
                                                  last_name=selected_employee_name.split()[1])
            selected_employee_id = selected_employee.employee_id
            selected_employee.delete()
            success_message = "Employee deleted successfully."
            return render(request, 'remove_emp.html', {'success_message': success_message})
        except Http404:
            error_message = "Selected employee does not exist. Please choose a valid employee."
            return render(request, 'remove_emp.html', {'error_message': error_message, 'context': context})
        except:
            error_message = "Selected employee does not exist. Please choose a valid employee."
            return render(request, 'remove_emp.html', {'error_message': error_message, 'context': context})
    else:
        return render(request, 'remove_emp.html', context)

# View details of a specific employee
def filter_emp(request):
    emps = Employee.objects.all()
    context = {"emps": emps}
    if request.method == 'POST':
        selected_employee_name = request.POST.get('dropdown')
        try:
            selected_employee = get_object_or_404(Employee,
                                                  first_name=selected_employee_name.split()[0],
                                                  last_name=selected_employee_name.split()[1])
            selected_employee_id = selected_employee.employee_id

            emps = Employee.objects.get(employee_id=selected_employee_id)
            return render(request, 'view_emp.html', {'emp':emps})
        except Http404:
            error_message = "Selected employee does not exist. Please choose a valid employee."
            return render(request, 'filter_emp.html', {'error_message': error_message, 'context': context})
        except:
            error_message = "Selected employee does not exist. Please choose a valid employee."
            return render(request, 'filter_emp.html', {'error_message': error_message, 'context': context})
    else:
        return render(request, 'filter_emp.html', context)


# Handle logout and redirect to the index page
def home(request):
    if request.method=="POST":
        lgs(request)
        return redirect('index')