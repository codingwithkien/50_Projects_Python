from pytube import YouTube
from colorama import init, Fore

def onComplete(stream, filepath):
    print("Download complete!!!")
    print(filepath)
def onProgress(stream, chunk, bytes_renaming):
    progressString = f'{round(100 - (bytes_renaming / stream.filesize * 100), 2)}%'
    print(progressString)


init()
linkInput = input("Enter YouTube Link: ")
videoObject = YouTube(linkInput, on_complete_callback = onComplete, on_progress_callback = onProgress)
print("*" * 30)
print(Fore.YELLOW + f"Title:  \033[39m {videoObject.title}")
print(Fore.YELLOW + f"Length: \033[39m {round(videoObject.length / 60,2)} minutes")
print(Fore.YELLOW + f"Views:  \033[39m {videoObject.views / 1000000} million")
print(Fore.YELLOW + f"Author: \033[39m {videoObject.author}")
print("*" * 30)

print("Download: Best (B) | Worst (W) | Audio (A) | Exit (E)")
downloadChoice = input("Choice: ")
match downloadChoice:
    case "B":
        videoObject.streams.get_highest_resolution().download(r"D:\LEARN PROGRAMMING\PYTHON\PROJECTS")
    case "W":
        videoObject.streams.get_lowest_resolution().download(r"D:\LEARN PROGRAMMING\PYTHON\PROJECTS")
    case "A":
        videoObject.streams.get_audio_only().download(r"D:\LEARN PROGRAMMING\PYTHON\PROJECTS")
