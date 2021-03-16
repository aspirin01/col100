#CODE FOR Q1:
def isStrDigit(x):
    #Check if a string is number of not

    for i in range(len(x)):
        if x[i]=='0' or x[i]=='1' or x[i]=='2' or x[i]=='3' or x[i]=='4' or x[i]=='5' or x[i]=='6' or x[i]=='7' or x[i]=='8' or x[i]=='9' :
            continue
        else: 
            return False
            break
    return True
def readNumber(s,i) :
	x = i
	while (x < len(s)):
		if (isStrDigit(s[x]) or s[x] == '.') :
			x += 1
		else :
			break
	number = float(s[i:x])
	return number, x

def evalParan(s, i):
    #This function is used to evaluate the value inside a given parenthesis.
    assert s[i] =='(' and s[len(s)-1] == ')',"Operation not in parenthesis"
     #This assertion makes sure that input is within parenthesis
    if (isStrDigit(s[i + 1])) :
        a, j = readNumber(s, i + 1)
    else :
        a, j = evalParan(s, i + 1)    
    if (isStrDigit(s[j + 1])) :
        b, k = readNumber(s, j + 1)
    else :
        b, k = evalParan(s, j + 1)
    assert s[j]!= '('or s[j]!= ')',"Invalid operation defined"
    if (s[j] == '+') :
        ans = a + b
    elif (s[j] == '-') :
        ans = a - b
    elif (s[j] == '*') :
        ans = a * b 
    elif (s[j] == '/') :
        ans = a / b

    return ans, k + 1

def evaluate (s) :
    # Function here gives the evaluated value after all the calculations above.
	if (s[0] != ')' or s[len(s) - 1] != ')' ) :
		s = '(' + s + ')'
	x, y = evalParan(s, 0)
	return x


print(evaluate("1+1"))
print(evaluate("(((2*3)*4)*5)+99"))
print(evaluate("1+(((123*3)-69)/100)"))




#CODE FOR Q2

def  sumSequence(n):
    arr = [1,2]
    k = arr[-1]+1
    # Outermost loop runs till length of array < n but when length is n-1 we append another k then it becomes n and loop finishes.
    while len(arr)<n :
        assert len(arr)<n,"Limit over"
        count =0
        #Initially count of possiible combinations to give k is 0.
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                assert k > arr[i] and k > arr[j],"Not possible"
                if arr[i]+ arr[j]==k:
                    count+=1  
                if count>1:
                    break
        if count==1:
            #Since the count is 1, k appended, and we can represent k as a unique combination of two elements, else k=k+1.
            arr.append(k)
        k+=1
    print(arr)
sumSequence(50)



#CODE FOR Q3
def minLength(A,n):
    k = len(A)
    #Initial min length is set to len(A)+1, because we do not know that even if we add all the elements, we get a val > n
    length = len(A)+1
    for i in range(len(A)):
        if A[i]>n:
            return 1    
        val = A[i]
        for j in range(i+1,len(A)):
            val+=A[j]
            if j-i+1 < length and val > n:
                length= j-i+1
    if length<=len(A):
        return length  
    else:
        return -1
print(minLength([0,1,1,0], 2))
print(minLength([3,-1,4,-2,-7,2], 4))   
print(minLength([4,5,8,2,-1,3], 9) )



#CODE FOR Q4


def mergeContacts(arr):
    #Changing a tupled list to list of list [(),()]->[[],[]]
    def tupleToList(arr):
        ans=[]
        for i in range(len(arr)):
            ans.append(list(arr[i]))
        return ans
    #'a' is the list of list form of tupled list arr
    a= tupleToList(arr)
    #'ks' is an empty list which gets updated with the first element of all elements in 'a' as the loop proceeds
    ks = []
    for i in range(len(a)):
        ks.append((a[i][0]))
    #'ls' is a sublist of 'ks' which doesn't contain all elements in 'ks' without repetition
    ls=[]
    for i in ks:
        if i not in ls:
            ls.append(i)
    #'xs' is a list which will have all the email addresses corresponding to the same name correctly merged
    xs=[]
    i=0
    while len(a)!=0 and i <len(a) :
        j=i+1
        ys = []
        ys.append(a[i][1])
        while j <len(a):
            if a[i][0]==a[j][0] and j <len(a):
                ys.append(a[j][1])
                a.pop(j)
            j+=1
        xs.append(ys)
        i+=1
    #combining 'ls' and 'xs' with proper ordering kept fixed
    def listToTupledList(l1, l2): 
        return list(map(lambda x, y:(x,y), l1, l2)) 
    ans = listToTupledList(ls,xs)
    return ans
arr =[("RN","narain@cse"), ("HS","saran@cse"), ("RN","Rahul.Narain@iitd"),("HS","saran@cse.iitd"),("RN","Rahul.Narain@cse.iitd")]
print(mergeContacts(arr))