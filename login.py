import customtkinter as ctk

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    # You can validate username and password (example)
    if username == "admin" and password == "password123":
        label_status.config(text="Login successful", text_color="green")
    else:
        label_status.config(text="Invalid username or password", text_color="red")


# Create the main window
app = ctk.CTk()

# Set window size
app.geometry("375x667")  # Mobile screen size (portrait)
app.title("Stylish Login")

# Set the background color for the app window (light blue)
app.config(bg="#e0f7fa")

# Create a frame for the login form with rounded corners and transparent background (using solid white)
login_frame = ctk.CTkFrame(app, width=300, height=400, corner_radius=20, fg_color="white")  # White background instead of transparency
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a title label for the login page with a blue color scheme
label_title = ctk.CTkLabel(login_frame, text="Welcome Back!", font=("Arial", 24, "bold"), text_color="#0277bd")
label_title.pack(pady=(30, 20))

# Create username input field with a blue theme
label_username = ctk.CTkLabel(login_frame, text="Username", text_color="black")
label_username.pack(pady=(10, 5))
entry_username = ctk.CTkEntry(login_frame, placeholder_text="Enter your username", width=250, height=40, corner_radius=10, fg_color="#e1f5fe")
entry_username.pack(pady=(0, 20))

# Create password input field with a blue theme
label_password = ctk.CTkLabel(login_frame, text="Password", text_color="black")
label_password.pack(pady=(10, 5))
entry_password = ctk.CTkEntry(login_frame, placeholder_text="Enter your password", show="*", width=250, height=40, corner_radius=10, fg_color="#e1f5fe")
entry_password.pack(pady=(0, 30))

# Create a login button with rounded corners and a blue color
button_login = ctk.CTkButton(login_frame, text="Login", width=250, height=40, corner_radius=10, command=login, fg_color="#0288d1", hover_color="#0277bd")
button_login.pack(pady=(0, 20))

# Create a status label to show success or error message
label_status = ctk.CTkLabel(login_frame, text="", text_color="black")
label_status.pack()

# Run the application
app.mainloop()
