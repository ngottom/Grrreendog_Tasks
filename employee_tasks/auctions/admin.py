from django.contrib import admin
from .models import User, Category, Listing, Comment, Section, Employee, EmployeeListing, employeeComment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Section)
admin.site.register(Employee)
admin.site.register(EmployeeListing)
admin.site.register(employeeComment)
