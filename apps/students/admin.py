from django.contrib import admin

from apps.students.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
