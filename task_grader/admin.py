from django.contrib import admin

# Register your models here.
from task_grader.models import Recruiter, Candidate, Task, Grade

admin.site.register(Recruiter)
admin.site.register(Candidate)
admin.site.register(Task)
admin.site.register(Grade)