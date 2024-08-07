import customtkinter as ctk
from random import  choice




# functions

# when click moves button to the right side of the window
def move_btn():
    global button_x
    button_x += 0.005
    button.place(relx=button_x, rely=0.5, anchor="center")
    if button_x < 0.9:
        window.after(1, move_btn)

    # # configure
    # colors = ["red", "navy", "orange", "yellow"]
    # button.configure(fg_color=choice(colors))


def infinite_print():
    print("infinite")
    global button_x
    if button_x < 10:
        button_x += 3
        window.after(10, infinite_print)



# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry("600x400")

# button
button_x = 0.5
button = ctk.CTkButton(window, text="toggle sidebar", command=move_btn, fg_color="blue")
button.place(relx=button_x, rely=0.5, anchor="center")

# run
window.mainloop()
