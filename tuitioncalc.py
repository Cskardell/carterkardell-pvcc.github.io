#Name: Carter+ Trey
# Program Purpose: This program computes PVCC college tuition and fees based on number of credits 
# PVCC Fee Rates are from https://www.pvcc.edu/tuition-and-fees

import datetime
#define tuition and fee rates#

RATE_TUITION_IN=159.61
RATE_TUITION_OUT=366.21
RATE_CAPITAL_FEE=23.50
RATE_INSTITUTION_FEE=1.75
RATE_ACTIVITY_FEE=2.90

#define global variables
inout=1 #1 means in state, 2 means out of state
num_credits=0
scholarshipamt=0
tuition_amount= 0
total_amount=0
balance_owed=0
cap_fee=0
inst_fee=0
activity_fee=0


###### define program function ######

def get_user_data():
    global inout, num_credits, scholarshipamt
    inout= int(input("Enter a 1 for IN-STATE; Enter a 2 for OUT-OF-STATE:"))
    num_credits=int(input("Number of credits registered for:"))
    scholarshipamt=float(input("Scholarship amount received:"))
           

def main ():
    more=True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno=input ("\nWould you like to calculate tuition and fees on another student (Y or N)?")
        if yesno=="n" or yesno=="N":
            another_student=False
            
    

def perform_calculations():
    global inout,num_credits,scholarshipamt,tuition_amount,total_amount,cap_fee,activity_fee,balance_owed,inst_fee,RATE_ACTIVITY_FEE,RATE_CAPITAL_FEE,RATE_INSTITUTION_FEE,RATE_TUITION_IN,RATE_TUITION_OUT
    if inout== 1:
        tuition_amount= RATE_TUITION_IN * num_credits
        cap_fee=0
    else:
        tuition_amount= RATE_TUITION_OUT * num_credits
        cap_fee= (num_credits * RATE_CAPITAL_FEE)


    inst_fee=(num_credits * RATE_INSTITUTION_FEE )
    activity_fee=(num_credits * RATE_ACTIVITY_FEE)
    total_amount = tuition_amount +cap_fee + inst_fee + activity_fee
    balance_owed= total_amount - scholarshipamt

def display_results ():
    moneyf="15,.2f"
    line= '---------------------------'
    print (line)
    print ('***** PVCC TUITION AMOUNT *******')
    print (line)
    print ('Tuition Amount $) '+ format(tuition_amount,moneyf))
    print('Cap Fee. Amount $) '+ format(cap_fee,moneyf))
    print('Activity Amount $) '+ format(activity_fee,moneyf))
    print('Inst. Amount    $) '+ format(inst_fee,moneyf))
    print('Total Amount    $) '+ format(total_amount,moneyf))
    print('Schlshp Ammount $)' + format(scholarshipamt,moneyf))
    print('Balance Owed    $) '+format(balance_owed,moneyf))

main()

