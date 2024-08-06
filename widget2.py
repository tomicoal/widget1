import customtkinter as ctk



def button_callback():
    label_string.set("New")
    ctk.set_appearance_mode("light")


# window
window = ctk.CTk()
window.title("customTKinter app")
window.geometry("600x400")


# widgets
label_string = ctk.StringVar()
label_string.set('A CTK Label')
label = ctk.CTkLabel(window,
                     textvariable=label_string,
                     fg_color=("red", "navy"),
                     text_color="white",
                     corner_radius=8
                     )
label.pack()

button = ctk.CTkButton(window,
                       text="my button",
                       fg_color="navy",
                       hover_color="red",
                       command=button_callback)

button.pack(padx=20, pady=20)


frame = ctk.CTkFrame(window, fg_color="transparent")
frame.pack()
slider = ctk.CTkSlider(frame)
slider.pack()


def switch_event():
    print("switch toggled, current value:", switch_var.get())


switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(window, text="Exercise Switch", command=switch_event,
                       variable=switch_var, onvalue="on", offvalue="off", fg_color="red",
                       progress_color="pink", button_color="green", button_hover_color="yellow",
                       switch_height=40, corner_radius=1)
switch.pack()


# run
window.mainloop()
