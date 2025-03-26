from customtkinter import *
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress
import datetime
import os

def start_download():
    url = url_entry.get()
    if url:
        status_label.configure(text="Starting Download...", text_color="#000080")
        app.update()

        try:
            yt = YouTube(url, on_progress_callback=on_progress)

            if download_type.get() == "Audio":
                stream = yt.streams.filter(only_audio=True).first()
                file_extension = "mp3"
            else:
                stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
                file_extension = "mp4"

            if not stream:
                status_label.configure(text="Error: No stream available!", text_color="#B22222")
                return

            save_path = filedialog.askdirectory()
            if not save_path:
                status_label.configure(text="Download canceled!", text_color="#B22222")
                return

            output_file = stream.download(output_path=save_path)

            if file_extension == "mp3":
                base, _ = os.path.splitext(output_file)
                new_file = base + ".mp3"
                os.rename(output_file, new_file)
                output_file = new_file

            status_label.configure(text="Download Completed!", text_color="#002080")

            save_download_history(yt.title, output_file)

            show_confirmation()
        except Exception as e:
            status_label.configure(text=f"Error: {str(e)}", text_color="#B22222")
    else:
        status_label.configure(text="Please enter a URL!", text_color="#fff")

def save_download_history(title, file_path):
    with open("download_history.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {title} - {file_path}\n")

def show_confirmation():
    confirmation_window = CTkToplevel()
    confirmation_window.geometry("300x150")
    confirmation_window.title("Download Completed")
    CTkLabel(master=confirmation_window, text="Video downloaded successfully!", font=("Arial Black", 14), text_color="#000080").pack(pady=30)
    CTkButton(master=confirmation_window, text="OK", fg_color="#00008B", hover_color="#000080", command=confirmation_window.destroy).pack()
    confirmation_window.grab_set()
    confirmation_window.transient(app)

app = CTk()
app.geometry("800x600")
app.minsize(width=600, height=300)
app.title("TubeCatch")
app.iconbitmap("./assets/icon_main.ico")
set_appearance_mode("dark")

main_frame = CTkFrame(master=app, fg_color="#1C1C1C", corner_radius=12)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

CTkLabel(master=main_frame, text="TubeCatch", font=("Arial Black", 20), text_color="#0000CD").pack(pady=10)

input_frame = CTkFrame(master=main_frame, fg_color="transparent")
input_frame.pack(fill="x", padx=20, pady=10)

url_entry = CTkEntry(master=input_frame, width=400, placeholder_text="Enter video URL", border_color="#191970", border_width=2)
url_entry.pack(side="left", padx=(0, 10), fill="x", expand=True)

download_type = StringVar(value="Video")
type_combobox = CTkComboBox(master=input_frame, variable=download_type, values=["Video", "Audio"], width=150)
type_combobox.pack(side="left")

d_button = CTkButton(master=main_frame, text="Download", fg_color="#00008B", hover_color="#000080", command=start_download)
d_button.pack(pady=10)

status_label = CTkLabel(master=main_frame, text="", font=("Arial", 14))
status_label.pack(pady=10)

footer_label = CTkLabel(master=main_frame, text="© 2025 Developed by CaioXyZ", font=("Arial", 12), text_color="#808080")
footer_label.pack(side="bottom", pady=10)

app.mainloop()
