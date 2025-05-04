import tkinter as tk

class SymptomCategory:
    def __init__(self, parent, title, symptoms, bg=None):
        self.vars = {}
        self.frame = tk.Frame(parent, bg=bg)
        self.title = tk.Label(parent, text=title, font=("Arial", 15, "bold"), bg=bg)
        self.title.pack(padx=10, pady=10, anchor='w')
        self.frame.pack(padx=5, pady=5, anchor='w')

        row = 0
        for symptom in symptoms:
            var = tk.IntVar()  
            self.vars[symptom] = var
            cb = tk.Checkbutton(self.frame, variable=var, bg=bg)
            cb.grid(row=row, column=0, sticky="e")
            lbl = tk.Label(self.frame, text=symptom, bg=bg)
            lbl.grid(row=row, column=1, sticky="w")
            row += 1

    def get_results(self):
        return {symptom: "Yes" if var.get() else "No" for symptom, var in self.vars.items()}


def ask_new_patient():
    prompt_label.config(text="Have you filled out the patient intake form?:")
    submit_button.config(state="normal")


def submit_response():
    response = new_patient_entry.get() 
    if response == "yes": 
        new_patient_entry.delete(0, tk.END)
        show_symptom_form()
    elif response == "no": 
        print("Please fill out the patient intake form before filling out the symptoms form.")
        window.quit() 
    else:  
        prompt_label.config(text="Please enter 'yes' or 'no'.")  


def show_symptom_form():
    global main_frame, categories  
    categories = []  


    main_frame = tk.Frame(window)
    main_frame.pack(fill="both", expand=1)

    canvas = tk.Canvas(main_frame)
    canvas.pack(side="left", fill="both", expand=1)

    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    form_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=form_frame, anchor="nw")

    title = tk.Label(form_frame, text="Please Mark Any of the Following Symptoms you Have:")
    title.config(font=("Arial", 15, "bold"))
    title.pack(padx=10, pady=10, anchor="w")

    category_definitions = [
        ("Constitutional Symptoms", [
            "Good general health lately", "Recent weight change", "Fever", "Fatigue", "Headache"
        ]),
        ("Eyes", [
            "Eye disease or injury", "Wear glasses/contact lenses", "Blurred or double vision"
        ]),
        ("Ears/Nose/Mouth/Throat", [
            "Hearing loss or ringing", "Earaches or drainage", "Nosebleeds/Sinus Problems/Rhinitis",
            "Mouth Sores", "Bleeding Gums", "Bad breathe or bad taste",
            "Sore throat or voice change", "Swollen glands in neck"
        ]),
        ("Cardiovascular", [
            "Heart Trouble", "Chest pain or Angina Pectoris", "Palpitations",
            "Shortness of breath while walking or lying flat", "Swelling of feet, ankles, or hands"
        ]),
        ("Respiratory", [
            "Chronic or frequent coughs", "Spitting up blood", "Shortness of Breath", "Wheezing"
        ]),
        ("Gastrointestinal", [
            "Loss of Appetite", "Change in Bowel Movements", "Nausea or Vomiting", "Frequent Diarrhea",
            "Painful bowel movements or constipation", "Rectal bleeding or blood in stool", "Abdominal Pain"
        ]),
        ("Musculoskeletal", [
            "Joint Pain", "Joint Stiffness or Swelling", "Weakness of muscles or joints",
            "Muscle pain or cramps", "Back Pain", "Cold Extremities", "Difficulty Walking"
        ]),
        ("Integumentary", [
            "Rash or Itching", "Change in skin color", "Change in hair or nails", "Varicose Veins"
        ]),
        ("Neurological", [
            "Frequent or Reoccuring Headache", "Lightheaded or dizzy", "Convulsions or Seizures",
            "Numbness or Tingling Sensations", "Paralysis", "Tremors", "Headache"
        ]),
        ("Psychiatric", [
            "Memory loss or confusion", "Nervousness", "Depression", "Insomnia"
        ]),
        ("Endocrine", [
            "Glandular or hormone problem", "Excessive thirst or urination", "Heat or cold intolerance",
            "Skin becoming drier", "Change in hat or glove size"
        ]),
        ("Hematologic/Lymphatic", [
            "Slow to heal after cuts", "Bleeding or bruising tendency", "Anemia", "Phlebitis",
            "Past transfusion", "Enlarged Glands"
        ])
    ]

    for item in category_definitions:
        title = item[0]
        symptoms = item[1]
        category = SymptomCategory(form_frame, title, symptoms)
        categories.append(category)

  
    submit_button = tk.Button(form_frame, text="Submit", command=submit, font=("Arial", 12, "bold"))
    submit_button.pack(pady=20)


def submit():
    print("\nPatient Symptom Report:")
    for category in categories:
        results = category.get_results()
        for symptom, answer in results.items():
            print(f"{symptom}: {answer}")



window = tk.Tk() 
window.title("Patient Intake Form")
window.geometry("850x600")


prompt_label = tk.Label(window, text="Have you filled out the patient intake form?", font=("Arial", 14))
prompt_label.pack(padx=10, pady=10)


new_patient_entry = tk.Entry(window, font=("Arial", 12))
new_patient_entry.pack(pady=10)


submit_button = tk.Button(window, text="Submit", command=submit_response, font=("Arial", 12, "bold"))
submit_button.pack(pady=20)

window.mainloop()


# Utilizes classes and if and else statements and prints report to terminal


