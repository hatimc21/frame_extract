from tkinter import messagebox
import cv2
import tkinter as tk
from tkinter import filedialog, ttk

class VideoDeframerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Deframer")

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#78909c')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.label_header = ttk.Label(self.frame, text="Video Deframer", style='Header.TLabel')
        self.label_header.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.label_input = ttk.Label(self.frame, text="Select Video File:")
        self.label_input.grid(row=1, column=0, pady=(0, 5), sticky='W')

        self.btn_browse_input = ttk.Button(self.frame, text="Browse", command=self.browse_input)
        self.btn_browse_input.grid(row=1, column=1, pady=(0, 5), padx=(0, 10), sticky='W')

        self.label_selected_video = ttk.Label(self.frame, text="")
        self.label_selected_video.grid(row=1, column=2, pady=(0, 5), sticky='W')

        self.label_output = ttk.Label(self.frame, text="Select Output Folder:")
        self.label_output.grid(row=2, column=0, pady=(0, 5), sticky='W')

        self.btn_browse_output = ttk.Button(self.frame, text="Browse", command=self.browse_output)
        self.btn_browse_output.grid(row=2, column=1, pady=(0, 5), padx=(0, 10), sticky='W')

        self.label_selected_output = ttk.Label(self.frame, text="")
        self.label_selected_output.grid(row=2, column=2, pady=(0, 5), sticky='W')

        self.btn_deframe = ttk.Button(self.frame, text="Deframe", command=self.deframe_video)
        self.btn_deframe.grid(row=3, column=0, columnspan=3, pady=(10, 0))

    def browse_input(self):
        file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi")])
        if file_path:
            self.video_path = file_path
            self.label_selected_video.config(text=f"Selected Video: {file_path}")

    def browse_output(self):
        folder_path = filedialog.askdirectory(title="Select Output Folder")
        if folder_path:
            self.output_folder = folder_path
            self.label_selected_output.config(text=f"Selected Output Folder: {folder_path}")

    def deframe_video(self):
        if hasattr(self, 'video_path') and hasattr(self, 'output_folder'):
            video = cv2.VideoCapture(self.video_path)
            frame_count = 0

            while True:
                ret, frame = video.read()

                if not ret:
                    break

                frame_count += 1
                cv2.imwrite(f'{self.output_folder}/frame{frame_count}.jpg', frame)

            video.release()

            # Display a message box after deframing is completed
            messagebox.showinfo("Video Deframer", "Video Deframing Completed.")
        else:
            messagebox.showwarning("Video Deframer", "Please select both the video file and output folder.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDeframerGUI(root)
    root.mainloop()
