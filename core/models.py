from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TYPES = (
	(0, "Coding"),
	(1, "MCQ"),
	(2, "Free Test")
)


DEGREES = (
	(0, "Bachelors"),
	(1, "Masters"),
	(2, "PHD")
)
	
class Country(models.Model):

	name = models.CharField(max_length=255)


class College(models.Model):

	name = models.CharField(max_length=255)
	country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
	acceptance_rate = models.IntegerField(null=True)
	highest_degree = models.IntegerField(choices=DEGREES, default=0)


class AcademicField(models.Model):

	name = models.CharField(max_length=255)


class AcademicBranch(models.Model):

	name = models.CharField(max_length=255)
	field = models.ForeignKey(AcademicField, on_delete=models.CASCADE)


class FieldRank(models.Model):

	college = models.ForeignKey(College, on_delete=models.CASCADE)
	field = models.ForeignKey(AcademicField, on_delete=models.CASCADE)
	rank = models.IntegerField(null=True)


class BranchRank(models.Model):

	college = models.ForeignKey(College, on_delete=models.CASCADE)
	branch = models.ForeignKey(AcademicBranch, on_delete=models.CASCADE)
	rank = models.IntegerField(null=True)
	
	