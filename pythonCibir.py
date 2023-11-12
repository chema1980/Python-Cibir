from tkinter import *
from cryptography.fernet import Fernet

class CifradorDescifrador:
    def __init__(self, master):
        self.master = master
        master.title("Cifrador y Descifrador")

        self.label = Label(master, text="Texto:")
        self.label.pack()

        self.texto_entry = Entry(master)
        self.texto_entry.pack()

        self.label2 = Label(master, text="Contraseña:")
        self.label2.pack()

        self.contrasena_entry = Entry(master, show="*")
        self.contrasena_entry.pack()

        self.cifrar_button = Button(master, text="Cifrar", command=self.cifrar)
        self.cifrar_button.pack()

        self.descifrar_button = Button(master, text="Descifrar", command=self.descifrar)
        self.descifrar_button.pack()

    def cifrar(self):
        texto = self.texto_entry.get().encode()
        contraseña = self.contrasena_entry.get().encode()

        cipher_suite = Fernet(contraseña)
        cifrado = cipher_suite.encrypt(texto)

        print("Texto cifrado:", cifrado)

    def descifrar(self):
        texto_cifrado = self.texto_entry.get().encode()
        contraseña = self.contrasena_entry.get().encode()

        cipher_suite = Fernet(contraseña)
        descifrado = cipher_suite.decrypt(texto_cifrado)

        print("Texto descifrado:", descifrado.decode())

def main():
    root = Tk()
    app = CifradorDescifrador(root)
    root.mainloop()

if __name__ == "__main__":
    main()