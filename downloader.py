from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import requests
import shutil

dwnld = Tk()
dwnld.title("youtube downloader")
dwnld.geometry('600x400')
dwnld.configure(bg='white')


def download():
    df = dwnld_format.get()
    link = entry_lnk.get("1.0", END)
    if(df == "video"):
        download_video(link)
    elif(df == "thumbnail"):
        download_thumb(link)
    elif(df == "description"):
        download_desc(link)


def download_video(link):
    # pip install pytube3
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download('C:\\Users\\manoj\\Desktop\\folder')


def download_thumb(link):
    yt = YouTube(link)
    url = yt.thumbnail_url
    filename = url.split("/")[-1]
    r = requests.get(url, stream=True)
    r.raw.decode_content = True
    # Open a local file with wb ( write binary ) permission.
    with open("C:\\Users\\manoj\\Desktop\\folder\\{}".format(filename), 'wb') as f:
        shutil.copyfileobj(r.raw, f)


def download_desc(link):
    yt = YouTube(link)
    desc = yt.description
    title = yt.title.split(" ")
    f = open("C:\\Users\\manoj\\Desktop\\folder\\{}.txt".format(
        title[0]), "w+")
    for i in desc:
        f.write(i)
    f.close()


# Adding youtubelogo
path = "assets\\download.png"
img = ImageTk.PhotoImage(PIL.Image.open(path))
logo = Label(dwnld, image=img)
logo.grid(row=0, column=1, padx=(50, 50), pady=(20, 0))

# entry link
label0 = Label(dwnld, text="Paste the link here:", bg='white',
               font='Helvetica').grid(row=1, column=1)
entry_lnk = Text(dwnld, width=20, height=1)
entry_lnk.grid(row=2, column=1)

label1 = Label(dwnld, text="Choose what to downlod :", bg='white',
               font='Helvetica').grid(row=3, column=1)
# Adding combobox drop down list
dwnld_format = StringVar()
drop_dwn = ttk.Combobox(dwnld, width=27, height=40, textvariable=dwnld_format)
drop_dwn['values'] = ('video', 'thumbnail', 'description')
drop_dwn.grid(row=4, column=1, padx=(0, 0), pady=(10, 10))
drop_dwn.current(0)

# download button
dwnld_button = Button(dwnld, text="Download", font='Helvetica', bg='red',
                      fg='black', height=1, width=8, command=lambda: download()).grid(row=5, column=1)

dwnld.mainloop()
