import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
window = tk.Tk()
window.title("login form")
window.geometry("480x480")

frame = tk.Frame(window)
frame.pack(fill="both",side="top")

user_personal_info_frame = tk.LabelFrame(frame,text="Personal Info:")
user_personal_info_frame.pack(side="left",padx=20,pady=15)
#creating widgets
first_name_label = tk.Label(user_personal_info_frame,text="First name")
first_name_label.grid(row=0,column=0)

second_name_label = tk.Label(user_personal_info_frame,text="Second name")
second_name_label.grid(row=1,column=0)

surname_label = tk.Label(user_personal_info_frame,text="Surname")
surname_label.grid(row=2,column=0)

age_label = tk.Label(user_personal_info_frame,text="Age:")
age_label.grid(row=3,column=0)

gender_label = tk.Label(user_personal_info_frame,text="Gender:")
gender_label.grid(row=4,column=0)

date_of_birth_label = tk.Label(user_personal_info_frame,text="Date Of Birth:")
date_of_birth_label.grid(row=5,column=0)

civil_status_label =tk.Label(user_personal_info_frame,text="Civil Status:")
civil_status_label.grid(row=6,column=0)

citizenship_label =tk.Label(user_personal_info_frame,text="Citizenship:")
citizenship_label.grid(row=7,column=0)

blood_type_label =tk.Label(user_personal_info_frame,text="Blood Type:")
blood_type_label.grid(row=8,column=0)

height_label =tk.Label(user_personal_info_frame,text="Height:")
height_label.grid(row=9,column=0)

weight_label =tk.Label(user_personal_info_frame,text="Weight:")
weight_label.grid(row=10,column=0)

TIN_label =tk.Label(user_personal_info_frame,text="T.I.N:")
TIN_label.grid(row=11,column=0)

National_id_num_label =tk.Label(user_personal_info_frame,text="National ID number:")
National_id_num_label.grid(row=12,column=0)

address_label =tk.Label(user_personal_info_frame,text="Home Address:")
address_label.grid(row=13,column=0)

email_label =tk.Label(user_personal_info_frame,text="Email:")
email_label.grid(row=14,column=0)

place_of_birth_label =tk.Label(user_personal_info_frame,text="Place of Birth:")
place_of_birth_label.grid(row=15,column=0)

title_label =tk.Label(user_personal_info_frame,text="Title:")
title_label.grid(row=16,column=0)



first_name_entry = tk.Entry(user_personal_info_frame)
first_name_entry.grid(row=0,column=1)

second_name_entry = tk.Entry(user_personal_info_frame)
second_name_entry.grid(row=1,column=1)

surname_entry = tk.Entry(user_personal_info_frame)
surname_entry.grid(row=2,column=1)

age_spinbox = tk.Spinbox(user_personal_info_frame,from_=0,to=100)
age_spinbox.grid(row=3,column=1)

gender_Male_checkbutton = tk.Checkbutton(user_personal_info_frame,text="MALE")
gender_Male_checkbutton.grid(row=4,column=1)

gender_Female_checkbutton = tk.Checkbutton(user_personal_info_frame,text="FEMALE")
gender_Female_checkbutton.grid(row=4,column=2)

date_of_birth_data_entry = DateEntry(user_personal_info_frame, date_pattern="yyyy-mm-dd")
date_of_birth_data_entry.grid(row=5,column=1)

civil_status_married_checkbutton =tk.Checkbutton(user_personal_info_frame,text="Married")
civil_status_married_checkbutton.grid(row=6,column=1)

civil_status_N_married_checkbutton =tk.Checkbutton(user_personal_info_frame,text="Not Married")
civil_status_N_married_checkbutton.grid(row=6,column=2)

citizenship_combobox =ttk.Combobox(user_personal_info_frame,values=["select type","By Naturalisation","By Decscent","By Birth"])
citizenship_combobox.grid(row=7,column=1)

blood_type_combobox =ttk.Combobox(user_personal_info_frame,values=["select blood type","A+","A-","B+","B-","0+","O-","AB+","AB-"])
blood_type_combobox.grid(row=8,column=1)

height_spinbox =tk.Spinbox(user_personal_info_frame,from_=0,to="infinity")
height_spinbox.grid(row=9,column=1)

weight_spinbox =tk.Spinbox(user_personal_info_frame,from_=0,to="infinity")
weight_spinbox.grid(row=10,column=1)

TIN_entry =tk.Entry(user_personal_info_frame)
TIN_entry.grid(row=11,column=1)

National_id_num_entry =tk.Entry(user_personal_info_frame)
National_id_num_entry.grid(row=12,column=1)

address_entry =tk.Entry(user_personal_info_frame)
address_entry.grid(row=13,column=1)

email_entry =tk.Entry(user_personal_info_frame)
email_entry.grid(row=14,column=1)

place_of_birth_entry =tk.Entry(user_personal_info_frame)
place_of_birth_entry.grid(row=15,column=1)

title_entry =tk.Entry(user_personal_info_frame)
title_entry.grid(row=16,column=1)

#user family background
user_family_background = tk.LabelFrame(frame,text="Family Background:")
user_family_background.pack(side="left",padx=20,pady=15)


father_name_label =tk.Label(user_family_background,text="Father's Name:")
father_name_label.grid(row=0,column=0)

mother_name_label =tk.Label(user_family_background,text="Mother's Name:")
mother_name_label.grid(row=1,column=0)

spouse_full_name_label =tk.Label(user_family_background,text="Spouse's Full Name")
spouse_full_name_label.grid(row=2,column=0)

occupation_label =tk.Label(user_family_background,text="Occupation:")
occupation_label.grid(row=3,column=0)

business_address_label =tk.Label(user_family_background,text="Business/Work Address:")
business_address_label.grid(row=4,column=0)

number_of_children_label =tk.Label(user_family_background,text="No. of Children:")
number_of_children_label.grid(row=5,column=0)


father_name_entry = tk.Entry(user_family_background)
father_name_entry.grid(row=0,column=1)

mother_name_entry =tk.Entry(user_family_background)
mother_name_entry.grid(row=1,column=1)

spouse_full_name_entry =tk.Entry(user_family_background)
spouse_full_name_entry.grid(row=2,column=1)

occupation_entry =tk.Entry(user_family_background)
occupation_entry.grid(row=3,column=1)

business_address_entry =tk.Entry(user_family_background)
business_address_entry.grid(row=4,column=1)

number_of_children_spinbox =tk.Spinbox(user_family_background,from_=0,to="infinity")
number_of_children_spinbox.grid(row=5,column=1)

#user educational background
user_educational_background = tk.LabelFrame(frame,text="Educational Background:")
user_educational_background.pack(side="left",padx=20,pady=15)


level_label =tk.Label(user_educational_background,text="LEVEL")
level_label.grid(row=0,column=0)

nursery_label =tk.Label(user_educational_background,text="nursery")
nursery_label.grid(row=1,column=0)

primary_label =tk.Label(user_educational_background,text="primary")
primary_label.grid(row=2,column=0)

o_level_label =tk.Label(user_educational_background,text="o level")
o_level_label.grid(row=3,column=0)

a_level_label =tk.Label(user_educational_background,text="A level")
a_level_label.grid(row=4,column=0)

university_label =tk.Label(user_educational_background,text="university")
university_label.grid(row=5,column=0)

name_of_school_label =tk.Label(user_educational_background,text="name of school")
name_of_school_label.grid(row=0,column=1)

basic_education_label =tk.Label(user_educational_background,text="combination/course")
basic_education_label.grid(row=0,column=2)

from_label =tk.Label(user_educational_background,text="From")
from_label.grid(row=0,column=3)

to_label =tk.Label(user_educational_background,text="To")
to_label.grid(row=0,column=4)

achievement_label=tk.Label(user_educational_background,text="Achievements")
achievement_label.grid(row=0,column=5)


window.mainloop()
