
    import os
    os.chdir('d:\\sushma')
    import tkinter as tk
    from tkinter import messagebox
    from pytube import YouTube as yt

    import tkinter as tk
    tab=tk.Tk()
    tab.title('youtube_downloder')
    tab.geometry('1016x1624')
    a=tk.StringVar()
    l1=tk.Label(tab,text="PLEASE ENTER THE URL LINK :",font=('Comic Sans MS',20,'italic',),bg='#63B3F4',)
    l1.place(x=100,y=100)
    e1=tk.Entry(tab,textvariable=a,font=('Harlow Solid Italic',20,'italic'),bg='#EF872B')
    e1.place(x=50,y=100)
    def yt_download():
        url=yt(a.get())
        data=url.streams.first()
        data.download()
        messagebox.showinfo("YouTube", "youtube video downloaded sucessfully")
    def error():
        url =yt(a.get())
        data=url.streams.first()
        data.download()
        messagebox.showinfo("YouTube", "youtube video downloaded sucessfully")
        if not url:
            messagebox.showinfo("Error", "Please enter a YouTube URL")
            return

    def cancel():
        a.set(' ')
    b1=tk.Button(tab,text='DOWNLOAD',font=('Comic Sans MS',24,'bold'),bg='#FBD83E',command=yt_download)
    b1.place(x=100,y=200)
    b2=tk.Button(tab,text='CANCEL',font=('Comic Sans MS',24,'bold'),bg='#B25AC1',command=cancel)
    b2.place(x=520,y=200)
    tab.mainloop()
