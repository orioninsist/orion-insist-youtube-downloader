from pytube import YouTube
YouTube('').streams.first().download()
yt = YouTube('')
yt.streams