from django.test import TestCase
from .models import Hifz
import datetime
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# Create your tests here.



class ModelTestCase(TestCase):
    def setUp(self):
        self.ayat_number = 85
        self.surah_number = 56
        self.surah_name = "Al-Waaqia"
        self.ayat = Hifz(surah=self.surah_number, ayat_number=self.ayat_number);

    def test_model_can_show_surah_name(self):
        self.assertEqual(self.surah_name, self.ayat.getSurahNameString());

    def test_model_return_now_for_last_added_after_initialization(self):
        self.assertEqual(self.ayat.getLastRefreshed(), datetime.date.today())

    def test_model_getter_ifdate_isinvalid_(self):
        self.ayat.last_refreshed = "2/3/2018"
        self.failUnlessRaises(TypeError, self.ayat.getLastRefreshed);

    def test_model_setter_ifdate_isinvalid(self):
        self.failUnlessRaises(TypeError, self.ayat.setLastRefreshed, "2/3/2018")

    # def test_model_can_save_and_retrieve(self):
    #     last_refreshed = datetime.datetime(year=2017, month=6, day=5, hour=18, minute=20)
    #     self.ayat.setLastRefreshed(last_refreshed)
    #     self.ayat.save()
    #     self.

# define the ViewTestCase testsuite right after the ModelTestCase
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # date format needs to be  YYYY[-MM[-DD]]
        self.hifz_data = {'surah': 3, 'ayat_number': 4, 'last_refreshed': '2017-02-02'}
        self.response = self.client.post(
            reverse('create'),
            self.hifz_data,
            format="json"
        )

    def test_api_can_create_list(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_list(self):
        hifz_list = Hifz.objects.all()

        response = self.client.get(
            reverse('details',
            kwargs = {'pk': hifz_data.id}),
            # format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(hifz_data)
        print(response)
        self.assertContains(response, hifz_data)

    def test_can_update_list(self):
        hifz_data = Hifz.objects.get()
        update_data = {'surah': 22, 'ayat_number': 3, 'last_refreshed': '2018-01-01'}
        response = self.client.put(reverse('details',   kwargs={'pk': hifz_data.id}), update_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete(self):
        hifz_data = Hifz.objects.get()
        response = self.client.delete(reverse('details', kwargs={'pk': hifz_data.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)