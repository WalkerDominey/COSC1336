# COSC1336

#Movie theater revenue from tickets
#Walker Dominey
#Fundamentals of Programming COSC 1336 Python
#ACC FALL 2018
#lab1.py
#Professor Onabajo
#Global Variable
def main():
    #variable declaration
    adult, children, adultprice, childrenprice= 0, 0, 6, 3
    name, gross, net, profit= ' ', 0, 0, 0
    percentage=.20
    #gets movie name
    name= input('What is the name of the movie? ')
    #gets amount of adult tickets
    adult= int(input('How many adult tickets sold? '))
    #gets amount of children tickets
    children=int (input('How many children tickets sold? '))
    #calculate profits and amount paid
    gross= float(adult*adultprice) + (children*childrenprice)
    net= float(gross*percentage)
    profit= float(gross-net)
    #output
    print('Movie Name: ',name)
    print('Adult Tickets Sold: ',adult)
    print('Children Tickets Sold: ',children)
    print('Gross Box Office Profit: ',gross)
    print('Net Box Office Profit: ',net)
    print('Amount Paid To Movie Company: ',profit)
main()
