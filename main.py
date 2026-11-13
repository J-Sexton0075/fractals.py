import tkinter as tk
from plot import takeN
root = tk.Tk(
    className="Tk"
)

tk.Label(root, text="n-value").grid(row=0, column=0)
tk.Label(root, text="plot-size").grid(row=1, column=0)
tk.Label(root, text="iterations").grid(row=2, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

tk.Button(root, text="plot", command=lambda: takeN(entry1.get(), entry3.get(), entry2.get())).grid(row=3, column=0)


root.mainloop()