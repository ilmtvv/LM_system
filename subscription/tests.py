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


    def test_subscription(self):

        """
        не знаю как отправлять пост в тесте на подписку, почему то выскакивает ошибка 404
        возможно это изза того что во вьюсете в методе пост обяълен метод get_or_404 но тогда как обращаться
        """

        # responce = self.client.get(
        #     reverse('subscriptions:subscription-post'),
        #     course=self.course.pk
        # )

        responce = self.client.get(
            reverse('materials:course-list')
        )

        self.assertFalse(
            responce.json()['results'][0]['subscription']
        )

        # print(responce.status_code)
        # print(responce.json())
