from django.contrib.auth.models import User
from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=500)
    brand = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField('date published', auto_now_add=True)
    quantity = models.IntegerField(max_length=200)
    condition = models.CharField(max_length=200)
    description = models.TextField()
    #Permissions
    music_ed = models.BooleanField('Music Education', default=False)
    pre_gate = models.BooleanField('Pre-Music Tech', default=False)
    post_gate = models.BooleanField('Music Tech', default=True)
    staff = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User)
    project = models.CharField(max_length=50)
    equipment = models.ManyToManyField('Equipment')
    reserved_time = models.DateTimeField(auto_now_add=True)  # Time reservation was placed by the student
    out_time = models.DateTimeField()  # Time reservation officially starts
    in_time = models.DateTimeField()  # Time equipment is due
    checked_out_time = models.DateTimeField(null=True, blank=True)  # Time equipment is actually checked out
    checked_in_time = models.DateTimeField(null=True, blank=True)  # Time equipment is actually returned
    is_approved = models.BooleanField()

    class Meta:
        ordering = ["out_time"]