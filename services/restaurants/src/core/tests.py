from rest_framework.test import APITestCase, APIClient


class MenuTestCase(APITestCase):
    '''
        Tests /restaurants/:restaurant-id/menus endpoints
    '''

    def setUp(self):
        self.client = APIClient()

    # def test_can_create_menu(self):
    #     assert False

    # def test_only_restaurant_manager_can_create_menus(self):
    #     assert False

    # def test_can_only_upload_one_menu_per_day(self):
    #     assert False

    # def test_fails_to_create_if_manager_does_not_exist(self):
    #     assert False
