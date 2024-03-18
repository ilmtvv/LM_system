import json

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from materials.models import Course
from users.models import User


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@casesb.com')
        self.user.set_password('qwe123RTY456')

        self.access_token = str(RefreshToken.for_user(self.user).access_token)

        self.client.force_authenticate(user=self.user, token=self.access_token)

        self.course = Course.objects.create(title='TestCasesb', owner=self.user.pk, )

        jsn = {
            "course": self.course.pk
        }

        self.client.post(
            reverse('subscriptions:subscription-post'),
            jsn
        )

        # print(.status_code)
        # print(.json())


    def test_subscription(self):
        responce = self.client.get(
            reverse('materials:course-list')
        )

        subscription = json.loads(*responce)['results'][0]['subscription']

        if subscription:
            jsn = {
                "course": self.course.pk
            }
            responce = self.client.post(
                reverse('subscriptions:subscription-post'),
                jsn
            )
            #print(json.loads(*responce))
            self.assertEqual(
                json.loads(*responce),
                {'message': 'subscription delete'},
            )
        else:
            self.assertEqual(
                json.loads(*responce),
                {'message': 'start subscription'},
            )
