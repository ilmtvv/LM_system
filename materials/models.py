from django.db import models


null_blank = {'null': True, 'blank': True}


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/study', **null_blank)
    description = models.TextField(**null_blank)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, **null_blank)
    price = models.PositiveIntegerField(null=True, blank=True, )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    title = models.CharField(max_length=25,)
    image = models.ImageField(upload_to='images/study', **null_blank)
    description = models.TextField(**null_blank)
    video_link = models.URLField(**null_blank)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, **null_blank)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


class PaymentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id_payment_course = models.CharField(max_length=555, **null_blank)
    url_payment_course = models.URLField(max_length=555, default='')

    def __str__(self):
        return f'{self.id_payment_course}'

    class Meta:
        verbose_name = 'payment-course'
        verbose_name_plural = 'payments-courses'
