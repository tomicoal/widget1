import customtkinter as ctk

# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry("600x400")

# button
button_x = 0.5
button = ctk.CTkButton(window,text="toggle sidebar")
button.place(relx=button_x, rely=0.5, anchor="center")

# run
window.mainloop()
