from django.db import models

# Create your models here.


GRADES = (
    (1, "1"),
    (1.5, "1+"),
    (1.75, "2-"),
    (2, "2"),
    (2.5, "2+"),
    (2.75, "3-"),
    (3, "3"),
    (3.5, "3+"),
    (3.75, "4-"),
    (4, "4"),
    (4.5, "4+"),
    (4.75, "5-"),
    (5, "5"),
    (5.5, "5+"),
    (5.75, "6-"),
    (6, "6")
)


class Task(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Grade(models.Model):
    value = models.FloatField(choices=GRADES)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    @property
    def name(self):
        return "{}, {}, {}, {}".format(self.value, self.task, self.candidate, self.recruiter)

    def __str__(self):
        return self.name
