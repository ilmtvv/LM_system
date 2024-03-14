from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.group = Group.objects.create(
            pk=1,
            name='managers',
        )

        self.user = User.objects.create(email='test@case.com')
        self.user.set_password('qwe123RTY456')

        # self.user.groups.set((1,))    # add user to manager

        self.access_token = str(RefreshToken.for_user(self.user).access_token)
        # print(access_token)
        # print(self.user)

        self.client.force_authenticate(user=self.user, token=self.access_token)

        self.course = Course.objects.create(title='TestCase', owner=self.user.pk,)

        self.lesson = Lesson.objects.create(
            title='testcase',
            course=self.course,
            owner=self.user.pk,
        )


    def test_get_lesson_list(self):
        responce = self.client.get(
            reverse('materials:lesson-list')
        )

        # print(responce.status_code)
        # print(responce.json())

        self.assertEqual(
            responce.status_code,
            status.HTTP_200_OK
        )


    def test_lesson_create(self):
        lesson = {
            'title': 'testcase2',
            'course': self.course.pk,
            'description': 'https://www.youtube.com/'
        }

        responce = self.client.post(
            reverse('materials:lesson-create'),
            lesson
        )

        # print(responce.status_code)
        # print(responce.json())

        if self.user.groups.filter(pk=1).exists():
            self.assertEqual(
                responce.status_code,
                status.HTTP_403_FORBIDDEN
            )
        elif not self.user.groups.filter(pk=1).exists():
            self.assertEqual(
                responce.status_code,
                status.HTTP_201_CREATED
            )


    def test_lesson_create_validation(self):
        lesson = {
            'title': 'testcase3',
            'course': self.course.pk,
            'description': 'https://www.qwe.com/'
        }

        responce = self.client.post(
            reverse('materials:lesson-create'),
            lesson
        )

        # print(responce.status_code)
        # print(responce.json())

        if self.user.groups.filter(pk=1).exists():
            self.assertEqual(
                responce.status_code,
                status.HTTP_403_FORBIDDEN
            )
        elif not self.user.groups.filter(pk=1).exists():
            self.assertEqual(
                responce.status_code,
                status.HTTP_400_BAD_REQUEST,
            )


    def test_lesson_patch(self):
        lesson = {
            'title': 'newname',
            'owner': self.user.pk,
        }

        responce = self.client.patch(
            reverse('materials:lesson-update', kwargs={'pk': self.lesson.pk}),
            lesson,
            )

        # print(responce.status_code)
        # print(responce.json())

        self.assertEqual(
            responce.status_code,
            status.HTTP_200_OK
        )


    def test_lesson_delete(self):
        responce = self.client.delete(
            reverse('materials:lesson-delete', kwargs={'pk': self.lesson.pk}),
            )

        #print(responce.status_code)

        self.assertEqual(
            responce.status_code,
            status.HTTP_204_NO_CONTENT
            )
