import vk_api


class VkApiWrapper:
    def __init__(self, vk: vk_api.vk_api.VkApiMethod):
        self.vk = vk

    def get_user_friends(self, user_id):
        friends_id = self.vk.friends.get(user_id=user_id)
        return friends_id["items"]

    def get_user_info(self, user_id):
        info = self.vk.users.get(user_id=user_id, fields='sex, country, city, bdate')
        return info

