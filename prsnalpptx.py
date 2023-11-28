import datetime

# define tax rates
PTT_RATE = 0.042
RELIEF_RATE = 0.33

# create list data
vehicle = ["2019 Volvo", "2018 Toyota", "2022 Kia", "2020 Ford", "2023 Honda", "2019 Lexus "]
vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]
pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y"]
owner_name = ["Brand, Debra", "Smith, Carter", "Johnson, Bradley", "Garcia, Jennifer", "Henderson, Leticia", "White, Danielle"]
ppt_owed = []
num_vehicles = len(vehicle)
total = 0

def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total
    total = 0  # initialize total
    for i in range(num_vehicles):
        tax_due = (vehicle_value[i] * PTT_RATE) / 2
        if pptr_eligible[i].upper() == "Y":
            tax_due = tax_due * 0.67
        ppt_owed.append(tax_due)
        total += tax_due

def display_results():
    moneyf = '8,.2f'
    line = "__________________________________________________________________________"
    tab = "\t"

    print(line)
    print("************PERSONAL PROPERTY TAX REPORT************")
    print("                 Charlottesville, Virginia ")
    print("\n\t\tRUN DATE/TIME:", str(datetime.datetime.now()))
    print("\nNAME" + tab + tab + tab + "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab + " TAX DUE")
    print(line)

    for i in range(num_vehicles):
        dataline1 = owner_name[i] + tab + vehicle[i] + tab + format(vehicle_value[i], moneyf) + tab
        dataline2 = pptr_eligible[i] + tab + format(ppt_owed[i], moneyf)
        print(dataline1 + dataline2)
        print(line)

    print("************ TOTAL TAX DUE:" + tab + format(total, moneyf))

main()
