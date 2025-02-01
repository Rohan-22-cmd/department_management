from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from .forms import DepartmentForm

# List of departments
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {'departments': departments})

# Create a new department
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect to department list after saving
    else:
        form = DepartmentForm()
    return render(request, 'departments/department_form.html', {'form': form})

# Update an existing department
def department_update(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect to department list after updating
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'departments/department_form1.html', {'form': form, 'department': department})

# Delete a department
def department_delete(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')  # Redirect to department list after deletion
    return render(request, 'departments/department_confirm_delete.html', {'department': department})
