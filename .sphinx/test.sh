cd 'C:\Users\jeanm\PycharmProjects\TikTokLive\.sphinx' || exit
sphinx-apidoc --ext-autodoc --force -o  . ../TikTokLive ../TikTokLive/proto/tiktok_schema_pb2.py
sh -c '.\\make html; exec sh'
