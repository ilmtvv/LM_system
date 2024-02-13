from django.db import models

null_blank = {'null': True, 'blank': True}

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=25,)
    image = models.ImageField(upload_to='images/study', **null_blank)
    description = models.TextField(**null_blank)


class Lesson(models.Model):
    title = models.CharField(max_length=25,)
    image = models.ImageField(upload_to='images/study', **null_blank)
    description = models.TextField(**null_blank)
    video_link = models.URLField(**null_blank)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
