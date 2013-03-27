from django.contrib import admin

from students.models import Student, Group, ModelChangeLog


class StudentInline(admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]


admin.site.register(Group, GroupAdmin)
admin.site.register(ModelChangeLog)
