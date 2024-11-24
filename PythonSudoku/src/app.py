import tkinter as tk
import hud
import time

def abrir_aplicativo(tests=False):
    raiz = tk.Tk()
    hud.Interface(raiz)

    if tests:
        raiz.update_idletasks()
        time.sleep(2)
        raiz.destroy()
        return True

    raiz.mainloop()

if __name__ == '__main__':
    abrir_aplicativo()