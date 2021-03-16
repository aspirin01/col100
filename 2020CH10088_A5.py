# Q1 Assignment 5


def gridPlay(grid):
    def minimumPenalty(cost, m, n):
        assert m >0 and n>0, "Entries not entered."
        for i in range(1,m):
            cost[i][0] += cost[i - 1][0]
        for j in range(1, n):
            cost[0][j] += cost[0][j - 1]
        for i in range(1,m):
            for j in range(1, n):
                assert cost[i][j]>= 0 ,"Negative values entered."
                # Here min() compares the minimum cost among the three possible directions.
                # INV- To reach [i][j], the minimum cost is found and added and cost[i][j] is updated.
                cost[i][j] += min(cost[i - 1][j],cost[i - 1][j - 1],cost[i][j - 1])
                # Our algorithm correctly gives the minimum cost to travel in a specific direction.
        return cost[-1][-1]
    return minimumPenalty(grid,len(grid),len(grid[0]))
grid1 = [[4, 8, 2, 4, 7, 1, 6, 2, 10]]

grid2 = [[2],[8],[9],[12],[2],[4],[1],[3]]

grid3 = [[2,4],[8,1],[9,2],[12,8],[2,1],[4,5],[1,6],[3,1]]

grid4 = [[2,4,3,1,4,2,7,8],[5,1,4,6,1,2,3,1]]

grid5 = [[8,6,2,1],[40,2,1,4],[2,3,70,5],[60,1,2,4],[7,7,75,2],[2,6,9,100],[22,2,3,1],[2,3,3,30],[2,1,2,4],[1,22,1,1]]


# Q2 Assignment 5


def stringProblem(A,B):
    vovels = ['a','e','i','o','u']
    # INV- This function gives the smallest number of changes that need to be done to convert a string A to another string B. 
    m =len(A)
    n= len(B)
    arr=[]
    for i in range(m+1):
        arr1=[]
        for j in range(n+1):
            arr1.append(0)
        arr.append(arr1)
    alphabets = "abcdefghijklmnopqrstuvwxxyz"
    for i in A:
        assert i in alphabets,"Invalid first string entered"
    for i in B:
        assert i in alphabets,"Invalid second string entered"
    assert m >=0 and n >=0, "Impossible length"
        
    for i in range(m + 1):
        for j in range( n + 1 ):

        # string one has zero character
        #insert all characters of second string
            if (i == 0): 
                arr[i][j] = j

            # when second string has 0 letters, hence to equate the two, we have to delete i elements. 
            elif (j == 0):
                arr[i][j] = i 

            # no operation needs to be performed if the digit into consideration is same in both the strings.
            elif (A[i-1] == B[j-1]):
                arr[i][j] = arr[i-1][j-1]
            else:
                
                if (B[j-1] in vovels):
                    arr[i][j]= 1 + min(arr[i][j-1],arr[i-1][j],arr[i-1][j-1])

                elif (A[i-1] in vovels):
                    #This is a corner case which includes the one in which we require to delete and insert a consonent instead of a vowel.
                    if (A[-1] in vovels):
                        arr[i][j]= 1+ min(arr[i][j-1],arr[i-1][j])
                    else:
                        # This corresponds to the case in which we have a vowel in A and a consonant in B.
                        arr[i][j]= 1 + min(arr[i][j-1],arr[i-1][j],arr[i-1][j-1])

                else:
                    arr[i][j]= 1 + min(arr[i-1][j] , arr[i][j-1] , arr[i-1][j-1])  
    return arr[m][n]


# Q3 Assignment 5


def start(y):
    if (y + ((y - 1) // 4) - ((y - 1) // 100) + ((y - 1) // 400)) % 7 == 0:
        return 6
    else: 
        return (y + ((y - 1) // 4) - ((y - 1) // 100) + ((y - 1) // 400)) % 7 -1   
def isLeap(n):
    if n%4==0 and n%100!=0:
        return True
    elif n%400==0:
        return True
    else:
        return False
def printcalendar(n):
    filex= open("calendar.txt", "w")
    filex.write(str(n).center(120)+ '\n')
    name= ["January", "February", "March", "April", "May", "June", "July","August",
           "September", "October", "November", "December"]  
    if isLeap(n):
        days = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
    a= start(n)
    spaceCount= [a]
    count = 0
    for i in range(12):
        count+=days[i]
        t=(a+count)%7
        spaceCount.append(t)
    for m in range(0,12,3):
        monthName="              "
        for i in range(m,m+3):
            monthName +='-'+str(name[i])+'-'+" "*(45-len(str(name[i])))
        weekHeadings=""
        weekHeadings+=(("M     T     w     T     F     S     S  ")+' '*8)*3   
        arr = [spaceCount[m],spaceCount[m+1],spaceCount[m+2]]
        l1,l2,l3,l4,l5,l6="","","","","",""
        for i in arr:
            for j in range(i):
                l1+=(" "*6)
            for j in range(1,8-i):
                l1+=(str(j)+" "*(6-len(str(j))))
            l1+=(" "*5)
            for j in range(8-i,15-i):
                l2+=(str(j)+" "*(6-len(str(j))))
            l2+=(" "*5)
            for j in range(15-i,22-i):
                l3+=(str(j)+" "*(6-len(str(j))))
            l3+=(" "*5)
            for j in range(22-i,29-i):
                l4+=(str(j)+" "*(6-len(str(j))))
            l4+=(" "*5)
        for i in range(3):
            for j in range(29-arr[i],36-arr[i]):
                if j<=days[m+i]:
                    l5+=(str(j)+" "*(6-len(str(j))))
                else:
                    l5+=(" "*6)
            l5+=(" "*5)
            for j in range(36-arr[i],43-arr[i]):
                if j<=days[m+i]:
                    l6+=(str(j)+" "*(6-len(str(j))))
                else:
                    l6+=(" "*6)
            l6+=(" "*5)
        filex.write(monthName+'\n' + weekHeadings+'\n')
        filex.write(l1+'\n'+ l2 +'\n'+l3+'\n'+l4+'\n'+l5+ '\n'+l6 +'\n')
    filex.close()
printcalendar(1780)
printcalendar(1900)
printcalendar(2000)
printcalendar(2145)

filex = open("calendar.txt", "r")

                                # Examples:

print(gridPlay(grid1))#44
print(gridPlay(grid2))#41
print(gridPlay(grid3))#26
print(gridPlay(grid4))#17
print(gridPlay(grid5))#35
A0 = "delhi"
B0 = "mumbai"
print(stringProblem(A0, B0))#5

A1 = "samsung"
B1 = "apple"
print(stringProblem(A1, B1))#6

A2 = "brontosaurus"
B2 = "tyrannosaurus"
print(stringProblem(A2, B2))#4

A3 = "test"
B3 = "thisdoesnothavetobeoneword"
print(stringProblem(A3, B3))#22

A4 = "supercalifragilisticexpialidocious"
B4 = "computers"
print(stringProblem(A4, B4))#30

