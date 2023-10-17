import json
import os
from googleapiclient.discovery import build


class APIMixin:
    __api_key: str = os.getenv('YT_API_KEY')

    def __init__(self):
        self.youtube = APIMixin.get_service()

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=APIMixin.__api_key)

    @classmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
