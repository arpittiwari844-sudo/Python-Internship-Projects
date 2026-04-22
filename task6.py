from pytube import YouTube

try:
    url = input("Enter YouTube Video URL: ")
    path = input("Enter download folder path: ")

    yt = YouTube(url)

    print("Downloading... Please wait ⏳")

    stream = yt.streams.get_highest_resolution()
    stream.download(path)

    print("Video downloaded successfully ✅")

except Exception as e:
    print("Error occurred ❌")
    print(e)