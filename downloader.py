import os
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import requests
import shutil
from ttkthemes import themed_tk as tk

dwnld = tk.ThemedTk()
dwnld.get_themes()
dwnld.set_theme('clam')
dwnld.title("pytube-dl")
dwnld.geometry('600x400')
dwnld.configure(bg='white')

directory = os.path.expanduser('~')+r'/Downloads/'

if not os.path.exists(directory): os.mkdir(directory)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 11), background='#32a852',foreground='white')
style.map('TButton', background=[('active', '#32a86d')])
style.configure('TLabel', font=('Helvetica', 11), background='white',foreground='black')
style.configure('TEntry', font=('Helvetica', 11), background='white',foreground='black')
style.configure('TLabel', font=('Helvetica', 11), background='white',foreground='black')


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
    ys.download(directory)


def download_thumb(link):
    yt = YouTube(link)
    url = yt.thumbnail_url
    filename = url.split("/")[-1]
    r = requests.get(url, stream=True)
    r.raw.decode_content = True
    # Open a local file with wb ( write binary ) permission.
    with open(directory.format(filename), 'wb') as f:
        shutil.copyfileobj(r.raw, f)


def download_desc(link):
    yt = YouTube(link)
    desc = yt.description
    title = yt.title.split(" ")
    f = open(directory.format(
        title[0]), "w+")
    for i in desc:
        f.write(i)
    f.close()


# Adding youtubelogo
path = "assets/download.png"
img = ImageTk.PhotoImage(PIL.Image.open(path))
logo = ttk.Label(dwnld, image=img)
logo.grid(row=0, column=1, padx=(50, 50), pady=(20, 0))

# entry link
label0 = ttk.Label(dwnld, text="Paste the link here:").grid(row=1, column=1)
entry_lnk = ttk.Entry(dwnld)
entry_lnk.grid(row=2, column=1)

label1 = ttk.Label(dwnld, text="Choose what to downlod :").grid(row=3, column=1)
# Adding combobox drop down list
dwnld_format = StringVar()
drop_dwn = ttk.Combobox(dwnld, width=27, height=40, textvariable=dwnld_format)
drop_dwn['values'] = ('video', 'thumbnail', 'description')
drop_dwn.grid(row=4, column=1, padx=(0, 0), pady=(10, 10))
drop_dwn.current(0)

# download button
dwnld_button = ttk.Button(dwnld, text="Download" ,command=lambda: download()).grid(row=5, column=1)

dwnld.mainloop()
