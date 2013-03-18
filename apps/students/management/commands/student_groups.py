from django.core.management.base import BaseCommand, CommandError

from apps.students.models import Student, Group


class Command(BaseCommand):

    def handle(self, *args, **options):
        groups = Group.objects.all()
        for group in groups:
            self.stdout.write('Group: %s' % group.name)
            self.stdout.write('  students:')
            for student in group.student_set.all():
                self.stdout.write('    - %s' % student.name)
