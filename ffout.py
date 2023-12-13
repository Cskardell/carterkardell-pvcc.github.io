import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia ",
    "Williams, John    ",
    "Brown, Michael    ",
    "Jones, Elizabeth  ",
    "Garcia, Brian     ",
    "Miller, Deborah   ",
    "Davis, Timothy    ",
    "Rodriguez, Ronald ",
    "Martinez, Karen   ",
    "Hernandez, Lisa   ",
    "Lopez, Nancy      ",
    "Gonzales, Betty   ",
    "Wilson, Sandra    ",
    "Anderson, Margie  ",
    "Thomas, Daniel    ",
    "Taylor, Steven    ",
    "Moore, Andrew     ",
    "Jackson, Donna    ",
    "Martin, Yolanda   ",
    "Lee, Carolina     ",
    "Perez, Kevin      ",
    "Thompson, Brian   ",
    "White, Deborah    ",
]
job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S", "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]
hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38, 28, 31, 37, 32, 36, 22, 28, 29, 21, 31]
num_emps = len(emp)

###### NEW Lists for calculated amounts ######
gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
net_pay = []

total_gross = 0
total_net = 0

###### TUPLES of Constants ######
# C S J M
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

# fed st ss med rt
DED_RATE = (0.12, 0.03, 0.062, 0.0145, 0.04)

###### Define Program Functions ######
def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):
        # Calculate Gross Pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]

        # Calculate Deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        sclsc = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        retmt = pay * DED_RATE[4]

        net = pay - fed - state - sclsc - med - retmt

        total_gross += pay
        total_net += net

        # Append to Lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(sclsc)
        medicare.append(med)
        net_pay.append(net)

def create_output_file():
    currency = '8.2f'
    line = '__________________________________________________________________________________________________________________'
    tab = "\t"
    ## Output file ##
    out_file = "payroll.txt"
    with open(out_file, "w") as f:
        f.write(line + "\n********** FRESH FOODS MARKET *********\n---------- WEEKLY PAYROLL ----------\n+tab" + str(datetime.datetime.now()) + line)
        titles1 = "\nEMP NAME" + tab + "CODE" + tab + "GROSS" + tab
        titles2 = (
                "FED INC TAX" + tab + "STATE INC TAX" + tab + "SOC SEC"
                + tab + "MEDICARE" + tab + "NET"
        )
        f.write(titles1 + titles2)

        for i in range(num_emps):
            data = emp[i] + tab + job[i] + tab + format(gross_pay[i], currency) + tab
            data += format(fed_tax[i], currency) + tab + format(state_tax[i], currency) + tab
            data += format(soc_sec[i], currency) + tab + format(medicare[i], currency) + tab
            data += format(net_pay[i], currency) + tab

            f.write(data + "\n")

        f.write("\n*************** TOTAL GROSS: $" + format(total_gross, currency))
        f.write("\n*************** TOTAL NET: $" + format(total_net, currency))
        f.write(line)

    print("Open " + out_file + " to view your report")

main()