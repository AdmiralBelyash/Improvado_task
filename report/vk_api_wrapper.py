import vk_api


class VkApiWrapper:
    def __init__(self, vk: vk_api.vk_api.VkApiMethod):
        self.vk = vk

    def get_friends_info(self, user_id):
        info = self.vk.friends.get(user_id=user_id, fields='sex, country, city, bdate')
        return info

