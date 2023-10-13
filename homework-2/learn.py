import json
import os
from googleapiclient.discovery import build
import isodate

api_key = 'AIzaSyDoXfDhCmEBqP323Mfo599sILGCvB9-Gb4'

value = os.getenv('YT_API_KEY')
print(value)

"""value2 = os.getenv('PATH')
print(value2)"""


"""youtube = build('youtube', 'v3', developerKey=api_key)
channel = youtube.channels().list(id='UC-OVMPlMA3-YCIeg4z5z23A', part='snippet,statistics').execute()

print(youtube)"""






{'kind': 'youtube#channelListResponse',
 'etag': 'WO_oOipUFQCGzvojWpd8sg9osUA',
 'pageInfo':
     {'totalResults': 1, 'resultsPerPage': 5},
 'items':
     [{'kind': 'youtube#channel',
       'etag': 'egfL1jK3GdLX2FlZfRwyPMd9Fok',
       'id': 'UC-OVMPlMA3-YCIeg4z5z23A',
       'snippet':
           {'title': 'MoscowPython',
            'description': 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)',
            'customUrl': '@moscowdjangoru',
            'publishedAt': '2012-07-13T09:48:44Z',
            'thumbnails':
                {'default':
                     {'url': 'https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s88-c-k-c0x00ffffff-no-rj',
                      'width': 88,
                      'height': 88},
                 'medium':
                     {'url': 'https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s240-c-k-c0x00ffffff-no-rj',
                      'width': 240,
                      'height': 240},
                 'high':
                     {'url': 'https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s800-c-k-c0x00ffffff-no-rj',
                      'width': 800,
                      'height': 800}},
            'localized':
                {'title': 'MoscowPython',
                 'description': 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)'},
            'country': 'RU'},
       'statistics':
           {'viewCount': '2423559',
            'subscriberCount': '26500',
            'hiddenSubscriberCount': False,
            'videoCount': '708'}}]}


{'kind': 'youtube#videoListResponse',
 'etag': 'Jj1ZqRJVl4u-5YP5OYSC0ZjmZ1I',
 'items':
     [{'kind':'youtube#video',
       'etag': '38NDLbXHldNlHxy8st1TPByNRbE',
       'id': 'AWX4JnAnjBE',
       'snippet':
           {'publishedAt': '2013-11-13T07:02:16Z',
            'channelId': 'UC-OVMPlMA3-YCIeg4z5z23A',
            'title': 'GIL в Python: зачем он нужен и как с этим жить',
            'description': 'Григорий Петров\n12 сентября 2013\nMoscow Django Meetup № 14\n\nВ своем докладе Григорий проведет краткий экскурс в историю потоков и расскажет, зачем был создан GIL. Будут рассмотрены практические вопросы многопоточности в Python и способы работы с GIL.\nСлайды выступления: http://www.moscowpython.ru/meetup/14/gil-and-python-why/',
            'thumbnails':
                {'default':
                     {'url': 'https://i.ytimg.com/vi/AWX4JnAnjBE/default.jpg',
                      'width': 120,
                      'height': 90},
                 'medium':
                     {'url': 'https://i.ytimg.com/vi/AWX4JnAnjBE/mqdefault.jpg',
                      'width': 320,
                      'height': 180},
                 'high':
                     {'url': 'https://i.ytimg.com/vi/AWX4JnAnjBE/hqdefault.jpg',
                      'width': 480,
                      'height': 360},
                 'standard':
                     {'url': 'https://i.ytimg.com/vi/AWX4JnAnjBE/sddefault.jpg',
                      'width': 640,
                      'height': 480},
                 'maxres':
                     {'url': 'https://i.ytimg.com/vi/AWX4JnAnjBE/maxresdefault.jpg',
                      'width': 1280,
                      'height': 720}},
            'channelTitle': 'MoscowPython',
            'tags': ['Moscow Django Meetup', 'python', 'moscowdjango'],
            'categoryId': '28',
            'liveBroadcastContent': 'none',
            'localized':
                {'title': 'GIL в Python: зачем он нужен и как с этим жить',
                 'description': 'Григорий Петров\n12 сентября 2013\nMoscow Django Meetup № 14\n\nВ своем докладе Григорий проведет краткий экскурс в историю потоков и расскажет, зачем был создан GIL. Будут рассмотрены практические вопросы многопоточности в Python и способы работы с GIL.\nСлайды выступления: http://www.moscowpython.ru/meetup/14/gil-and-python-why/'}},
       'statistics':
           {'viewCount': '54836',
            'likeCount': '2332',
            'favoriteCount': '0',
            'commentCount': '54'}}],
 'pageInfo': {'totalResults': 1, 'resultsPerPage': 1}}

