import customtkinter as ctk
from scripts.convert_file import convert_file


def select_file(path:str):
    file_path = ctk.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        path.delete(0, ctk.END)
        path.insert(0, file_path)

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Conversion de archivos")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (350 // 2)
        y = (screen_height // 2) - (650 // 2)
        self.geometry(f"{800}x{200}+{x}+{y}")
        self.resizable(False, False)
        self.frame()
        self.frame_selection()

    def frame(self):
        self.frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=15,
            border_width=2,
            border_color="black"
        )
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.frame.grid_columnconfigure(1, weight=1)

    def frame_selection(self):
        py = (50, 10)
        label = ctk.CTkLabel(
            self.frame,
            text="Archivo:",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="black"
        )
        label.grid(row=1, column=0, padx=10, pady=py, sticky="w")

        path_var = ctk.StringVar()
        path_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text = 'Seleccione el archivos',
            width = 60,
            font=("Monotype", 10, "italic"),
            text_color = '#000000',
            textvariable = path_var
        )
        path_entry.grid(row=1, column=1, padx=10, pady=py, sticky="ew")

        boton_select = ctk.CTkButton(
            self.frame,
            text="Seleccionar",
            text_color="black",
            fg_color="transparent",
            hover_color="#FFFFFF",
            border_color="black",
            border_width=2,
            corner_radius=8,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=lambda: select_file(path_entry)
        )
        boton_select.grid(row=1, column=2, padx=10, pady=py)

        boton_execute = ctk.CTkButton(
            self.frame,
            text="Convertir",
            text_color="black",
            fg_color="transparent",
            hover_color="#FFFFFF",
            border_color="black",
            border_width=2,
            corner_radius=8,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=lambda: convert_file(path_var.get())
        )
        boton_execute.grid(row=2, column=1, padx=10, pady=10)



    


app = App()
app.mainloop()
