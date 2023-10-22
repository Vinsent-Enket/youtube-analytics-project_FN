from src.apimixin import APIMixin


class Video(APIMixin):

    def __init__(self, id_video: str) -> None:
        super().__init__()
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.video = self.youtube.videos().list(id=id_video, part='snippet,statistics').execute()
        try:
            self.id = self.video['items'][0]['id']
        except IndexError:
            print("ОШИБКА")
            self.id = id_video
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None
        else:
            self.title = self.video['items'][0]['snippet']['title']
            self.url = self.video['items'][0]['snippet']['thumbnails']['default']['url']
            self.view_count = self.video['items'][0]['statistics']['viewCount']
            self.like_count = int(self.video['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.title

    def __repr__(self):
        return (f'Название -  {self.title}\n'
                f'адрес - {self.url}\n'
                f'id - {self.id}\n'
                f'просмотры - {self.viewCount}\n'
                f'лайки - {self.likeCount}\n')


class PLVideo(Video):

    def __init__(self, id_video: str, id_playlist):
        super().__init__(id_video)
        self.play_list = self.youtube.playlists().list(id=id_playlist, part='contentDetails,snippet',
                                                  maxResults=50, ).execute()
        self.play_list_id = self.play_list['items'][0]['id']
