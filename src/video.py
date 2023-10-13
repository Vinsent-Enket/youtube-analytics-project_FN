import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:

    def __init__(self, id_video: str) -> None:

        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""

        self.video = youtube.videos().list(id=id_video, part='snippet,statistics').execute()
        self.id = self.video['items'][0]['id']
        self.title = self.video['items'][0]['snippet']['title']
        self.url = self.video['items'][0]['snippet']['thumbnails']['default']['url']
        self.viewCount = self.video['items'][0]['statistics']['viewCount']
        self.likeCount = int(self.video['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.title

    def __repr__(self):
        return (f'Название -  {self.title}\n'
                f'адрес - {self.url}\n'
                f'id - {self.id}\n'
                f'просмотры - {self.viewCount}\n'
                f'лайки - {self.likeCount}\n')


class PLVideo(Video):
    """
    Откровенно говоря не понял, а зачем id видео и id playlist если нам нужна инфа именно по плейлисту?
    Да и судя по метод принимает лишь 1 аргумент, один id
    И да, хоть и стоит метод videos он исправна дает всю нужную инфу
    """
    def __init__(self, id_video: str, id_playlist):
        super().__init__(id_video)
        self.play_list = youtube.videos().list(id=id_playlist, part='snippet,statistics').execute()
