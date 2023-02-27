import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr

# Create a function to change the color of the buttons when hovering over them
def on_enter(event):
    event.widget.config(bg="gray")

def on_leave(event):
    event.widget.config(bg="SystemButtonFace")

# Create a function to select an audio file
def select_file():
    global audio_path
    audio_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    file_label.config(text="File: " + audio_path)

# Create a function to extract the script from the audio file
def extract_script():
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    text = text.replace("\n", " ")
    output_text.delete("1.0", "end")
    output_text.insert("end", text)

# Initialize the GUI
root = tk.Tk()
root.title("Audio Script Extractor")

# Create a label to display the selected audio file
file_label = tk.Label(root, text="File: None")
file_label.pack(pady=10)

# Create a button to select the audio file
select_button = tk.Button(root, text="Select File", width=15, height=2, command=select_file)
select_button.pack(pady=10)
select_button.bind("<Enter>", on_enter)
select_button.bind("<Leave>", on_leave)

# Create a button to start the script extraction
extract_button = tk.Button(root, text="Extract Script", width=15, height=2, command=extract_script)
extract_button.pack(pady=10)
extract_button.bind("<Enter>", on_enter)
extract_button.bind("<Leave>", on_leave)

# Create a text box to display the extracted script
output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)

root.mainloop()
