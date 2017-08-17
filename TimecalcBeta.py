import re
#Imports tkinter to create a GUI
from tkinter import *
from tkinter import ttk


def split_hours_and_minutes(time):
    #Splits the user input into hours and minutes, then returns a tuple
    try:
        if re.search(r'^\d\d[.:]\d\d$|^\d{4}$', time):
            hours_minutes = (time[0:2], time[len(time) - 2:len(time)])
            return hours_minutes
        elif re.search(r'^\d[.:]\d\d$|^\d{3}$', time):
            hours_minutes = (int(time[0:1]), int(time[-2] + time[-1]))
            return hours_minutes
    except ValueError:
        pass

def calculate(*args):
    #This calculates the time difference and sets time_worked accordingly
    try:
        in_time = split_hours_and_minutes(intid.get())
        out_time = split_hours_and_minutes(uttid.get())
        if rast.get() == "":
            _break_ = 0
        else:
            _break_ = int(rast.get())
        
        hours = ""
        minutes = "" #1240 - 13:45
        if int(in_time[1]) > int(out_time[1]):
            hours = int(out_time[0]) - int(in_time[0]) - 1
            difference =  int(in_time[1]) - int(out_time[1])
            minutes =  60 - difference
        else:
            hours = int(out_time[0]) - int(in_time[0])
            minutes = int(out_time[1]) - int(in_time[1])
        if _break_ > minutes:
            hours -= 1
            difference = minutes - _break_
            minutes = 60 + difference
        else:
            minutes = minutes - _break_


        
        total = str(hours) + " timmar och \n" + str(minutes) + " minuter."
        time_worked.set(total)

    except ValueError:
            pass


#GUI code starts here
root = Tk()
root.title("Tidräknare")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#These creates a boxes for in time, out time and break
ttk.Label(mainframe, text="Intid:").grid(column=1, row=1, sticky=(W))
intid = StringVar()
intid_entry = ttk.Entry(mainframe, width=7, textvariable=intid)
intid_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Uttid:").grid(column=1, row=3, sticky=(W))
uttid = StringVar()
uttid_entry = ttk.Entry(mainframe, width=7, textvariable=uttid)
uttid_entry.grid(column=1, row=4, sticky=(W, E))

ttk.Label(mainframe, text="Rast(i minuter):").grid(column=1, row=5, sticky=(W))
rast = StringVar()
rast_entry = ttk.Entry(mainframe, width=7, textvariable=rast)
rast_entry.grid(column=1, row=6, sticky=(W, E))

time_worked = StringVar()

ttk.Button(mainframe, text="Beräkna", command=calculate).grid(column=2, row=6, sticky=(S, W))

#A text saying "time worked" and an output widget
ttk.Label(mainframe, text="Arbetstid:").grid(column=2, row=1, sticky=W)

ttk.Label(mainframe, textvariable=time_worked).grid(column=2, row=2, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=20, pady=1)
    

root.bind('<Return>', calculate)
root.mainloop()
