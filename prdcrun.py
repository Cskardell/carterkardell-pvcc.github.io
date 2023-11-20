# Name: Carter Kardell
# Prog Purpose: This program creates a payroll report
import datetime
from traceback import print_tb
############## LISTS of data ############
emp = [
"Smith, James ",
"Johnson, Patricia",
"Williams, John ",
"Brown, Michael ",
"Jones, Elizabeth ",
"Garcia, Brian ",
"Miller, Deborah ",
"Davis, Timothy ",
"Rodriguez, Ronald",
"Martinez, Karen ",
"Hernandez, Lisa ",
"Lopez, Nancy ",
"Gonzales, Betty ",
"Wilson, Sandra ",
"Anderson, Margie ",
"Thomas, Daniel ",
"Taylor, Steven ",
"Moore, Andrew ",
"Jackson, Donna ",
"Martin, Yolanda ",
"Lee, Carolina ",
"Perez, Kevin ",
"Thompson, Brian ",
"White, Deborah ",]
job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
"C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]
hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
28, 31, 37, 32, 36, 22, 28, 29, 21, 31]
num_emps = len(emp)

###### NEW Lists for calculated amounts ######
gross_pay=[]
fed_tax=[]
state_tax=[]
soc_sec=[]
medicare=[]
net_pay=[]

total_gross=0
total_net=0

###### TUPLES of Constants ######
#           C     S     J      M 
PAY_RATE= (16.50,15.75,15.75,19.30)

#         fed  st   ss  med   rt
DED_RATE=(.12,.03,.062,.0145,.04)

###### Define Program Functions ######
def main():
    perform_calculations()
    display_results()

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
def display_results():
    currency = '8.2f'
    line = '____________________'
    tab = "\t"

    print(line)
    print("********** FRESH FOODS MARKET *********")
    print("---------- WEEKLY PAYROLL ----------")
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "EMP NAME" + tab + "CODE" + tab + "GROSS" + tab
    titles2 = "FED INC TAX" + tab + "STATE INC TAX" + tab + "SOC SEC" + tab + "MEDICARE" + tab + "NET"
    print(titles1 + titles2)

    for i in range(num_emps):
        data = emp[i] + " " + job[i] + format(gross_pay[i], currency)
        print (data)
        print(line)
        print("*************** TOTAL GROSS: $" + format(total_gross, currency))
        print("*************** TOTAL NET: $" + format(total_net, currency))
        print(line)
main()
