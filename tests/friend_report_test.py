from unittest import TestCase
from unittest.mock import Mock

from report.friends_report import FriendsReport


class FriendReportTest(TestCase):
    def setUp(self):
        api = Mock()
        api.get_user_info.return_value = [
            {
                'first_name': 'Иван',
                'last_name': 'Бураков',
                'country': {'id': 123, 'title': 'Россия'},
                'city': {'id': 123, 'title': 'Такеча'},
                'bdate': '23.1.2002',
                'sex': 2,
            },
        ]
        self.report = FriendsReport(api)

    def test_format_city(self):
        self.assertEqual(self.report.format_city({}, {'city': {'id': 360, 'title': 'Москва'}}), {'city': 'Москва'})

    def test_format_city_no_city(self):
        self.assertEqual(self.report.format_city({}, {}), {'city': 'Unknown'})

    def test_format_country(self):
        self.assertEqual(self.report.format_country({}, {'country': {'id': 1, 'title': 'Россия'}}),
                         {'country': 'Россия'})

    def test_format_country_no_country(self):
        self.assertEqual(self.report.format_country({}, {}), {'country': 'Unknown'})

    def test_format_date(self):
        self.assertEqual(self.report.format_date({}, {'bdate': '21.12.2002'}), {'birth_date': '2002.12.21'})

    def test_format_date_no_year(self):
        self.assertEqual(self.report.format_date({}, {'bdate': '21.12'}), {'birth_date': '12.21'})

    def test_format_date_no_date(self):
        self.assertEqual(self.report.format_date({}, {}), {'birth_date': 'Unknown'})

    def test_format_sex(self):
        self.assertEqual(self.report.format_sex({}, {'sex': 1}), {'sex': 'Жен'})

    def test_format_sex_no_sex(self):
        self.assertEqual(self.report.format_sex({}, {}), {'sex': 'Unknown'})

    def test_format_sex_uncorrect_sex(self):
        self.assertEqual(self.report.format_sex({}, {'sex': 'человек'}), {'sex': 'Unknown'})

    def test_get_data(self):
        expected = {
            'first_name': 'Иван',
            'last_name': 'Бураков',
            'country': 'Россия',
            'city': 'Такеча',
            'birth_date': '2002.1.23',
            'sex': 'Муж'
        }
        got = self.report.get_data(user_id=1)

        self.assertEqual(got, expected)
