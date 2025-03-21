https://www.programiz.com/online-compiler/9qbtjU4l05TrB


###SOLID PATTERN CODE

row=int(input("enter the input/row value:"))
#row=3
##upper pyramid
m=2*row-2
for i in range(0,row):
    asci=65  ## ASCII value of alphabet A
    for j in range(0,m): ###print space
        print(end=" ") 
    for j in range(0,i):  ## prints a,b,c in each row
        print(chr(asci),end=" ")  ##chr(asci) converts into alphabet
        asci+=1   
    m=m-1
    print(" ") 
    
##lower pyramid
m=row-2
for i in range(row,-1,-1):
    asci=65
    for j in range(0,m): ###print space
        print(end=" ") 
    for j in range(0,i):  ## print chara
        print(chr(asci),end=" ")
        asci+=1
    m=m+1
    print(" ")
