import customtkinter as ctk
from PIL import Image


class App():

    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('500x550')
        self.master.resizable(False, False)
        self.master.wm_title('AliaBot - by Michatec')
        self.master.iconbitmap("logoAlia.ico")
        self.master.config(background='white')
        self.master.attributes("-transparentcolor", "grey")
        
        App.firstPage(self.master)

    @staticmethod
    def firstPage(self):
        frame = ctk.CTkFrame(self.master,
                             width=500,
                             height=550,
                             corner_radius=20,
                             fg_color=("#E63946"),
                             bg_color="grey")
        frame.pack()

        img = ctk.CTkImage(light_image=Image.open("image.png"),
                           size=(120, 90))
        label_img = ctk.CTkLabel(master=self.master,
                                 image=img,
                                 text=None)
        label_img.place(x=180, y=15)

        self.email_field = ctk.CTkEntry(master=frame,
                                        width=340,
                                        placeholder_text=(
                                         "Email de acesso ao painel Alia"),
                                        font=("Arial", 14),
                                        corner_radius=10
                                        ).place(x=75, y=120)
        self.email_label = ctk.CTkLabel(master=frame,
                                        text="*campo obrigatório",
                                        text_color="white",
                                        font=("Arial", 12),
                                        ).place(x=75, y=148)

        self.password_field = ctk.CTkEntry(master=frame,
                                           show="*",
                                           width=340,
                                           placeholder_text=(
                                            "Senha de accesso ao painel Alia"),
                                           font=("Arial", 14),
                                           corner_radius=10
                                           ).place(x=75, y=180,)
        self.password_label = ctk.CTkLabel(master=frame,
                                           text="*campo obrigatório",
                                           text_color="white",
                                           font=("Arial", 12),
                                           ).place(x=75, y=208)

        self.button = ctk.CTkButton(master=frame,
                                    width=120,
                                    height=32,
                                    border_width=2,
                                    border_color="light grey",
                                    corner_radius=8,
                                    text="INICIAR CADASTRO",
                                    font=("Arial", 16, 'bold'),
                                    fg_color="white",
                                    text_color="#E63946").place(x=165, y=470)


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.eval('tk::PlaceWindow . center')
    app.mainloop()
