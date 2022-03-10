from rest_framework.test import APITestCase  # , APIClient


class VotesTestCase(APITestCase):
    '''
        Tests /votes endpoints
    '''

    # def setUp(self):
    #     self.client = APIClient()

    # def test_can_vote(self):
    #     assert False

    # def test_only_employees_can_vote(self):
    #     assert False

    # def test_cannot_vote_on_menu_not_uploaded_on_the_day(self):
    #     assert False

    # def test_fails_if_points_not_corectly_allocated(self):
    #     '''
    #         Total of poins should make 1 + 2 + 3 = 6
    #         All point should be integer and > 0
    #     '''
    #     assert False

    # def test_bad_request_if_all_three_menus_are_not_different(self):
    #     assert False
