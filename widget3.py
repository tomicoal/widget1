import customtkinter as ctk
# from random import  choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general attributes
        self.start_pos = start_pos
        self.end_pos = end_pos - 0.02
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)
        print(self.pos)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            print(self.pos)
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            print(self.pos)
            self.in_start_pos = True



# functions

# when click moves button to the right side of the window
# def move_btn():
#     global button_x
#     button_x += 0.005
#     button.place(relx=button_x, rely=0.5, anchor="center")
#     if button_x < 0.9:
#         window.after(1, move_btn)

    # # configure
    # colors = ["red", "navy", "orange", "yellow"]
    # button.configure(fg_color=choice(colors))


# def infinite_print():
#     print("infinite")
#     global button_x
#     if button_x < 10:
#         button_x += 3
#         window.after(10, infinite_print)



# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry("600x400")
# ctk.set_appearance_mode("light")


# animated panel
animated_panel = SlidePanel(window, 1, 0.7)
ctk.CTkLabel(animated_panel, text="Label 1").pack(expand=True, fill="both", padx=2, pady=10)
ctk.CTkLabel(animated_panel, text="Label 2").pack(expand=True, fill="both", padx=2, pady=10)
ctk.CTkLabel(animated_panel, text="Label 3").pack(expand=True, fill="both", padx=2, pady=10)
ctk.CTkTextbox(animated_panel, fg_color=("#dbdbdb","#2b2b2b")).pack(expand=True, fill="both", pady=10)

# button
button_x = 0.5
button = ctk.CTkButton(window, text="toggle sidebar", command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, anchor="center")

# run
window.mainloop()
