from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.title("Tip Calculator")
root.geometry("300x200")
f1 = ("Calibri", 15)
f2 = ("Arial", 15, "bold")

pattern = r'[a-zA-Z ]'
pattern2 = r'[a-zA-Z. ]'

def convert():
	

        # Data validation
	try:
		bill_amount = ent_bill_amount.get()
		if not bill_amount.strip():
			raise ValueError("Bill Amount cannot be blank.")
		if re.search(pattern, bill_amount):
			raise ValueError("Bill Amount should only contain numbers")		
		tip_percentage = ent_tip_percentage.get()
		if not tip_percentage.strip():
			raise ValueError("Tip cannot be blank.")
		if re.search(pattern, tip_percentage):
			raise ValueError("Tip should only contain numbers")

		num_people = ent_num_people.get()
		if not num_people.strip():
			raise ValueError("No. of people cannot be blank.")
		if re.search(pattern2, num_people):
			raise ValueError("No. of people should only contain natural numbers.")

		bill_amount = float(bill_amount)
		tip_percentage = float(tip_percentage)
		num_people = int(num_people)

		if bill_amount <= 0:
			raise ValueError("Bill Amount must be positive.")
		if tip_percentage < 0 or tip_percentage > 100:
			raise ValueError("Tip Percentage must be between 0 and 100.")
		if num_people <= 0:
			raise ValueError("Number of People must be positive.")
	except ValueError as e:
		messagebox.showerror("Error", str(e))
		return

        # Calculate tip per person
	total_tip = bill_amount * (tip_percentage / 100)
	total_bill = bill_amount + total_tip
	tip_per_person = total_tip / num_people
	total_bill_per_person = total_bill / num_people

	messagebox.showinfo("Tip Calculation", f"Total Tip: ${total_tip:.2f}\nTotal Bill: ${total_bill:.2f}\nTip per Person: ${tip_per_person:.2f}\nTotal Bill per Person: ${total_bill_per_person:.2f}")

	# Reset fields
	ent_bill_amount.delete(0, END)
	ent_tip_percentage.delete(0, END)
	ent_num_people.delete(0, END)

lab_header = Label(root, text = "Tip Calculator", font = f2)
lab_header.pack()

lab_bill_amount = Label(root, text="Bill Amount:")
lab_bill_amount.pack()
ent_bill_amount = Entry(root)
ent_bill_amount.pack()

lab_tip_percentage = Label(root, text="Tip Percentage:")
lab_tip_percentage.pack()
ent_tip_percentage = Entry(root)
ent_tip_percentage.pack()

lab_num_people = Label(root, text="Number of People:")
lab_num_people.pack()
ent_num_people = Entry(root)
ent_num_people.pack()

btn_convert = Button(root, text = "Calculate", font = f1, command = convert)
btn_convert.pack()

root.mainloop()
