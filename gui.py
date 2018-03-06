from tkinter import*
import logic
from tkinter import filedialog

root=Tk()
root.withdraw()

inf=filedialog.askopenfilename(initialdir = "/",title = "Vali fail",filetypes = (("ARGO failid","*.atab"),("kõik failid","*.*")))
outf=filedialog.asksaveasfilename(initialdir = "/",title = "Vali asukoht",filetypes = (("csv fail","*.csv"),("kõik failid","*.*")))

if outf[-4:]!=".csv":
    outf=outf+".csv"

logic.extract(inf)
logic.output(outf)

root.destroy()
root.mainloop()
