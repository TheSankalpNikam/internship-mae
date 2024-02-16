from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

root = Tk()
root.title("Speed Converter")
root.geometry("600x500+450+100")
f1 = ("Calibri", 15)
f2 = ("Arial", 20, "bold")

pattern = r'[a-zA-z ]'

def convert():
	try:
		# Data Validation
		speed = ent_speed.get()
		if not speed.strip():
			raise ValueError("Speed cannot be blank.")
		if re.search(pattern, speed):
			raise ValueError("Speed cannot contain alphabets")

		km = float(speed)
		if km < 0:
			raise ValueError("Speed cannot be negative.")
		
		selected_unit = unit_dropdown.get()
		if selected_unit == 'kmph':
			mach = round(km * 0.000816, 5)
			ftps = round(km * 0.91, 2)
			mph = round(km * 0.62, 2)
			kn = round(km * 0.54, 2)
			mps = round(km * 0.28, 2)
			turtles = round(km * 3.11, 2)
			msg = str(km) + " kmph is " + str(mach) + " Mach\n About equal to:\n" + str(ftps) + " ft/s  " + str(mph) + " mph  " + str(kn) + " kn  " + str(mps) + " m/s  " + str(turtles) + " turtles"
		elif selected_unit == 'Mach':
			kmph = round(km / 0.000816, 2)
			ftps = round(km / 0.91, 2)
			mph = round(km / 0.62, 2)
			kn = round(km / 0.54, 2)
			mps = round(km / 0.28, 2)
			jets = round(km * 1.38, 2)
			msg = str(km) + " Mach is " + str(kmph) + " kmph\n About equal to:\n" + str(ftps) + " ft/s  " + str(mph) + " mph  " + str(kn) + " kn  " + str(mps) + " m/s  " + str(jets) + " jets"
		else:
			raise ValueError("Invalid unit selected.")
	 
		lab_convert.configure(text = msg)	
		
	except ValueError as e:
		messagebox.showerror("Error", str(e))
		lab_convert.configure(text = "")
		return

lab_header = Label(root, text = "Speed Converter", font = f2)
lab_header.place(x = 200, y = 50)

lab_speed = Label(root, text = "Enter Speed: ", font = f1)
lab_speed.place(x = 50, y = 125)

ent_speed = Entry(root, font = f1)
ent_speed.place(x = 200, y = 125)

unit_dropdown = ttk.Combobox(root, values=['kmph', 'Mach'], font=f1, width = 5)
unit_dropdown.current(0)
unit_dropdown.place(x=400, y=125)

btn_convert = Button(root, text = "Convert", font = f1, command = convert)
btn_convert.place(x = 250, y = 175)

lab_convert = Label(root, text = "", font = f1)
lab_convert.place(x = 100, y = 250) 

root.mainloop()
