from pytube import YouTube
link = input("Enter the link: ")
yt = YouTube(link)

#Title of video
print("Title: ",yt.title)

#Number of views of video
print("Number of views: ",yt.views)

#Length of video
print("Length: ",yt.length," seconds")

#Description of video
print("Description: ",yt.description)

#Rating
print("Ratings: ",yt.rating)

#printing all the available streams
print(yt.streams)

#filter out only-audio streams
print(yt.streams.filter(progressive=True))

#decided which stream to download
ys = yt.streams.get_highest_resolution()

#download

ys.download('location')
print("Download complete.")