from django.db import models

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)  # Set automatically when the object is created
    updated_at = models.DateTimeField(auto_now=True)  # Set automatically when the object is updated
    status = models.BooleanField(default=True)  # Use BooleanField instead of CharField for a True/False value

    def __str__(self):
        return self.name
