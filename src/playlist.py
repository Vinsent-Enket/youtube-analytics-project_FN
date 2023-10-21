import isodate
import datetime

from src.apimixin import APIMixin


class PlayList(APIMixin):

    """
    Предполагаю что задание рассчитывалось на то, что надо наследоваться от классов video и PLVideo, но в таком случае
    надо полностью переделывать субъекты них, чтобы они могли хранить сразу несколько значений, по этому в данном классе
    есть 3 типа запроса, данные по плейлисту, данные по видео(id) в плейлисте и по статистике нескольких видео, по совету
    подмешал класс предоставляющий объект для работы с ютуб(build)
    """

    def __init__(self, playlist_id):
        super().__init__()
        self.__total_duration = datetime.timedelta(0)
        self.playlists = self.youtube.playlists().list(id=playlist_id,part='contentDetails,snippet', maxResults=50).execute()
        self.title = self.playlists['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlists['items'][0]['id'] #как иначе вытащить юрлку я не понял, возможно через другой запрос, но так больше квот тратится
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',maxResults=50).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics', id=','.join(self.video_ids)).execute()


        self.calk_dur(self.video_response)

    @property
    def total_duration(self):
        return self.__total_duration

    def show_best_video(self):
        return self.top_url

    def calk_dur(self, video_response):
        self.likes = 0
        self.top_url = ''
        for video in video_response['items']:
            if int(video['statistics']['likeCount']) > self.likes:
                self.likes = int(video['statistics']['likeCount'])
                self.top_url = 'https://youtu.be/' + video['id']
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self.__total_duration += duration