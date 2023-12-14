#Name: your name here
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emeraldata.csv"
outfile = "emeraldwebpage.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                subtotal= ROOM_RATES[1]*num_nights

            else:
                 subtotal= ROOM_RATES[2]*num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS        
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total =  subtotal+salestax+occupancy
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
           
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)



def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title style="color:#FFFFFF:"> Emerald Beach Hotel & Resort</title>\n')
    f.write('<style> td{text-align: right;} </style>\n')
    f.write('</head>\n')
    f.write('<body style="background-image:url(beachpxe.jpg); height: 100%;">\n')
    f.write('<table style="margin: auto">')
    f.write('<h1 style="text-align: center; background-color:#211f20;color:FFFFFF"> Emerald Hotel </h1>')
    f.write(' </table>')
def create_output_html():
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'

    f.write('<table style="background-color:#211f20; color:#FFFFFF; margin:auto;" border="1">\n')
    f.write('<tr><th colspan="8">Report Printed: ' + day_time + '</th></tr>\n')
    f.write('<tr><th>Name Last</th><th>Name First</th><th>Room Type</th><th>Nights</th><th>Subtotal</th><th>Sales Tax</th><th>Occupancy Tax</th><th>Total</th></tr>\n')

    for i in range(len(guest)):
        f.write(tr + guest[i][0] + td + guest[i][1] + td + guest[i][2] + td + guest[i][3] + td)
        f.write(format(guest[i][4], currency) + td)
        f.write(format(guest[i][5], currency) + td)
        f.write(format(guest[i][6], currency) + td)
        f.write(format(guest[i][7], currency) + endtr)
    
    f.write('</table><br />')
    f.write('<table style="background-color:#211f20; color:#FFFFFF; margin:auto;" border="1">\n')
    f.write('<tr><th colspan="7">Grand Total</th><td>' + format(grandtotal, ',.2f') + '</td></tr>\n')
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

main()
