import requests
import ctypes
import os


def getImage(url):
    response = requests.get(url)
    name = response.url.split("/")[4]  # This splits the response url and then extracts the image id to be used as file name

    open(f"files/{name}.jpg", "wb").write(
        response.content
    )  # writes the fetched file to the directory in the fstring
    filepath = os.path.abspath(f"files/{name}.jpg")
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, filepath, 0
    )  # used to set the fetched image as wallpaper


if __name__ == "__main__":
    theurl = "https://picsum.photos/1920/1080"  # replace the values with the resolution of the display
    isdir = os.path.exists("files")

    # checks if the directory exists and created one if it doesnt
    if not isdir:
        os.mkdir("files")
    getImage(theurl)
