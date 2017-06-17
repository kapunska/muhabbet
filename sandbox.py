height = int(input("enter the sandbox height: "))

width = int(input("enter the sandbox width: "))

#creates the matrix with the given height and width.
Matrix = [[0 for i in range(width)] for j in range(height)]

#gets the matrix inputs from the user.
for i in range(0, height):
     for j in range(0, width):
          print ("Enter the elemnt at %d, %d: " %(i , j))
          Matrix[i][j]= int(input())

##ctr = 0
##for i in range(0, height):
##     for j in range(0, width):
##          if Matrix[i][j] > 3:
##               Matrix[i][j] -= 4
##               for k in range (4):
##                    if i-1 > 0:
##                         Matrix[i-1][j] += 1
##                    if j-1 > 0:
##                         Matrix[i][j-1] += 1
##                    if j+1 < width:
##                         Matrix[i][j+1] += 1
##                    if i+1 < height:
##                         Matrix[i+1][j] += 1
                    

                 
#prints the matrix
for i in range(height):
     for j in range(width):
          print (Matrix[i][j], end=" ")
     print("\n")
