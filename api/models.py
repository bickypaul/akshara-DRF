from django.db import models

# This is database model for Boundaries
class Boundary(models.Model):
    district = models.CharField(max_length=200)
    block = models.CharField(max_length=200)
    cluster = models.CharField(max_length=200)
    gram_panchayat = models.CharField(max_length=200)
    
    def __str__(self):
        return self.district+"|"+self.block+"|"+self.cluster+"|"+self.gram_panchayat

# This is the database model for GP Contest data with respective contest results
class GPContest(models.Model):
    district = models.CharField(max_length=200)
    block = models.CharField(max_length=200)
    cluster = models.CharField(max_length=200)
    gram_panchayat = models.CharField(max_length=200)
    addition = models.IntegerField()
    subtraction = models.IntegerField()
    multiplication = models.IntegerField()
    division = models.IntegerField()

    def __str__(self):
        return self.district+"|"+self.schoolname

# This is for the Schools with respective contest results
class School(models.Model):
    schoolname = models.CharField(max_length=200)
    addition = models.IntegerField()
    subtraction = models.IntegerField()
    multiplication = models.IntegerField()
    division = models.IntegerField()

    def __str__(self):
        return self.schoolname


