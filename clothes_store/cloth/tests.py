from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import cloth
from rest_framework import status
from django.utils.http import urlencode
from django.contrib.auth.models import User

class clothTests(APITestCase):
    def post_cloth(self, name, _data_of_purchase, _brand_of_clothes):
        url = reverse(views.clothList.name)
        data = {'name':name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_cloth(self):
        new_cloth_name = 'IT'
        response = self.post_cloth(new_cloth_name)
        print("PK {0}".format(cloth.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert cloth.objects.count() == 1
        assert cloth.objects.get().name == new_cloth_name

    def test_post_existing_cloth_name(self):
        url = reverse(views.clothList.name)
        new_cloth_name = 'Duplicate IT'
        data = {'name':new_cloth_name}
        response_one = self.post_cloth(new_cloth_name)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_cloth(new_cloth_name)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST


    def test_update_cloth(self):
        cloth_name = 'IT'
        response = self.cloth(cloth_name)
        url = urls.reverse(views.clothDetail.name,None,{response.data['pk']})
        updated_cloth_name = 'New IT'
        data = {'name': updated_cloth_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_cloth_name

    def test_get_cloth(self):
        cloth_name = 'IT'
        response = self.cloth(cloth_name)
        url = urls.reverse(views.clothDetail.name,None,{response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == cloth_name