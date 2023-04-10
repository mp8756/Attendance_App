from django.contrib import admin
from attendance.models import User,studentdetail,attendancedetail
# Register your models here.
admin.site.register(User)
admin.site.register(studentdetail)
admin.site.register(attendancedetail)
