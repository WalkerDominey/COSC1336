# COSC1336
#This program is to compute sum and deviation of test scores
#Walker Dominey
#Fundamentals of Programming COSC 1336 Python
#ACC FALL 2018
#lab4framework.py
#Professor Onabajo
#Global Variable
N=20
def main():
    #file declaration
    infile.open
    outfile.open
    #array declaration
    x=[0]*20
    dev=[0]*20
    dev1=[0]*20
    sd1=[0]*20
    #variable declaration
    sumx=0
    xbar=0
    dev2=0
    std=0
    sd2=0
    #call functions
    loaddata(infile,x)
    sumx=loaddata(infile,x)
    #compute average
    xbar=sumx/n
    #call deviation
    dev2=deviation(x,dev,dev1,xbar)
    #compute standard deviation
    std=sqrt((dev2)/n)
    #compute standard score
    sd2=standard(dev,sd1,std)
    #output result
    outdata(outfile,x,dev,dev1,sd1)
    #print rest of data
    print('sum=',sumx)
    outfile.write('sum=',str(sumx))
    xbar
    dev2
    sd2
    std

def loaddata(file,a)
    #local variable
    k=0
    x=0
    for k in range(n):
        templist(file.readline().strip('\n'))
        a[k]=int(templist)
        x=x+a[k]
    return(k)

def deviation(A,B,C,d)
    #local variable
    k=0
    x=0
    for k in range(n)
        B[k]=d-A[k]
        C[k]=B[k]*B[k]
        x=x+C[k]
    return(x)

def standard(

def outdata(
    
