from pytube import YouTube

#ask for the link from user
link = input("Der Link vom Video, dass du downloaden möchtest:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Clicks: ",yt.views)
print("Länge des Videos: ",yt.length)
print("Bewertung des Videos: ",yt.rating)

va = input('Audio "a" oder Video "v" Donwloaden:  ')
if va == "v":
    #Getting the highest resolution possible   
    ys = yt.streams.get_highest_resolution()
if va == "a":
    ys = yt.streams.filter(only_audio=True).all()[0]
#Starting download
print("Downloading...")
ys.download()
print("Download completed!") 