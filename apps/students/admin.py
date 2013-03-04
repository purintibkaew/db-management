from django.contrib import admin

from apps.students.models import Student, Group


class StudentInline(admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]


admin.site.register(Group, GroupAdmin)
