from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'student_profile')
    name = models.CharField(max_length=50, blank=False)
    email_id = models.EmailField(max_length=100, blank=False)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name = 'teacher_profile')
    name = models.CharField(max_length=50, blank=False)
    email_id = models.EmailField(max_length=100, blank=False)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_student:
        instance.student_profile.save()
    else:
        Teacher.objects.get_or_create(user = instance)
