import tkinter as tk

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
entry9 = tk.Entry(content_frame, width = 25)
entry9.grid(row = 2, column = 3)

father = tk.Label(content_frame, text = "Father:")
father.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "w")
entry8 = tk.Entry(content_frame, width = 25)
entry8.grid(row = 3, column = 3)

city = tk.Label(content_frame, text = "City:")
city.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "w")
entry9 = tk.Entry(content_frame, width = 25)
entry9.grid(row = 4, column = 3)

zip = tk.Label(content_frame, text = "Zip Code:")
zip.grid(row = 5, column = 2, padx = 5, pady = 5, sticky = "w")
entry10 = tk.Entry(content_frame, width = 25)
entry10.grid(row =5, column = 3)

email = tk.Label(content_frame, text = "Email:")
email.grid(row = 6, column = 2, padx = 5, pady = 5, sticky = "w")
entry11 = tk.Entry(content_frame, width = 25)
entry11.grid(row = 6, column = 3)

emergency_title = tk.Label(main_frame, text = "Emergency Contact Information")
emergency_title.config(font = ("Arial", 15, "bold"))
emergency_title.pack(padx = 10, pady = 10)

emergency_frame = tk.Frame(main_frame)
emergency_frame.pack()

contact = tk.Label(emergency_frame, text = "Emergency Contact Name:")
contact.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
entry12 = tk.Entry(emergency_frame, width = 25)
entry12.grid(row = 1, column = 1, padx = 5, pady = 5)

relationship = tk.Label(emergency_frame, text = "Relationship to Patient:")
relationship.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
entry13 = tk.Entry(emergency_frame, width = 25) 
entry13.grid(row = 2, column = 1, padx = 5, pady = 5)

phone = tk.Label(emergency_frame, text = "Phone:")
phone.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
entry14 = tk.Entry(emergency_frame, width = 25)
entry14.grid(row = 3, column = 1, padx = 5, pady = 5)

allergies_title = tk.Label(main_frame, text = "Please Select if you have the Following Allergies:")
allergies_title.config(font = ("Arial", 15, "bold"))
allergies_title.pack(padx = 10, pady = 10)

allergies_frame = tk.Frame(main_frame)
allergies_frame.pack()

acetaminophen_var = tk.IntVar()
Erythromycin_var = tk.IntVar()
Penicillin_var = tk.IntVar()
SulfaDrug_var = tk.IntVar()
Aspirin_var = tk.IntVar()
Ibuprofen_var = tk.IntVar()
Tetracycline_var = tk.IntVar()
Cephlasporins_var = tk.IntVar()
Chlorhexidine_var = tk.IntVar()
Codeine_var = tk.IntVar()
Latex_var = tk.IntVar()
NutsFruits_var = tk.IntVar() 

a = tk.Label(allergies_frame, text = "Penicillin or other antibiotics")
a.grid(row = 0, column = 0, sticky = "w")
a1 = tk.Checkbutton(allergies_frame, variable = acetaminophen_var)
a1.grid(row = 0, column = 1)

b = tk.Label(allergies_frame, text = "Morphine, Demerol, or other narcotics")
b.grid(row = 1, column = 0, sticky = "w")
b1 = tk.Checkbutton(allergies_frame, variable = Erythromycin_var)
b1.grid(row = 1, column = 1)

c = tk.Label(allergies_frame, text = "Aspirin or other pain remedies")
c.grid(row = 2, column = 0, sticky = "w")
c1 = tk.Checkbutton(allergies_frame, variable = Penicillin_var)
c1.grid(row = 2, column = 1)

d = tk.Label(allergies_frame, text = "Tetanus antitoxin or or other serums")
d.grid(row = 3, column = 0, sticky = "w")
d1 = tk.Checkbutton(allergies_frame, variable = SulfaDrug_var)
d1.grid(row = 3, column = 1)

e = tk.Label(allergies_frame, text = "Iodine, Methiolate, or other antiseptic")
e.grid(row = 4, column = 0, sticky = "w")
e1 = tk.Checkbutton(allergies_frame, variable = Aspirin_var)
e1.grid(row = 4, column = 1)

f = tk.Label(allergies_frame, text = "Other drugs/medications")
f.grid(row = 5, column = 0, sticky = "w")
f1 = tk.Checkbutton(allergies_frame, variable = Ibuprofen_var)
f1.grid(row = 5, column = 1)

g = tk.Label(allergies_frame, text = "Known food allergies")
g.grid(row = 6, column = 0, sticky = "w")
g1 = tk.Checkbutton(allergies_frame, variable = Tetracycline_var)
g1.grid(row = 6, column = 1)

h = tk.Label(allergies_frame, text = "Environmental allergies")
h.grid(row = 7, column = 0, sticky = "w")
h1 = tk.Checkbutton(allergies_frame, variable = Cephlasporins_var)
h1.grid(row = 7, column = 1)

conditions_title = tk.Label(main_frame, text = "Please Mark Any of the Following Medical Conditions You Have:")
conditions_title.config(font = ("Arial", 15, "bold"))
conditions_title.pack(padx = 10, pady = 10)

conditions_frame = tk.Frame(main_frame)
conditions_frame.pack()

hemophilia_var = tk.IntVar()
arthritis_var = tk.IntVar()
acid_var = tk.IntVar()
hiv_var = tk.IntVar()
anemia_var = tk.IntVar()
asthma_var = tk.IntVar()
autoimmune_var = tk.IntVar()
cancer_var = tk.IntVar()
coldsore_var = tk.IntVar()
diabetes_var = tk.IntVar()
epilepsy_var = tk.IntVar()
headache_var = tk.IntVar()
glaucoma_var = tk.IntVar()
cholesterol_var = tk.IntVar()
joint_var = tk.IntVar()
kidney_var = tk.IntVar()
blood_var = tk.IntVar()
cardiovascular_var = tk.IntVar()
mental_var = tk.IntVar()
neurological_var = tk.IntVar()
liver_var = tk.IntVar()
respiratory_var = tk.IntVar()
thyroid_var = tk.IntVar()
organ_var = tk.IntVar()
pregnant_var = tk.IntVar()
breast_var = tk.IntVar()
ulcers_var = tk.IntVar()
osteoporosis_var = tk.IntVar()
celiac_var = tk.IntVar()
other_var = tk.IntVar()

m = tk.Label(conditions_frame, text = "Hemophilia/Bleeding")
m.grid(row = 0, column = 0, sticky = "w")
m1 = tk.Checkbutton(conditions_frame, variable = hemophilia_var)
m1.grid(row = 0, column = 1)

n = tk.Label(conditions_frame, text = "Arthritis")
n.grid(row = 1, column = 0, sticky = "w")
n1 = tk.Checkbutton(conditions_frame, variable = arthritis_var)
n1.grid(row = 1, column = 1)

o = tk.Label(conditions_frame, text = "Acid Reflux/GERD")
o.grid(row = 2, column = 0, sticky = "w")
o1 = tk.Checkbutton(conditions_frame, variable = acid_var)
o1.grid(row = 2, column = 1)

p = tk.Label(conditions_frame, text = "HIV/AIDS")
p.grid(row = 3, column = 0, sticky = "w")
p1 = tk.Checkbutton(conditions_frame, variable = hiv_var)
p1.grid(row = 3, column = 1)

q = tk.Label(conditions_frame, text = "Anemia/Sickle Cell")
q.grid(row = 4, column = 0, sticky = "w")
q1 = tk.Checkbutton(conditions_frame, variable = anemia_var)
q1.grid(row = 4, column = 1)

r = tk.Label(conditions_frame, text = "Asthma")
r.grid(row = 5, column = 0, sticky = "w")
r1 = tk.Checkbutton(conditions_frame, variable = asthma_var)
r1.grid(row = 5, column = 1)

s = tk.Label(conditions_frame, text = "Autoimmune Disorder")
s.grid(row = 6, column = 0, sticky = "w")
s1 = tk.Checkbutton(conditions_frame, variable = autoimmune_var)
s1.grid(row = 6, column = 1)

t = tk.Label(conditions_frame, text = "Cancer")
t.grid(row = 7, column = 0, sticky = "w")
t1 = tk.Checkbutton(conditions_frame, variable = cancer_var)
t1.grid(row = 7, column = 1)

u = tk.Label(conditions_frame, text = "Coldsore")
u.grid(row = 8, column = 0, sticky = "w")
u1 = tk.Checkbutton(conditions_frame, variable = coldsore_var)
u1.grid(row = 8, column = 1)

v = tk.Label(conditions_frame, text = "Diabetes")
v.grid(row = 9, column = 0, sticky = "w")
v1 = tk.Checkbutton(conditions_frame, variable = diabetes_var)
v1.grid(row = 9, column = 1)

w = tk.Label(conditions_frame, text = "Epilepsy")
w.grid(row = 10, column = 0, sticky = "w")
w1 = tk.Checkbutton(conditions_frame, variable = epilepsy_var)
w1.grid(row = 10, column = 1)

x = tk.Label(conditions_frame, text = "Headache")
x.grid(row = 11, column = 0, sticky = "w")
x1 = tk.Checkbutton(conditions_frame, variable = headache_var)
x1.grid(row = 11, column = 1)

y = tk.Label(conditions_frame, text = "Glaucoma")
y.grid(row = 12, column = 0, sticky = "w")
y1 = tk.Checkbutton(conditions_frame, variable = glaucoma_var)
y1.grid(row = 12, column = 1)

z = tk.Label(conditions_frame, text = "Cholesterol")
z.grid(row = 13, column = 0, sticky = "w")
z1 = tk.Checkbutton(conditions_frame, variable = cholesterol_var)
z1.grid(row = 13, column = 1)

a1 = tk.Label(conditions_frame, text = "Joint Issues")
a1.grid(row = 14, column = 0, sticky = "w")
a2 = tk.Checkbutton(conditions_frame, variable = joint_var)
a2.grid(row = 14, column = 1)

b1 = tk.Label(conditions_frame, text = "Kidney Issues")
b1.grid(row = 15, column = 0, sticky = "w")
b2 = tk.Checkbutton(conditions_frame, variable = kidney_var)
b2.grid(row = 15, column = 1)

c1 = tk.Label(conditions_frame, text = "Blood Pressure Issues")
c1.grid(row = 16, column = 0, sticky = "w")
c2 = tk.Checkbutton(conditions_frame, variable = blood_var)
c2.grid(row = 16, column = 1)

d1 = tk.Label(conditions_frame, text = "Cardiovascular Disease")
d1.grid(row = 17, column = 0, sticky = "w")
d2 = tk.Checkbutton(conditions_frame, variable = cardiovascular_var)
d2.grid(row = 17, column = 1)

e1 = tk.Label(conditions_frame, text = "Mental Health Disorders")
e1.grid(row = 18, column = 0, sticky = "w")
e2 = tk.Checkbutton(conditions_frame, variable = mental_var)
e2.grid(row = 18, column = 1)

f1 = tk.Label(conditions_frame, text = "Neurological Issues")
f1.grid(row = 19, column = 0, sticky = "w")
f2 = tk.Checkbutton(conditions_frame, variable = neurological_var)
f2.grid(row = 19, column = 1)

g1 = tk.Label(conditions_frame, text = "Liver Problems")
g1.grid(row = 20, column = 0, sticky = "w")
g2 = tk.Checkbutton(conditions_frame, variable = liver_var)
g2.grid(row = 20, column = 1)

h1 = tk.Label(conditions_frame, text = "Respiratory Disease")
h1.grid(row = 21, column = 0, sticky = "w")
h2 = tk.Checkbutton(conditions_frame, variable = respiratory_var)
h2.grid(row = 21, column = 1)

i1 = tk.Label(conditions_frame, text = "Thyroid Issues")
i1.grid(row = 22, column = 0, sticky = "w")
i2 = tk.Checkbutton(conditions_frame, variable = thyroid_var)
i2.grid(row = 22, column = 1)

j1 = tk.Label(conditions_frame, text = "Organ Transplant")
j1.grid(row = 23, column = 0, sticky = "w")
j2 = tk.Checkbutton(conditions_frame, variable = organ_var)
j2.grid(row = 23, column = 1)

k1 = tk.Label(conditions_frame, text = "Pregnant")
k1.grid(row = 24, column = 0, sticky = "w")
k2 = tk.Checkbutton(conditions_frame, variable = pregnant_var)
k2.grid(row = 24, column = 1)

l1 = tk.Label(conditions_frame, text = "Breast Feeding")
l1.grid(row = 25, column = 0, sticky = "w")
l2 = tk.Checkbutton(conditions_frame, variable = breast_var)
l2.grid(row = 25, column = 1)

m1 = tk.Label(conditions_frame, text = "Ulcers")
m1.grid(row = 26, column = 0, sticky = "w")
m2 = tk.Checkbutton(conditions_frame, variable = ulcers_var)
m2.grid(row = 26, column = 1)

n1 = tk.Label(conditions_frame, text = "Osteoporosis")
n1.grid(row = 27, column = 0, sticky = "w")
n2 = tk.Checkbutton(conditions_frame, variable = osteoporosis_var)
n2.grid(row = 27, column = 1)

o1 = tk.Label(conditions_frame, text = "Celiac")
o1.grid(row = 28, column = 0, sticky = "w")
o2 = tk.Checkbutton(conditions_frame, variable = celiac_var)
o2.grid(row = 28, column = 1)


symptoms_title = tk.Label(main_frame, text = "Please Mark Any of the Following Symptoms you Have:")
symptoms_title.config(font = ("Arial", 15, "bold"))
symptoms_title.pack(padx = 10, pady = 10)

constititional_title = tk.Label(main_frame, text = "Constitutional Symptoms")
constititional_title.config(font = ("Arial", 15, "bold"))
constititional_title.pack(padx = 10, pady = 10)

symptoms_frame = tk.Frame(main_frame)
symptoms_frame.pack()

health_var = tk.IntVar()
weight_var = tk.IntVar()
fever_var = tk.IntVar()
fatigue_var = tk.IntVar()
headache_var = tk.IntVar()

u1 = tk.Label(symptoms_frame, text = "Good general health lately")
u1.grid(row = 0, column = 0, sticky = "w")
u2 = tk.Checkbutton(symptoms_frame, variable = health_var)
u2.grid(row = 0, column = 1)

v1 = tk.Label(symptoms_frame, text = "Recent weight change")
v1.grid(row = 1, column = 0, sticky = "w")
v2 = tk.Checkbutton(symptoms_frame, variable = weight_var)
v2.grid(row = 1, column = 1)

w1 = tk.Label(symptoms_frame, text = "Fever")
w1.grid(row = 2, column = 0, sticky = "w")
w2 = tk.Checkbutton(symptoms_frame, variable = fever_var)
w2.grid(row = 2, column = 1)

x1 = tk.Label(symptoms_frame, text = "Fatigue")
x1.grid(row = 3, column = 0, sticky = "w")
x2 = tk.Checkbutton(symptoms_frame, variable = fatigue_var)
x2.grid(row = 3, column = 1)

y1 = tk.Label(symptoms_frame, text = "Headache")
y1.grid(row = 4, column = 0, sticky = "w")
y2 = tk.Checkbutton(symptoms_frame, variable = headache_var)
y2.grid(row = 4, column = 1)

eyes_title = tk.Label(main_frame, text = "Eyes")
eyes_title.config(font = ("Arial", 15, "bold"))
eyes_title.pack(padx = 10, pady = 10)

eyes_frame = tk.Frame(main_frame)
eyes_frame.pack()

disease_var = tk.IntVar()
lenses_var = tk.IntVar()
blurred_var = tk.IntVar()

disease = tk.Label(eyes_frame, text = "Eye disease or injury")
disease.grid(row = 0, column = 0, sticky = "w")
disease1 = tk.Checkbutton(eyes_frame, variable = disease_var)
disease1.grid(row = 0, column = 1)

lenses = tk.Label(eyes_frame, text = "Wear glasses/contact lenses")
lenses.grid(row = 1, column = 0, sticky = "w")
lenses1 = tk.Checkbutton(eyes_frame, variable = lenses_var)
lenses1.grid(row = 1, column = 1)

blurred = tk.Label(eyes_frame, text = "Blurred or double vision")
blurred.grid(row = 2, column = 0, sticky = "w")
blurred1 = tk.Checkbutton(eyes_frame, variable = blurred_var)
blurred1.grid(row = 2, column = 1)

ears_title = tk.Label(main_frame, text = "Ears/Nose/Mouth/Throat")
ears_title.config(font = ("Arial", 15, "bold"))
ears_title.pack(padx = 10, pady = 10)

ears_frame = tk.Frame(main_frame)
ears_frame.pack()

loss_var = tk.IntVar()
earache_var = tk.IntVar()
nosebleed_var = tk.IntVar()
sores_var = tk.IntVar()
bleeding_var = tk.IntVar()
breath_var = tk.IntVar()
throat_var = tk.IntVar()
glands_var = tk.IntVar()

loss = tk.Label(ears_frame, text = "Hearing loss or ringing")
loss.grid(row = 0, column = 0, sticky = "w")
loss1 = tk.Checkbutton(ears_frame, variable = loss_var)
loss1.grid(row = 0, column = 1)

earache = tk.Label(ears_frame, text = "Earaches or drainage")
earache.grid(row = 1, column = 0, sticky = "w")
earache1 = tk.Checkbutton(ears_frame, variable = earache_var)
earache1.grid(row = 1, column = 1)

nosebleed = tk.Label(ears_frame, text = "Nosebleeds/Sinus Problems/Rhinitis")
nosebleed.grid(row = 2, column = 0, sticky = "w")
nosebleed1 = tk.Checkbutton(ears_frame, variable = nosebleed_var)
nosebleed1.grid(row = 2, column = 1)

sores = tk.Label(ears_frame, text = "Mouth Sores")
sores.grid(row = 3, column = 0, sticky = "w")
sores1 = tk.Checkbutton(ears_frame, variable = sores_var)
sores1.grid(row = 3, column = 1)

bleeding = tk.Label(ears_frame, text = "Bleeding Gums")
bleeding.grid(row = 4, column = 0, sticky = "w")
bleeding1 = tk.Checkbutton(ears_frame, variable = bleeding_var)
bleeding1.grid(row = 4, column = 1)

breath = tk.Label(ears_frame, text = "Bad breathe or bad taste")
breath.grid(row = 5, column = 0, sticky = "w")
breath1 = tk.Checkbutton(ears_frame, variable = breath_var)
breath1.grid(row = 5, column = 1)

throat = tk.Label(ears_frame, text = "Sore throat or voice change")
throat.grid(row = 6, column = 0, sticky = "w")
throat1 = tk.Checkbutton(ears_frame, variable = throat_var)
throat1.grid(row = 6, column = 1)

glands = tk.Label(ears_frame, text = "Swollen glands in neck")
glands.grid(row = 7, column = 0, sticky = "w")
glands1 = tk.Checkbutton(ears_frame, variable = glands_var)
glands1.grid(row = 7, column = 1)

cardio_title = tk.Label(main_frame, text = "Cardiovascular")
cardio_title.config(font = ("Arial", 15, "bold"))
cardio_title.pack(padx = 10, pady = 10)

cardio_frame = tk.Frame(main_frame)
cardio_frame.pack()

heart_var = tk.IntVar()
chest_var = tk.IntVar()
palp_var = tk.IntVar()
short_var = tk.IntVar()
swell_var = tk.IntVar()


heart = tk.Label(cardio_frame, text = "Heart Trouble")
heart.grid(row = 0, column = 0, sticky = "w")
heart1 = tk.Checkbutton(cardio_frame, variable = heart_var)
heart1.grid(row = 0, column = 1)

chest = tk.Label(cardio_frame, text = "Chest pain or Angina Pectoris")
chest.grid(row = 1, column = 0, sticky = "w")
chest1 = tk.Checkbutton(cardio_frame, variable = chest_var)
chest1.grid(row = 1, column = 1, sticky = "w")

palp = tk.Label(cardio_frame, text = "Palpitations")
palp.grid(row = 2, column = 0, sticky = "w")
palp1 = tk.Checkbutton(cardio_frame, variable = palp_var)
palp1.grid(row = 2, column = 1, sticky = "w")

short = tk.Label(cardio_frame, text = "Shortness of breath while walking or lying flat")
short.grid(row = 3, column = 0, sticky = "w")
short1 = tk.Checkbutton(cardio_frame, variable = short_var)
short1.grid(row = 3, column = 1, sticky = "w")

swell = tk.Label(cardio_frame, text = "Swelling of feet, ankles, or hands")
swell.grid(row = 4, column = 0, sticky = "w")
swell1 = tk.Checkbutton(cardio_frame, variable = swell_var)
swell1.grid(row = 4, column = 1, sticky = "w")


respiratory_title = tk.Label(main_frame, text = "Respiratory")
respiratory_title.config(font = ("Arial", 15, "bold"))
respiratory_title.pack(padx = 10, pady = 10)

respiratory_frame = tk.Frame(main_frame)
respiratory_frame.pack()

chronic_var = tk.IntVar()
spit_var = tk.IntVar()
shortness_var = tk.IntVar()
wheezing_var = tk.IntVar()


chronic = tk.Label(respiratory_frame, text = "Chronic or frequent coughs")
chronic.grid(row = 0, column = 0, sticky = "w")
chronic1 = tk.Checkbutton(respiratory_frame, variable = chronic_var)
chronic1.grid(row = 0, column = 1)

spit = tk.Label(respiratory_frame, text = "Spitting up blood")
spit.grid(row = 1, column = 0, sticky = "w")
spit1 = tk.Checkbutton(respiratory_frame, variable = spit_var)
spit1.grid(row = 1, column = 1)

shortness = tk.Label(respiratory_frame, text = "Shortness of Breath")
shortness.grid(row = 2, column = 0, sticky = "w")
shortness1 = tk.Checkbutton(respiratory_frame, variable = shortness_var)
shortness1.grid(row = 2, column = 1)

wheezing = tk.Label(respiratory_frame, text = "Wheezing")
wheezing.grid(row = 3, column = 0, sticky = "w")
wheezing1 = tk.Checkbutton(respiratory_frame, variable = wheezing_var)
wheezing1.grid(row = 3, column = 1)


gastrointestinal_title = tk.Label(main_frame, text = "Gastrointestinal")
gastrointestinal_title.config(font = ("Arial", 15, "bold"))
gastrointestinal_title.pack(padx = 10, pady = 10)

gastrointestinal_frame = tk.Frame(main_frame)
gastrointestinal_frame.pack()

appetite_var = tk.IntVar()
bowel_var = tk.IntVar()
nausea_var = tk.IntVar()
diarrhea_var = tk.IntVar()
constipation_var = tk.IntVar()
rectal_var = tk.IntVar()
abdominal_var = tk.IntVar()


appetite = tk.Label(gastrointestinal_frame, text = "Loss of Appetite")
appetite.grid(row = 0, column = 0, sticky = "w")
appetite1 = tk.Checkbutton(gastrointestinal_frame, variable = appetite_var)
appetite1.grid(row = 0, column = 1)

bowel = tk.Label(gastrointestinal_frame, text = "Change in Bowel Movements")
bowel.grid(row = 1, column = 0, sticky = "w")
bowel1 = tk.Checkbutton(gastrointestinal_frame, variable = bowel_var)
bowel1.grid(row = 1, column = 1)

nausea = tk.Label(gastrointestinal_frame, text = "Nausea or Vomiting")
nausea.grid(row = 2, column = 0, sticky = "w")
nausea1 = tk.Checkbutton(gastrointestinal_frame, variable = nausea_var)
nausea1.grid(row = 2, column = 1)

diarrhea = tk.Label(gastrointestinal_frame, text = "Frequent Diarrhea")
diarrhea.grid(row = 3, column = 0, sticky = "w")
diarrhea1 = tk.Checkbutton(gastrointestinal_frame, variable = diarrhea_var)
diarrhea1.grid(row = 3, column = 1)

constipation = tk.Label(gastrointestinal_frame, text = "Painful bowel movements or constipation")
constipation.grid(row = 4, column = 0, sticky = "w")
constipation1 = tk.Checkbutton(gastrointestinal_frame, variable = constipation_var)
constipation1.grid(row = 4, column = 1)

rectal = tk.Label(gastrointestinal_frame, text = "Rectal bleeding or blood in stool")
rectal.grid(row = 5, column = 0, sticky = "w")
rectal1 = tk.Checkbutton(gastrointestinal_frame, variable = rectal_var)
rectal1.grid(row = 5, column = 1)

abdominal = tk.Label(gastrointestinal_frame, text = "Abdominal Pain")
abdominal.grid(row = 6, column = 0, sticky = "w")
abdominal1 = tk.Checkbutton(gastrointestinal_frame, variable = abdominal_var)
abdominal1.grid(row = 6, column = 1)

musculoskeletal_title = tk.Label(main_frame, text = "Musculoskeletal")
musculoskeletal_title.config(font = ("Arial", 15, "bold"))
musculoskeletal_title.pack(padx = 10, pady = 10)

musculoskeletal_frame = tk.Frame(main_frame)
musculoskeletal_frame.pack()

joint1_var = tk.IntVar()
joint3_var = tk.IntVar()
weakness_var = tk.IntVar()
cramps_var = tk.IntVar()
back_var = tk.IntVar()
cold_var = tk.IntVar()
walking_var = tk.IntVar()



joint1 = tk.Label(musculoskeletal_frame, text = "Joint Pain")
joint1.grid(row = 0, column = 0, sticky = "w")
joint2 = tk.Checkbutton(musculoskeletal_frame, variable = joint1_var)
joint2.grid(row = 0, column = 1)

joint3 = tk.Label(musculoskeletal_frame, text = "Joint Stiffness or Swelling")
joint3.grid(row = 1, column = 0, sticky = "w")
joint4 = tk.Checkbutton(musculoskeletal_frame, variable = joint3_var)
joint4.grid(row = 1, column = 1)

weakness = tk.Label(musculoskeletal_frame, text = "Weakness of muscles or joints")
weakness.grid(row = 2, column = 0, sticky = "w")
weakness1 = tk.Checkbutton(musculoskeletal_frame, variable = weakness_var)
weakness1.grid(row = 2, column = 1)

cramps = tk.Label(musculoskeletal_frame, text = "Muscle pain or cramps")
cramps.grid(row = 3, column = 0, sticky = "w")
cramps1 = tk.Checkbutton(musculoskeletal_frame, variable = cramps_var)
cramps1.grid(row = 3, column = 1)

back = tk.Label(musculoskeletal_frame, text = "Back Pain")
back.grid(row = 4, column = 0, sticky = "w")
back1 = tk.Checkbutton(musculoskeletal_frame, variable = back_var)
back1.grid(row = 4, column = 1)

cold = tk.Label(musculoskeletal_frame, text = "Cold Extremities")
cold.grid(row = 5, column = 0, sticky = "w")
cold1 = tk.Checkbutton(musculoskeletal_frame, variable = cold_var)
cold1.grid(row = 5, column = 1)

walking = tk.Label(musculoskeletal_frame, text = "Difficulty Walking")
walking.grid(row = 6, column = 0, sticky = "w")
walking1 = tk.Checkbutton(musculoskeletal_frame, variable = walking_var)


integumentary_title = tk.Label(main_frame, text = "Integumentary")
integumentary_title.config(font = ("Arial", 15, "bold"))
integumentary_title.pack(padx = 10, pady = 10)

integumentary_frame = tk.Frame(main_frame)
integumentary_frame.pack()

rash_var = tk.IntVar()
color_var = tk.IntVar()
hair_var = tk.IntVar()
varicose_var = tk.IntVar()
headache1_var = tk.IntVar()
dizzy_var = tk.IntVar()
convulsions_var = tk.IntVar()
tingling_var = tk.IntVar()
paralysis_var = tk.IntVar()
tremors_var = tk.IntVar()
head_var = tk.IntVar()


rash = tk.Label(integumentary_frame, text = "Rash or Itching")
rash.grid(row = 0, column = 0, sticky = "w")
rash1 = tk.Checkbutton(integumentary_frame, variable = rash_var)
rash1.grid(row = 0, column = 1)

color = tk.Label(integumentary_frame, text = "Change in skin color")
color.grid(row = 1, column = 0, sticky = "w")
color1 = tk.Checkbutton(integumentary_frame, variable = color_var)
color1.grid(row = 1, column = 1)

hair = tk.Label(integumentary_frame, text = "Change in hair or nails")
hair.grid(row = 2, column = 0, sticky = "w")
hair1 = tk.Checkbutton(integumentary_frame, variable = hair_var)
hair1.grid(row = 2, column = 1)

varicose = tk.Label(integumentary_frame, text = "Varicose Veins")
varicose.grid(row = 3, column = 0, sticky = "w")
varicose1 = tk.Checkbutton(integumentary_frame, variable = varicose_var)
varicose1.grid(row = 3, column = 1)

neurological_title = tk.Label(main_frame, text = "Neurological")
neurological_title.config(font = ("Arial", 15, "bold"))
neurological_title.pack(padx = 10, pady = 10)

neurological_frame = tk.Frame(main_frame)
neurological_frame.pack()

headache1 = tk.Label(neurological_frame, text = "Frequent or Reoccuring Headache")
headache1.grid(row = 0, column = 0, sticky = "w")
headache2 = tk.Checkbutton(neurological_frame, variable = headache1_var)
headache2.grid(row = 0, column = 1)

dizzy = tk.Label(neurological_frame, text = "Lightheaded or dizzy")
dizzy.grid(row = 1, column = 0, sticky = "w")
dizzy1 = tk.Checkbutton(neurological_frame, variable = dizzy_var)
dizzy1.grid(row = 1, column = 1)

convulsions = tk.Label(neurological_frame, text = "Convulsions or Seizures")
convulsions.grid(row = 2, column = 0, sticky = "w")
convulsions1 = tk.Checkbutton(neurological_frame, variable = convulsions_var)
convulsions1.grid(row = 2, column = 1)

tingling =  tk.Label(neurological_frame, text = "Numbness or Tingling Sensations")
tingling.grid(row = 3, column = 0, sticky = "w")
tingling1 = tk.Checkbutton(neurological_frame, variable = tingling_var)
tingling1.grid(row = 3, column = 1)

paralysis = tk.Label(neurological_frame, text = "Paralysis")
paralysis.grid(row = 4, column = 0, sticky = "w")
paralysis1 = tk.Checkbutton(neurological_frame, variable = paralysis_var)
paralysis1.grid(row = 4, column = 1)

tremors = tk.Label(neurological_frame, text = "Tremors")
tremors.grid(row = 5, column = 0, sticky = "w")
tremors1 = tk.Checkbutton(neurological_frame, variable = tremors_var)
tremors1.grid(row = 5, column = 1)

head = tk.Label(neurological_frame, text = "Headache")
head.grid(row = 6, column = 0, sticky = "w")
head1 = tk.Checkbutton(neurological_frame, variable = head_var)
head1.grid(row = 6, column = 1)

psychiatric_title = tk.Label(main_frame, text = "Psychiatric")
psychiatric_title.config(font = ("Arial", 15, "bold"))
psychiatric_title.pack(padx = 10, pady = 10)

psychiatric_frame = tk.Frame(main_frame)
psychiatric_frame.pack()

loss1_var = tk.IntVar()
nervousness_var = tk.IntVar()
depression_var = tk.IntVar()
insomnia_var = tk.IntVar()


loss1 = tk.Label(psychiatric_frame, text = "Memory loss or confusion")
loss1.grid(row = 0, column = 0, sticky = "w")
loss2 = tk.Checkbutton(psychiatric_frame, variable = loss1_var)
loss2.grid(row = 0, column = 1)

nervousness = tk.Label(psychiatric_frame, text = "Nervousness")
nervousness.grid(row = 1, column = 0, sticky = "w")
nervousness2 = tk.Checkbutton(psychiatric_frame, variable = nervousness_var)
nervousness2.grid(row = 1, column = 1)

depression = tk.Label(psychiatric_frame, text = "Depression")
depression.grid(row = 2, column = 0, sticky = "w")
depression1 = tk.Checkbutton(psychiatric_frame, variable = depression_var)
depression1.grid(row = 2, column = 1)

insomnia = tk.Label(psychiatric_frame, text = "Insomnia")
insomnia.grid(row = 3, column = 0, sticky = "w")
insomnia1 = tk.Checkbutton(psychiatric_frame, variable = insomnia_var)
insomnia1.grid(row = 3, column = 1)

endocrine_title = tk.Label(main_frame, text = "Endocrine")
endocrine_title.config(font = ("Arial", 15, "bold"))
endocrine_title.pack(padx = 10, pady = 10)

endocrine_frame = tk.Frame(main_frame)
endocrine_frame.pack()

hormone_var = tk.IntVar()
thirst_var = tk.IntVar()
heat_var = tk.IntVar()
dry_var = tk.IntVar()
size_var = tk.IntVar()


hormone = tk.Label(endocrine_frame, text = "Glandular or hormone problem")
hormone.grid(row = 0, column = 0, sticky = "w")
hormone1 = tk.Checkbutton(endocrine_frame, variable = hormone_var)
hormone1.grid(row = 0, column = 1)

thirst = tk.Label(endocrine_frame, text = "Excessive thirst or urination")
thirst.grid(row = 1, column = 0, sticky = "w")
thirst1 = tk.Checkbutton(endocrine_frame, variable = thirst_var)
thirst1.grid(row = 1, column = 1)

heat = tk.Label(endocrine_frame, text = "Heat or cold intolerance")
heat.grid(row = 2, column = 0, sticky = "w")
heat1 = tk.Checkbutton(endocrine_frame, variable = heat_var)
heat1.grid(row = 2, column = 1)

dry = tk.Label(endocrine_frame, text = "Skin becoming drier")
dry.grid(row = 3, column = 0, sticky = "w")
dry1 = tk.Checkbutton(endocrine_frame, variable = dry_var)
dry1.grid(row = 3, column = 1)

size = tk.Label(endocrine_frame, text = "Change in hat or glove size")
size.grid(row = 4, column = 0, sticky = "w")
size1 = tk.Checkbutton(endocrine_frame, variable = size_var)
size1.grid(row = 4, column = 1)

hematologic_title = tk.Label(main_frame, text = "Hematologic/Lymphatic")
hematologic_title.config(font = ("Arial", 15, "bold"))
hematologic_title.pack(padx = 10, pady = 10)

hematologic_frame = tk.Frame(main_frame)
hematologic_frame.pack()

heal_var = tk.IntVar()
bruising_var = tk.IntVar()
phlebitis_var = tk.IntVar()
transfusion_var = tk.IntVar()
glands1_var = tk.IntVar()

heal = tk.Label(hematologic_frame, text = "Slow to heal after cuts")
heal.grid(row = 0, column = 0, sticky = "w")
heal1 = tk.Checkbutton(hematologic_frame, variable = heal_var)
heal1.grid(row = 0, column = 1)

bruising = tk.Label(hematologic_frame, text = "Bleeding or bruising tendency")
bruising.grid(row = 1, column = 0, sticky = "w")
bruising1 = tk.Checkbutton(hematologic_frame, variable = bruising_var)
bruising1.grid(row = 1, column = 1)

anemia = tk.Label(hematologic_frame, text = "Anemia")
anemia.grid(row = 2, column = 0, sticky = "w")
anemia1 = tk.Checkbutton(hematologic_frame, variable = anemia_var)
anemia1.grid(row = 2, column = 1)

phlebitis = tk.Label(hematologic_frame, text = "Phlebitis")
phlebitis.grid(row = 3, column = 0, sticky = "w")
phlebitis1 = tk.Checkbutton(hematologic_frame, variable = phlebitis_var)
phlebitis1.grid(row = 3, column = 1)

transfusion = tk.Label(hematologic_frame, text = "Past transfusion")
transfusion.grid(row = 4, column = 0, sticky = "w")
transfusion1 = tk.Checkbutton(hematologic_frame, variable = transfusion_var)
transfusion1.grid(row = 4, column = 1)

glands1 = tk.Label(hematologic_frame, text = "Enlarged Glands")
glands1.grid(row = 5, column = 0, sticky = "w")
glands2 = tk.Checkbutton(hematologic_frame, variable = glands1_var)
glands2.grid(row = 5, column = 1)

window.mainloop()