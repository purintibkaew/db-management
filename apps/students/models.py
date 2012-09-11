from django.db import models


class Student(models.Model):
	name = models.CharField(max_lenght=35)
	date = models.DateField()
	student_ID = models.IntegerField()
	group = models.ForeignKey('Group')

    def __unicode__(self):
        return '%s' % (self.name)


class Group(models.Model):
	name = models.CharField(max_lenght=35)
	group_senior = models.ForeignKey(Student)

    def __unicode__(self):
        return '%s' % (self.name)
		