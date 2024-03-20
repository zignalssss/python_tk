import tkinter as tk
window = tk.Tk()
main_frame = tk.Frame(window)
main_frame.pack(expand=True, pady=20)


lbl_name = tk.Label(main_frame,text="°F(fahrenheit)")
ent_name = tk.Entry(main_frame,text="text",fg="black",width=10)

Ans = tk.Label(main_frame,text="100°C")

ent_name.pack(side=tk.LEFT)
lbl_name.pack(side=tk.LEFT)

Ans.pack(side=tk.LEFT)


window.mainloop()