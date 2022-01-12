# Magic Square is that kind of square in which sum of each row, sum
#  of each column and sum of both the diagonals is equal.
# You have to write this program that takes a nested list as input and 
# checks whether it is a magic square or not?
# This is a magic square because,

a = [[8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]]
row1=0
row2=0
row3=0    
i=0
while i<len(a):
    j=0
    while(j<len(a[i])):
        if(i==0):
            row1=row1+a[i][j]
        elif(i==1):
            row2=row2+a[i][j]
        else:
            row3=row3+a[i][j]
        j=j+1
    i=i+1
if(row1==row2==row3):
    f=0
else:
    f=1        
print("RoW 1:-",row1)
print("Row 2:-",row2) 
print("Row 3:-",row3) 
colum1=0
colum2=0
colum3=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if(j==0):
            colum1=colum1+a[i][j]
        elif(j==1):
            colum2=colum2+a[i][j]
        else:
            colum3=colum3+a[i][j]
        j=j+1
    i=i+1
if(colum1==colum2==colum3):
    f=0
else:
    f=1        
print("colum 1:-",colum1)
print("colum 2:-",colum2)
print("colum 3:-",colum3) 
daigonal1=0
daigonal2=0 
i=0
while i<len(a):
    j=0
    while(j<len(a[i])):
        if(i==j):
            daigonal1=daigonal1+a[i][j]
        if(i+j==3-1):
            daigonal2=daigonal2+a[i][j]
        j=j+1
    i=i+1
if(daigonal1==daigonal2):
    f=0
else:
    f=1        
print("Diagonal 1:-",daigonal1)
print("Diagonal 2:-",daigonal2)   
if(f==0):
    print("It's a Magic Square.")
else:
    print("It's not a Magic Square.")                 
