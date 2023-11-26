# Name: Carter Kardell
# Program Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# Note: Pet medications prescribed by licensed vets are not subject to sales tax in Virginia
#
# Pet CARE MEDS Pricing 
#----------------------------------
# Canine Vaccines:
# 1. Bordatella 30.00
# 2. DAPP 35.00
# Influenza 48.00
# Leptospirosis 21.00
# Lyme Disease 41.00
# Rabies 25.00
# Full Vaccine Package (include all vaccines): 15% discount

# Canine Heartworm Preventative Chews (price per chew; one chew per month)
    # Small dogs: up to 25lbs: 9.99
    # Medium-sized dogs: 26-50lbs: 11.99
    # Large dogs: 51 to 100lbs 13.99

import datetime

### Define Global Variables ###
# define dog prices #
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

## CAT PRICES ##
PR_FLLK=35
PR_FLVR=30
PR_FRB=25

PR_CAT_CHEW=8


# Define global variables

#### Define Program Functions ####

def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
        ask_again = input("\nWould you like to process another pet (Y/N)")
        if ask_again.upper() == "N":
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet Name:")
    pet_type = input("Is this pet a dog (D) or a cat (C)?")
    pet_weight = int(input("Weight of your pet (in pounds):"))

### Dog Functions ###

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.influenza \n\t4.leptospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.NONE"
    dog_menu = dog1 + dog2
    pet_vax_type = int(input("Enter the number corresponding to the desired vaccine:" ))
    num_chews = int(input("How many heartworm chews would you like to order?"))

def perform_dog_calculations():
    global vax_cost, vax_name, chews_cost, total
    ### Vaccines ###
    if pet_vax_type == 1:
        vax_cost = PR_BORD
        vax_name = "Bordatella"
    elif pet_vax_type == 2:
        vax_cost = PR_DAPP
        vax_name = "DAPP"
    elif pet_vax_type == 3:
        vax_cost = PR_FLU
        vax_name = "Influenza"
    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU
        vax_cost = 0.85 * PR_ALL
        vax_name = "Full Vaccine Package"

    ### Heart Worm Chews ###
    if num_chews != 0:
        if pet_weight < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL
        elif 26 <= pet_weight < 50:
            chews_cost = num_chews * PR_CHEWS_MED
        else:
            chews_cost = num_chews * PR_CHEWS_LARGE
    else:
        chews_cost = 0

    ### Total ###
    total = vax_cost + chews_cost

def display_dog_results():
    moneyf = "15,.2f"
    line = "-------------------------"
    print(line)
    print('***** PET CARE MEDS *******')
    print(line)
    print('Vaccine Type   $' + format(vax_name))
    print('Vaccine Cost   $' + format(vax_cost, moneyf))
    print('Chew Cost      $' + format(chews_cost, moneyf))
    print('Total Amount   $' + format(total, moneyf))
    print(line)
    print(str(datetime.datetime.now())) 
# Call the main function to run the programJ



###### Cat FUNCTIONS ######

def get_cat_data ():
    global pet_vax_type, num_chews
    cat1 = "\n** Cat Vaccines: \n\t1.Feline Leukemia \n\t2.Feline Viral Rhinotracheitis \n\t3. Rabies"
    cat2 = "\n\t5. Full Vaccinne Package \n\t6.NONE"
    cat_menu = cat1 + cat2
    pet_vax_type = int(input("Enter the number corresponding to the desired vaccine:" ))
    num_chews = int(input("How many heartworm chews would you like to order?"))

def perform_cat_calculations():
    global vax_cost, vax_name, chews_cost, total 
    if pet_vax_type == 1:
        vax_cost = PR_FLLK
        vax_name = "Feline Leukemia"
    elif pet_vax_type == 2:
        vax_cost = PR_FLVR
        vax_name = "Feline"
    elif pet_vax_type == 3:
        vax_cost = PR_FRB
        vax_name = "Rabies"
    else:
        PR_ALL = PR_FLLK + PR_FLVR + PR_FRB
        vax_cost = 0.90 * PR_ALL
        vax_name = "Full Vaccine Package"

    if num_chews != 0:
            chews_cost= num_chews*PR_CAT_CHEW
    else:
        chews_cost = 0
    total=vax_cost+chews_cost
def display_cat_results():
    moneyf = "15,.2f"
    line = "-------------------------"
    print(line)
    print('***** PET CARE MEDS *******')
    print(line)
    print('Vaccine Type   $' + format(vax_name))
    print('Vaccine Cost   $' + format(vax_cost, moneyf))
    print('Chew Cost      $' + format(chews_cost, moneyf))
    print('Total Amount   $' + format(total, moneyf))
    print(line)
    print(str(datetime.datetime.now())) 
 
main()
