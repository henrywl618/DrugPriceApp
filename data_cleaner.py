import csv

forms = []
doses = []
qtys = []
drug_qtys = []

# remove duplicate entries and remove units from qtys

with open('medication_forms.csv', 'r') as form_file, open('medication_doses.csv', 'r') as dose_file , open('medication_qtys.csv', 'r') as qty_file, open('medication_form_qty.csv', 'r') as medication_qty_file:
    reader1 = csv.reader(form_file)
    reader2 = csv.reader(dose_file)
    reader3 = csv.reader(qty_file)
    reader4 = csv.reader(medication_qty_file)
    for row in reader1:
        form = row[0]
        if form != 'form' and form not in forms:
            forms.append(form)
    for row in reader2:
        dose = row[0]
        if dose != 'dose' and dose not in doses:
            doses.append(dose)
    for row in reader3:
        qty = row[0]
        qty = qty.split(" ")[0]
        if qty != 'qty' and qty not in qtys:
            qtys.append(qty)
    for row in reader4:
        qty = row[2]
        qty = qty.split(" ")[0]
        if qty != 'qty':
            new_row = [row[0],row[1],qty]
            drug_qtys.append(new_row)
    print(forms)
    print(len(forms))
    print(doses)
    print(len(doses))
    print(qtys)
    print(len(qtys))
    print(drug_qtys)
    print(len(drug_qtys))

with open('medication_forms (c).csv', 'w') as form_file, open('medication_doses (c).csv', 'w') as dose_file , open('medication_qtys (c).csv', 'w') as qty_file, open('medication_form_qtys (c).csv', 'w') as medication_qty_file:
    writer1 = csv.writer(form_file)
    writer2 = csv.writer(dose_file)
    writer3 = csv.writer(qty_file)
    writer4 = csv.writer(medication_qty_file)
    writer1.writerow(['form'])
    writer2.writerow(['dose'])
    writer3.writerow(['qty'])
    writer4.writerow(['name','form','qty'])

    for form in forms:
        writer1.writerow([form])
    for dose in doses:
        writer2.writerow([dose])
    for qty in qtys:
        writer3.writerow([qty])
    for row in drug_qtys:
        writer4.writerow(row)


