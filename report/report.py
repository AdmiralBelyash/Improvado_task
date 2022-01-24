from .vk_api_wrapper import VkApiWrapper


class Report:
    def __init__(self, api: VkApiWrapper):
        self.api = api

    def get_data(self, user_id: int):
        pass
