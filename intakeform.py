import tkinter as tk

from tkinter import filedialog
import fpdf

window = tk.Tk()
window.title("Patient Intake Form")
window.geometry("800x600")


canvas = tk.Canvas(window)
canvas.pack(side = "left", fill = "both", expand = "True")
scrollable_frame = tk.Frame(canvas)

scrollbar = tk.Scrollbar(window, orient = "vertical", command = canvas.yview)
scrollbar.pack(side = "right", fill = "y")

canvas.configure(yscrollcommand = scrollbar.set)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion = canvas.bbox("all")
    )
)

canvas.create_window((0,0), window = scrollable_frame, anchor = "nw")

canvas.configure(yscrollcommand = scrollbar.set)

main_frame = scrollable_frame

title_label = tk.Label(main_frame, text = "Patient Information")
title_label.config(font = ("Arial", 15, "bold"))
title_label.pack(padx = 10, pady = 10)

content_frame = tk.Frame(main_frame)
content_frame.pack()

name = tk.Label(content_frame, text = "Patient Full Name:")
name.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
entry1 = tk.Entry(content_frame, width = 25)
entry1.grid(row = 0, column = 1, padx = 5, pady = 5)

gender = tk.Label(content_frame, text = "Gender:")
gender.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
entry2 = tk.Entry(content_frame, width = 25)
entry2.grid(row = 1, column = 1, padx = 5, pady = 5)

height = tk.Label(content_frame, text = "Height:")
height.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
entry3 = tk.Entry(content_frame, width = 25)
entry3.grid(row = 2, column = 1, padx = 5, pady = 5)

mother = tk.Label(content_frame, text = "Mother:")
mother.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
entry4 = tk.Entry(content_frame, width = 25)
entry4.grid(row = 3, column = 1, padx = 5, pady = 5)

address = tk.Label(content_frame, text = "Address:")
address.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
entry5 = tk.Entry(content_frame, width = 25)
entry5.grid(row = 4, column = 1, padx = 5, pady = 5)

state = tk.Label(content_frame, text = "State:")
state.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "w")
entry6 = tk.Entry(content_frame, width = 25)
entry6.grid(row = 5, column = 1, padx = 5, pady = 5)

phone = tk.Label(content_frame, text = "Phone:")
phone.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "w")
entry7 = tk.Entry(content_frame, width = 25)
entry7.grid(row = 6, column = 1, padx = 5, pady = 5)

dob = tk.Label(content_frame, text = "DOB:")
dob.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "w")
entry8 = tk.Entry(content_frame, width = 25)
entry8.grid(row = 0, column = 3)

age = tk.Label(content_frame, text = "Age:")
age.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "w")
entry9 = tk.Entry(content_frame, width = 25)
entry9.grid(row = 1, column = 3)

weight = tk.Label(content_frame, text = "Weight:")
weight.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
entry10 = tk.Entry(content_frame, width = 25)
entry10.grid(row = 2, column = 3)

father = tk.Label(content_frame, text = "Father:")
father.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "w")
entry11 = tk.Entry(content_frame, width = 25)
entry11.grid(row = 3, column = 3)

city = tk.Label(content_frame, text = "City:")
city.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "w")
entry12 = tk.Entry(content_frame, width = 25)
entry12.grid(row = 4, column = 3)

zip = tk.Label(content_frame, text = "Zip Code:")
zip.grid(row = 5, column = 2, padx = 5, pady = 5, sticky = "w")
entry13 = tk.Entry(content_frame, width = 25)
entry13.grid(row =5, column = 3)

email = tk.Label(content_frame, text = "Email:")
email.grid(row = 6, column = 2, padx = 5, pady = 5, sticky = "w")
entry14 = tk.Entry(content_frame, width = 25)
entry14.grid(row = 6, column = 3)

emergency_title = tk.Label(main_frame, text = "Emergency Contact Information")
emergency_title.config(font = ("Arial", 15, "bold"))
emergency_title.pack(padx = 10, pady = 10)

emergency_frame = tk.Frame(main_frame)
emergency_frame.pack()

contact = tk.Label(emergency_frame, text = "Emergency Contact Name:")
contact.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
entry15 = tk.Entry(emergency_frame, width = 25)
entry15.grid(row = 1, column = 1, padx = 5, pady = 5)


relationship = tk.Label(emergency_frame, text = "Relationship to Patient:")
relationship.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
entry16 = tk.Entry(emergency_frame, width = 25) 
entry16.grid(row = 2, column = 1, padx = 5, pady = 5)

phone = tk.Label(emergency_frame, text = "Phone:")
phone.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
entry17 = tk.Entry(emergency_frame, width = 25)
entry17.grid(row = 3, column = 1, padx = 5, pady = 5)

from PIL import Image, ImageTk

image_frame = tk.Frame(main_frame)
image_frame.pack()

image = Image.open("pain11.png")
image = ImageTk.PhotoImage(image)

image_label = tk.Label(image_frame, image = image)
image_label.pack()

scale_frame = tk.Frame(main_frame)
scale_frame.pack()

pain_title = tk.Label(scale_frame, text = "Please Mark Your Pain Level:")
pain_title.config(font = ("Arial", 15, "bold"))
pain_title.grid(row = 0, column = 1)

none_var = tk.IntVar()
low_var = tk.IntVar()
mid_var = tk.IntVar()
high_var = tk.IntVar()
extreme_var = tk.IntVar()

p1 = tk.Label(scale_frame, text = "0")
p1.grid(row = 1, column = 1)
p2 = tk.Checkbutton(scale_frame, variable = none_var)
p2.grid(row = 1, column = 0)

q1 = tk.Label(scale_frame, text = "1-3")
q1.grid(row = 2, column = 1)
q2 = tk.Checkbutton(scale_frame, variable = low_var)
q2.grid(row = 2, column = 0)

r1 = tk.Label(scale_frame, text = "4-6")
r1.grid(row = 3, column = 1)
r2 = tk.Checkbutton(scale_frame, variable = mid_var)
r2.grid(row = 3, column = 0)

s1 = tk.Label(scale_frame, text = "7-9")
s1.grid(row = 4, column = 1)
s2 = tk.Checkbutton(scale_frame, variable = high_var)
s2.grid(row = 4, column = 0)

t1 = tk.Label(scale_frame, text = "10")
t1.grid(row = 5, column = 1)
t2 = tk.Checkbutton(scale_frame, variable = extreme_var)
t2.grid(row = 5, column = 0)

allergies_title = tk.Label(main_frame, text = "Please Select if you have the Following Allergies:")
allergies_title.config(font = ("Arial", 15, "bold"))
allergies_title.pack(padx = 10, pady = 10)

allergies_frame = tk.Frame(main_frame)
allergies_frame.pack()

allergy_labels = [
    "Penicillin or other antibiotics",
    "Morphine, Demerol, or other narcotics",
    "Aspirin or other pain remedies",
    "Tetanus antitoxin or other serums",
    "Iodine, Methiolate, or other antiseptic",
    "Other drugs/medications",
    "Known food allergies",
    "Environmental allergies"
]

allergy_vars = {}  

row = 0  
for label_text in allergy_labels:
    var = tk.IntVar()
    allergy_vars[label_text] = var  

    cb = tk.Checkbutton(allergies_frame, variable=var)
    cb.grid(row=row, column=0, sticky="e")

    lbl = tk.Label(allergies_frame, text=label_text)
    lbl.grid(row=row, column=1, sticky="w")

    row += 1 

for allergy, var in allergy_vars.items():
    print(f"{allergy}: {'Yes' if var.get() else 'No'}")


conditions_title = tk.Label(main_frame, text = "Please Mark Any of the Following Medical Conditions You Have:")
conditions_title.config(font = ("Arial", 15, "bold"))
conditions_title.pack(padx = 10, pady = 10)

conditions_frame = tk.Frame(main_frame)
conditions_frame.pack()

conditions_list = [
    "Hemophilia/Bleeding", "Arthritis", "Acid Reflux/GERD", "HIV/AIDS",
    "Anemia/Sickle Cell", "Asthma", "Autoimmune Disorder", "Cancer",
    "Coldsore", "Diabetes", "Epilepsy", "Headache", "Glaucoma",
    "Cholesterol", "Joint Issues", "Kidney Issues", "Blood Pressure Issues",
    "Cardiovascular Disease", "Mental Health Disorders", "Neurological Issues",
    "Liver Problems", "Respiratory Disease", "Thyroid Issues", "Organ Transplant",
    "Pregnant", "Breast Feeding", "Ulcers", "Osteoporosis", "Celiac", "Other"
]

condition_vars = {}


row_num = 0


for condition in conditions_list:
    var = tk.IntVar()
    condition_vars[condition] = var
    cb = tk.Checkbutton(conditions_frame, text=condition, variable=var)
    cb.grid(row=row_num, column=0, sticky="w", padx=10, pady=2)
    row_num += 1  

for condition, var in condition_vars.items():
    print(f"{condition}: {'Yes' if var.get() else 'No'}")


def convert_to_pdf():
    dictionary ={
    "Patient Full Name":entry1.get(),
    "Gender": entry2.get(),
    "Height": entry3.get(),
    "Mother": entry4.get(),
    "Address": entry5.get(),
    "State": entry6.get(),
    "Phone": entry7.get(),
    "DOB": entry8.get(),
    "Age": entry9.get(),
    "Weight": entry10.get(),
    "Father": entry11.get(),
    "City": entry12.get(),
    "Zip Code": entry13.get(),
    "Email": entry14.get(),
    "Emergency Contact Name": entry15.get(),
    "Relationship to Patient": entry16.get(),
    "Phone": entry17.get()
    }

    selected_allergies = []
    for allergy, var in allergy_vars.items():
        if var.get() == 1: 
            selected_allergies.append(allergy)


    selected_conditions = []
    for condition, var in condition_vars.items():
        if var.get() == 1:  
            selected_conditions.append(condition)

  
    dictionary["Selected Allergies"] = ", ".join(selected_allergies) if selected_allergies else "None"
    dictionary["Selected Medical Conditions"] = ", ".join(selected_conditions) if selected_conditions else "None"

    pdf = fpdf.FPDF() 
    pdf.add_page()
    pdf.set_font("Arial", size = 10)


    for key, value in dictionary.items():
         pdf.cell(200,10, f"{key}: {value}", ln=1)
    filepath = filedialog.asksaveasfilename(defaultextension= ".pdf")
    pdf.output(filepath)

    terminal_print()


def terminal_print():
    print("Selected Allergies:")
    for allergy, var in allergy_vars.items():
        if var.get():
            print(f"- {allergy}")

    print("\nSelected Medical Conditions:")
    for condition, var in condition_vars.items():
        if var.get():
            print(f"- {condition}")
        


button_frame = tk.Frame(main_frame)
button_frame.pack()

submit_button = tk.Button(button_frame, text = "Submit", command = convert_to_pdf)
submit_button.grid(row = 0, column = 0)



window.mainloop()

