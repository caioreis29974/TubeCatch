from customtkinter import *
from pytubefix import YouTube
from pytubefix.cli import on_progress

def start_download():
    url = url_entry.get()
    if url:
        try:
            yt = YouTube(url, on_progress_callback= on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path="saves")
            status_label.configure(text="Download Completed!", text_color="#000080")
        except Exception as e:
            status_label.configure(text=f"Erro: {str(e)}", text_color="#B22222")
    else:
        status_label.configure(text="Please enter a valid URL!", text_color="#fff")

app = CTk()
app.geometry("800x600")
app.title("TubeCatch")
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
