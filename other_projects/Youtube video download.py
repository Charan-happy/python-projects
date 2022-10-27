#first pip install pytube
import pytube
link=input("enter youtube video URL")
yt=pytube.youtube(link)
yt.streams.first().download()
print('Download', link)
