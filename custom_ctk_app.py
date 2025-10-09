import customtkinter as ctk
from tkinter import messagebox
import sys

# Set the appearance mode and color theme
ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"

class MagentaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Magenta Themed CustomTkinter App")
        self.geometry("900x700")
        
        # Configure grid layout (3 columns, multiple rows)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        for i in range(6):
            self.main_frame.grid_rowconfigure(i, weight=1)
        
        # Create header label
        self.header_label = ctk.CTkLabel(
            self.main_frame,
            text="MAGENTA DASHBOARD",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#FF00FF"  # Magenta color
        )
        self.header_label.grid(row=0, column=0, columnspan=3, pady=(20, 30))
        
        # Create buttons with magenta styling
        self.create_buttons()
        
        # Create a label to show button clicks
        self.status_label = ctk.CTkLabel(
            self.main_frame, 
            text="Click any button below", 
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#FF69B4"  # Hot pink
        )
        self.status_label.grid(row=5, column=0, columnspan=3, pady=20)
        
        # Create exit button
        self.exit_button = ctk.CTkButton(
            self.main_frame,
            text="EXIT APPLICATION",
            fg_color="#FF00FF",  # Magenta
            hover_color="#FF1493",  # Deep pink
            text_color="white",
            font=ctk.CTkFont(size=14, weight="bold"),
            corner_radius=10,
            height=40,
            command=self.quit_app
        )
        self.exit_button.grid(row=6, column=0, columnspan=3, pady=20, padx=40, sticky="ew")
        
    def create_buttons(self):
        # Define magenta color scheme
        magenta_colors = {
            "primary": "#FF00FF",      # Pure magenta
            "secondary": "#FF69B4",    # Hot pink
            "accent": "#DA70D6",       # Orchid
            "hover": "#FF1493",        # Deep pink
            "text": "#FFFFFF"          # White text
        }
        
        # Button configurations in a 3x4 grid
        buttons = [
            {"text": "Dashboard", "row": 1, "col": 0, "color": magenta_colors["primary"]},
            {"text": "Reports", "row": 1, "col": 1, "color": magenta_colors["secondary"]},
            {"text": "Settings", "row": 1, "col": 2, "color": magenta_colors["accent"]},
            {"text": "Users", "row": 2, "col": 0, "color": magenta_colors["primary"]},
            {"text": "Analytics", "row": 2, "col": 1, "color": magenta_colors["secondary"]},
            {"text": "Messages", "row": 2, "col": 2, "color": magenta_colors["accent"]},
            {"text": "Profile", "row": 3, "col": 0, "color": magenta_colors["primary"]},
            {"text": "Help", "row": 3, "col": 1, "color": magenta_colors["secondary"]},
            {"text": "Logout", "row": 3, "col": 2, "color": magenta_colors["accent"]},
            {"text": "Tools", "row": 4, "col": 0, "color": magenta_colors["primary"]},
            {"text": "Files", "row": 4, "col": 1, "color": magenta_colors["secondary"]},
            {"text": "Search", "row": 4, "col": 2, "color": magenta_colors["accent"]},
        ]
        
        # Create buttons with custom styling
        for btn_config in buttons:
            button = ctk.CTkButton(
                self.main_frame,
                text=btn_config["text"],
                fg_color=btn_config["color"],
                hover_color=magenta_colors["hover"],
                text_color=magenta_colors["text"],
                font=ctk.CTkFont(size=14, weight="bold"),
                corner_radius=10,
                height=50,
                command=lambda t=btn_config["text"]: self.button_callback(t)
            )
            button.grid(
                row=btn_config["row"], 
                column=btn_config["col"], 
                padx=15, 
                pady=10, 
                sticky="nsew"
            )
    
    def button_callback(self, button_text):
        self.status_label.configure(text=f"Clicked: {button_text}")
        # Show a message box with the button text
        messagebox.showinfo("Button Clicked", f"You clicked the {button_text} button!")
    
    def quit_app(self):
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = MagentaApp()
    app.mainloop()