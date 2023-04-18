import urllib.request
import re
import urllib.parse

from urllib.parse import quote
search_keyword = input('Search For:')

print('Top Result For:' + search_keyword)



html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + quote(search_keyword))
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

print("https://www.youtube.com/watch?v=" + video_ids[0])
