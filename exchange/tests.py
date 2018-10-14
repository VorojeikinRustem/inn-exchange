from django.test import TestCase
from django.contrib.auth.models import User

from exchange.models import Inn, Profile


class ExchangeTestCase(TestCase):
    inn_1 = 11111
    inn_2 = 22222
    viktor = "Viktor"
    egor = "Egor"
    irina = "Irina"
    mihhail = "Mihail"
    price = 10

    def setUp(self):
        inn_1 = Inn.objects.create(inn=self.inn_1)
        inn_2 = Inn.objects.create(inn=self.inn_2)
        user_viktor = User.objects.create(username=self.viktor, password="superpasswordviktor")
        user_irina = User.objects.create(username=self.irina, password="superpasswordirina")
        Profile.objects.create(inn=inn_1, user=user_viktor, price=1000)
        Profile.objects.create(inn=inn_2, user=user_irina, price=1000)

    def test_create_inn(self):
        """ Inn's correct created """
        inn = Inn.objects.create(inn=self.inn_1)
        self.assertEqual(self.inn_1, inn.inn)

    def test_create_user(self):
        """ User's correct created """
        user = User.objects.create(username=self.mihhail)
        self.assertEqual(self.mihhail, user.username)

    def test_create_profile(self):
        """ Profile correct created """
        user = User.objects.create(
            username=self.egor,
            password="superpasswordegor"
        )
        inn = Inn.objects.get(inn=self.inn_1)
        profile = Profile.objects.create(
            user=user,
            inn=inn,
            price=999
        )
        self.assertEqual(self.egor, profile.user.username)

    def test_change_profile_price(self):
        """ Change profile price """
        inn = Inn.objects.get(inn=self.inn_2)
        profile = Profile.objects.get(inn=inn)
        price = profile.price
        profile.price -= self.price
        profile.save()
        self.assertEqual(profile.price + self.price, price)
