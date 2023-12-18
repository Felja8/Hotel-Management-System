import tkinter as tk

window = tk.Tk()
window.title("Junkie House")
window.geometry("1400x800")
window.resizable(False, False)


frame = tk.Frame(window)
frame.pack(expand=True, fill="both")
frame.pack_propagate(False)

button = tk.Button(frame, text="Fuck u!!")
button.pack(pady=350, padx=20)


window.mainloop()