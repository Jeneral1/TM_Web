from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  CAT_CHOICES = [
    ('Work', 'Work Task'),
    ('Personal', 'Personal Task'),
    ('Home', 'House Chores'),
    ('Health', 'Health Check'),
    ('Education', 'Education'),
    ('Social', 'Social Task'),
  ]
  title = models.CharField(max_length=200)
  desc = models.TimeField(blank=True, null=True)
  category = models.CharField(max_length=100, choices=CAT_CHOICES, default='Personal')
  completed = models.BooleanField(default=False)
  due_date = models.DateField()
  created_at = models.DateTimeField(default=timezone.now)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title} - {self.category}"
  