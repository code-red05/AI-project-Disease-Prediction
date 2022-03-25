from tkinter import *

root = Tk()

root.geometry("500x300")


def update(data):
    my_list.delete(0, END)
    for item in data:
        my_list.insert(END, item)


def fillout(e):
    my_entry.delete(0, END)

    my_entry.insert(0, my_list.get(ANCHOR))


def check(e):
    typed = my_entry.get()

    if typed == '':
        data = symptoms
    else:
        data = []
        for item in symptoms:
            if typed.lower() in item.lower():
                data.append(item)

    update(data)


def update2(data):
    my_list.delete(0, END)
    for item in data:
        my_list.insert(END, item)


def fillout2(e):
    my_entry2.delete(0, END)

    my_entry2.insert(0, my_list.get(ANCHOR))


def check2(e):
    typed = my_entry2.get()

    if typed == '':
        data = symptoms
    else:
        data = []
        for item in symptoms:
            if typed.lower() in item.lower():
                data.append(item)

    update2(data)


my_label = Label(root, text="Start Typing...",
                 font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

my_entry2 = Entry(root, font=("Helvetica", 20))
my_entry2.pack()

my_list = Listbox(root, width=50)
my_list.pack(pady=40)

symptoms = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
            'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']


update(symptoms)

my_list.bind("<<ListboxSelect>>", fillout)

my_entry.bind("<KeyRelease>", check)

update2(symptoms)

my_list.bind("<<ListboxSelect>>", fillout2)

my_entry2.bind("<KeyRelease>", check2)

root.mainloop()

from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *

countries = [
        'Antigua and Barbuda', 'Bahamas','Barbados','Belize', 'Canada',
        'Costa Rica ', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador ',
        'Grenada', 'Guatemala ', 'Haiti', 'Honduras ', 'Jamaica', 'Mexico',
        'Nicaragua', 'Saint Kitts and Nevis', 'Panama ', 'Saint Lucia', 
        'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States of America'
        ]

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#8DBF5A')

frame = Frame(ws, bg='#8DBF5A')
frame.pack(expand=True)

Label(
    frame, 
    bg='#8DBF5A',
    font = ('Times',21),
    text='Countries in North America '
    ).pack()

entry = AutocompleteCombobox(
    frame, 
    width=30, 
    font=('Times', 18),
    completevalues=countries
    )
entry.pack()




Label(
    frame, 
    bg='#8DBF5A',
    font = ('Times',21),
    text='Symptom 2 '
    ).pack()

entry2 = AutocompleteCombobox(
    frame, 
    width=30, 
    font=('Times', 18),
    completevalues=countries
    )
entry2.pack()










ws.mainloop()   