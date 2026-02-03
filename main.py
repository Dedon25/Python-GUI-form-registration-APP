import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

window = tk.Tk()
window.title("Registration Form")
window.geometry("1200x520")

# ================= MAIN FRAME =================
frame = tk.Frame(window)
frame.pack(fill="both", side="top")

# ================= PERSONAL INFO =================
user_personal_info_frame = tk.LabelFrame(frame, text="Personal Info:")
user_personal_info_frame.pack(side="left", padx=10, pady=10)

labels = [
    "First name", "Second name", "Surname", "Age", "Gender",
    "Date Of Birth", "Civil Status", "Citizenship", "Blood Type",
    "Height", "Weight", "T.I.N", "National ID number",
    "Home Address", "Email", "Place of Birth", "Title"
]

for i, label in enumerate(labels):
    tk.Label(user_personal_info_frame, text=label).grid(row=i, column=0, sticky="w")

first_name = tk.Entry(user_personal_info_frame)
second_name = tk.Entry(user_personal_info_frame)
surname = tk.Entry(user_personal_info_frame)
age = tk.Spinbox(user_personal_info_frame, from_=0, to=120)

gender = tk.StringVar()
tk.Radiobutton(user_personal_info_frame, text="Male", variable=gender, value="Male").grid(row=4, column=1)
tk.Radiobutton(user_personal_info_frame, text="Female", variable=gender, value="Female").grid(row=4, column=2)

dob = DateEntry(user_personal_info_frame, date_pattern="yyyy-mm-dd")

civil_status = tk.StringVar()
tk.Radiobutton(user_personal_info_frame, text="Married", variable=civil_status, value="Married").grid(row=6, column=1)
tk.Radiobutton(user_personal_info_frame, text="Single", variable=civil_status, value="Single").grid(row=6, column=2)

citizenship = ttk.Combobox(user_personal_info_frame, values=[
    "By Birth", "By Naturalisation", "By Descent"
])

blood_type = ttk.Combobox(user_personal_info_frame, values=[
    "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"
])

height = tk.Spinbox(user_personal_info_frame, from_=0, to=300)
weight = tk.Spinbox(user_personal_info_frame, from_=0, to=300)
tin = tk.Entry(user_personal_info_frame)
nid = tk.Entry(user_personal_info_frame)
address = tk.Entry(user_personal_info_frame)
email = tk.Entry(user_personal_info_frame)
pob = tk.Entry(user_personal_info_frame)
title = tk.Entry(user_personal_info_frame)

entries = [
    first_name, second_name, surname, age, None, dob,
    None, citizenship, blood_type, height, weight,
    tin, nid, address, email, pob, title
]

for i, entry in enumerate(entries):
    if entry:
        entry.grid(row=i, column=1)

# ================= FAMILY BACKGROUND =================
user_family_background = tk.LabelFrame(frame, text="Family Background:")
user_family_background.pack(side="left", padx=10, pady=10)

tk.Label(user_family_background, text="Father's Name").grid(row=0, column=0)
tk.Label(user_family_background, text="Mother's Name").grid(row=1, column=0)
tk.Label(user_family_background, text="Spouse Name").grid(row=2, column=0)
tk.Label(user_family_background, text="Occupation").grid(row=3, column=0)
tk.Label(user_family_background, text="Work Address").grid(row=4, column=0)
tk.Label(user_family_background, text="No. of Children").grid(row=5, column=0)

father = tk.Entry(user_family_background)
mother = tk.Entry(user_family_background)
spouse = tk.Entry(user_family_background)
occupation = tk.Entry(user_family_background)
work_address = tk.Entry(user_family_background)
children = tk.Spinbox(user_family_background, from_=0, to=20)

family_entries = [father, mother, spouse, occupation, work_address, children]

for i, entry in enumerate(family_entries):
    entry.grid(row=i, column=1)

# ================= EDUCATIONAL BACKGROUND =================
user_educational_background = tk.LabelFrame(frame, text="Educational Background:")
user_educational_background.pack(side="left", padx=10, pady=10)

headers = ["Level", "School", "Course", "From", "To", "Achievements"]
for col, header in enumerate(headers):
    tk.Label(user_educational_background, text=header).grid(row=0, column=col)

levels = ["Nursery", "Primary", "O-Level", "A-Level", "University"]
education_entries = {}

for row, level in enumerate(levels, start=1):
    tk.Label(user_educational_background, text=level).grid(row=row, column=0)
    school = tk.Entry(user_educational_background)
    course = tk.Entry(user_educational_background)
    year_from = tk.Entry(user_educational_background, width=6)
    year_to = tk.Entry(user_educational_background, width=6)
    achievement = tk.Entry(user_educational_background)

    school.grid(row=row, column=1)
    course.grid(row=row, column=2)
    year_from.grid(row=row, column=3)
    year_to.grid(row=row, column=4)
    achievement.grid(row=row, column=5)

    education_entries[level] = (school, course, year_from, year_to, achievement)

# ================= SUBMIT FUNCTION =================
def submit_form():
    data = {
        "First Name": first_name.get(),
        "Surname": surname.get(),
        "Gender": gender.get(),
        "DOB": dob.get(),
        "Email": email.get(),
        "Father": father.get(),
        "Mother": mother.get()
    }

    print("\n--- REGISTRATION DATA ---")
    for k, v in data.items():
        print(f"{k}: {v}")

    messagebox.showinfo("Success", "Form submitted successfully!")

# ================= SUBMIT BUTTON =================
submit_btn = tk.Button(window, text="Submit Form", command=submit_form, bg="green", fg="white")
submit_btn.pack(pady=10)

window.mainloop()
