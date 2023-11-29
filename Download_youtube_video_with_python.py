from pytube import YouTube
video = 'https://www.youtube.com/watch?v=B7TPfEIhSDY&list=RDvxUjwGDxR3w&index=2'  # Rick Astley - Never Gonna Give You Up
yt = YouTube(video)
yt.streams.first().download()
print(f"Downloaded Video:{yt.title}")
