from pytube import YouTube

#ask for the link from user
link = input("link:  ")
yt = YouTube(link)

#Showing details
print("title: ",yt.title)
print("views: ",yt.views)
print("lenght: ",yt.length)
print("rating: ",yt.rating)

va = input('Audio "a" or Video "v":  ')
if va == "v":
    #Getting the highest resolution possible   
    ys = yt.streams.get_highest_resolution()
if va == "a":
    ys = yt.streams.filter(only_audio=True).all()[0]
#Starting download
print("Downloading...")
ys.download()
print("Download completed!") 
