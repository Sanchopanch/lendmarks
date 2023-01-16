import pytube
yt = pytube.YouTube('https://www.youtube.com/watch?v=SfZpoVp4op4')
stream=yt.streams
print(stream)
video = stream.filter(res='1080p').desc().first()
stream = yt.streams.get_by_itag(22)
video.download()