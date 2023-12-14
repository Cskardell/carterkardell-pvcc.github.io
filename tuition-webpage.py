# Name: Carter+ Trey
# Program Purpose: This program computes PVCC college tuition and fees based on the number of credits
# PVCC Fee Rates are from https://www.pvcc.edu/tuition-and-fees

import datetime

# Define tuition and fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 366.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# Define global variables
inout = 1  # 1 means in state, 2 means out of state
num_credits = 0
scholarshipamt = 0
tuition_amount = 0
total_amount = 0
balance_owed = 0
cap_fee = 0
inst_fee = 0
activity_fee = 0

outfile = 'tuitionwebpage.html'

# Define program function
def get_user_data():
    global inout, num_credits, scholarshipamt
    inout = int(input("Enter 1 for IN-STATE; Enter 2 for OUT-OF-STATE: "))
    num_credits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def main():
    open_outfile()

    more = True
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        yesno = input("\nWould you like to calculate tuition and fees for another student (Y or N)? ")
        if yesno.lower() == "n":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition Calculator </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-tuitionbackground.webp); color: #f8dd61;">\n')

def perform_calculations():
    global inout, num_credits, scholarshipamt, tuition_amount, total_amount, cap_fee, activity_fee, balance_owed, inst_fee, RATE_ACTIVITY_FEE, RATE_CAPITAL_FEE, RATE_INSTITUTION_FEE, RATE_TUITION_IN, RATE_TUITION_OUT
    if inout == 1:
        tuition_amount = RATE_TUITION_IN * num_credits
        cap_fee = 0
    else:
        tuition_amount = RATE_TUITION_OUT * num_credits
        cap_fee = num_credits * RATE_CAPITAL_FEE

    inst_fee = num_credits * RATE_INSTITUTION_FEE
    activity_fee = num_credits * RATE_ACTIVITY_FEE
    total_amount = tuition_amount + cap_fee + inst_fee + activity_fee
    balance_owed = total_amount - scholarshipamt

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #47161a;  font-family: arial; margin: auto;">\n')
    f.write(colsp + '\n')
    f.write('<h2>PVCC TUITION CALCULATION</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Central Virginias Community College ***\n')

    f.write(tr + 'Tuition Amount' + endtd + format(tuition_amount, currency) + endtd +
            tr + 'Cap Fee Amount' + endtd + format(cap_fee, currency) + endtd +
            tr + 'Activity Amount' + endtd + format(activity_fee, currency) + endtd +
            tr + 'Inst. Amount' + endtd + format(inst_fee, currency) + endtd +
            tr + 'Total Amount' + endtd + format(total_amount, currency) + endtd +
            tr + 'Scholarship Amount' + endtd + format(scholarshipamt, currency) + endtd +
            tr + 'Balance Owed' + endtd + format(balance_owed, currency) + endtd +
            colsp + 'Date/Time: ' + day_time + endtr)
    f.write('</table><br />')

main()
