from src.apimixin import APIMixin


class Video(APIMixin):

    def __init__(self, id_video: str) -> None:
        super().__init__()
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""

        self.video = self.youtube.videos().list(id=id_video, part='snippet,statistics').execute()
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
    Откровенно говоря не понял, а зачем id видео и id playlist если нам нужна инфа именно по видео?
    Да и судя по метод принимает лишь 1 аргумент, один id
    И да, хоть и стоит метод videos он исправно дает всю нужную инфу
    Но код работает
    """

    def __init__(self, id_video: str, id_playlist):
        super().__init__(id_video)
        self.play_list = self.youtube.playlists().list(id=id_playlist, part='contentDetails,snippet',
                                                  maxResults=50, ).execute()
        self.play_list_id = self.play_list['items'][0]['id']
