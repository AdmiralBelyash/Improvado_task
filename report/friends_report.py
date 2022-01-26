from .report_base import Report


class FriendsReport(Report):
    def format_city(self, temp_data: dict, info: dict):
        if 'city' in info:
            temp_data['city'] = info['city']['title']
        else:
            temp_data['city'] = 'Unknown'
        return temp_data

    def format_country(self, temp_data: dict, info: dict):
        if 'country' in info:
            temp_data['country'] = info['country']['title']
        else:
            temp_data['country'] = 'Unknown'
        return temp_data

    def format_sex(self, temp_data: dict, info: dict):
        if 'sex' in info:
            if info['sex'] == 2:
                temp_data['sex'] = 'Муж'
            elif info['sex'] == 1:
                temp_data['sex'] = 'Жен'
            else:
                temp_data['sex'] = 'Unknown'
        else:
            temp_data['sex'] = 'Unknown'
        return temp_data

    def format_date(self, temp_data: dict, info: dict):
        if 'bdate' in info:
            date = info['bdate'].split('.')
            temp_data['birth_date'] = '.'.join(date[::-1])
        else:
            temp_data['birth_date'] = 'Unknown'
        return temp_data

    def get_data(self, user_id: int):

        data = []
        friends_info = self.api.get_friends_info(user_id)['items']
        for info in friends_info:
            temp_data = {}
            temp_data['first_name'] = info['first_name']
            temp_data['last_name'] = info['last_name']
            self.format_country(temp_data, info)
            self.format_city(temp_data, info)
            self.format_date(temp_data, info)
            self.format_sex(temp_data, info)
            data.append(temp_data)
        return data
