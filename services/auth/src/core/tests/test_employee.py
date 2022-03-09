from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
# from core.models import Employee
# from django.test import TestCase, override_settings


User = get_user_model()


class EmployeeTests(APITestCase):
    """ Tests the employees API """
    pass

    def setUp(self):
        self.client = APIClient()
        self.employee_payload = {
            "name": "nehemie",
            "email": "nehemie@mintales.com",
            "passord": "pass@API_#001"
        }

    # def test_can_create_employee(self):
    #     ''' Tests that we can create an employee '''
    #     # print(Employee.objects.all())
    #     # test does not return passowrd field
    #     assert False

    # def test_non_admin_cannot_create_employee(self):
    #     assert False
