import customtkinter as ctk
from PIL import Image
from cadastra_produto import Cadastro


class App():

    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('500x500')
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
                             height=500,
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
                                        corner_radius=10)
        self.email_field.place(x=75, y=140)
        self.email_label = ctk.CTkLabel(master=frame,
                                        text="*campo obrigatório",
                                        text_color="white",
                                        font=("Arial", 12),
                                        ).place(x=75, y=168)

        self.password_field = ctk.CTkEntry(master=frame,
                                           show="*",
                                           width=340,
                                           placeholder_text=(
                                            "Senha de accesso ao painel Alia"),
                                           font=("Arial", 14),
                                           corner_radius=10
                                           )
        self.password_field.place(x=75, y=200,)
        self.password_label = ctk.CTkLabel(master=frame,
                                           text="*campo obrigatório",
                                           text_color="white",
                                           font=("Arial", 12)
                                           ).place(x=75, y=228)

        self.filename_field = ctk.CTkEntry(master=frame,
                                           width=340,
                                           placeholder_text=(
                                            "Informe a planilha com os dados"),
                                           font=("Arial", 14),
                                           corner_radius=10
                                           )
        self.filename_field.place(x=75, y=260)
        self.filename_label = ctk.CTkLabel(master=frame,
                                           text=(
                                            '*Ex: "planilha.xlsx"(sem aspas)'),
                                           text_color="white",
                                           font=("Arial", 12),
                                           ).place(x=75, y=288)

        self.button = ctk.CTkButton(master=frame,
                                    width=120,
                                    height=32,
                                    border_width=2,
                                    border_color="light grey",
                                    corner_radius=8,
                                    text="INICIAR CADASTRO",
                                    font=("Arial", 16, 'bold'),
                                    fg_color="white",
                                    text_color="#E63946",
                                    command=(lambda: Cadastro.CadastraProdutos(
                                        self.email_field.get(),
                                        self.password_field.get(),
                                        self.filename_field.get()))
                                    ).place(x=165, y=390)


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.eval('tk::PlaceWindow . center')
    app.mainloop()
