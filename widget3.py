import customtkinter as ctk
from random import  choice


# functions
def move_btn():
    global button_x
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, relheight=button_x, anchor="center")

    # configure
    colors = ["red", "navy", "orange", "yellow"]
    button.configure(fg_color=choice(colors))


# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry("600x400")

# button
button_x = 0.5
button = ctk.CTkButton(window, text="toggle sidebar", command=move_btn, fg_color="blue")
button.place(relx=button_x, rely=0.5, relheight=button_x, anchor="center")

# run
window.mainloop()
