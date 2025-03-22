from customtkinter import *
from tkinter import PhotoImage
from pytubefix import YouTube
from pytubefix.cli import on_progress

def start_download():
    url = url_entry.get()
    if url:
        status_label.configure(text="Starting Download...", text_color="#000080")
        app.update()
        try:
            yt = YouTube(url, on_progress_callback= on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path="saves")
            status_label.configure(text="Download Completed!", text_color="#002080")
            show_confirmation()
        except Exception as e:
            status_label.configure(text=f"Erro: {str(e)}", text_color="#B22222")
    else:
        status_label.configure(text="Please enter a valid URL!", text_color="#fff")

def show_confirmation():
    confirmation_window = CTkToplevel()
    confirmation_window.geometry("300x150")
    confirmation_window.title("Download Completed")
    CTkLabel(master=confirmation_window, text="Video downloaded successfully!",font=("Arial Black", 14), text_color="#000080").pack(pady=30)
    CTkButton(master=confirmation_window, text="OK", fg_color="#00008B", hover_color="#000080", command=confirmation_window.destroy).pack()
    confirmation_window.grab_set()
    confirmation_window.transient(app)

app = CTk()
app.geometry("800x600")
app.title("TubeCatch")
app.iconbitmap("./assets/icon_main.ico")
set_appearance_mode("dark")

main_frame = CTkFrame(master=app, fg_color="#1C1C1C", corner_radius=12)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

CTkLabel(master=main_frame, text="TubeCatch", font=("Arial Black", 20), text_color= "#0000CD", ).pack(pady=10)

url_entry = CTkEntry(master=main_frame, width=600, placeholder_text="Enter video URL", border_color="#191970", border_width=2)
url_entry.pack(pady=10)

d_button = CTkButton(master=main_frame, text="Download", fg_color="#00008B", hover_color="#000080", command=start_download)
d_button.pack(pady=10)

status_label = CTkLabel(master=main_frame, text="", font=("Arial", 14))
status_label.pack(pady=10)

app.mainloop()
