def size(n):
    return len(n)
####################################
def intersection(a,b):
    n=[]
    # sort a
    #print(a)
    a.sort()
    #print(a)
    # sort b
    #print(b)
    b.sort()
    #print(b)
    # find common
    cc=0
    for n1 in a:
        for n2 in b:
            if n1==n2:
                #print(n1," this is common")
                n.insert(cc,n1)
    # add common to n
    # return n
    return n
#########################################
def neighbours(node):
    n=[]
    #print(a, "before neighbours begin")
    for each in a:
        #print(each," Print each element in a")
        count=0
        for aa in each:
            #print(aa)
            #print(node)
            #print(each==node)
            if ((aa==node) and (count % 2 ==0)):
                #print("Neighbour of ", node," is ",each[count+1])
                n.append(each[count+1])
                #print(n)
            if ((aa==node) and (count % 2 ==1)):
                #print("Neighbour of ", node," is ",each[count-1])
                n.append(each[count-1])
                #print(n)
            count=count+1
    return n
###############################################
def check(first,second):
    # check if pair first,second exists in List a           
    flag=0
    x=-1  # x counts the position for o
    for o in a:
        x=x+1
        if ((o==first) and (x % 2 ==0)):
            if (a[x+1]==second):
                flag=1
                break            
    return flag
###########################################
##############################################
import sys
kk=int(sys.argv[2])
ff=sys.argv[1]
f = open(ff, 'r') 
cx=[]    # Copy of x
a=[]    # a Holds the entire graph
i=0     # Counts the first and second
k=0     # Counts the nu,ber of edges
# Loop over file and increment a key for each char.
for line in f.readlines():
    words=line.split()
    x=[]    # A List contains an edge
    for word in words:
        x.insert(i,int(word))
        i=i+1
    #print(x)
    i=0
    #print("I just print List x")
    cx=x
    a.insert(k,cx)
    
    k=k+1
#print(a)
#print("I just print List a")
#print("The List a has been created")
#print()
########################################
# Print character counts.
#for item in chars.items():
#    print(item)
# Create a List with unique nodes
###############################################
ff=1
while (ff==1):
    ff=0
    for hh in a:
        i=0
        a1=hh[0]
        a2=hh[1]
        #print(a1,a2,"   ---- Just read from a")
        #print(neighbours(a1))
        #print(neighbours(a2))
        #print()
        #print(intersection(neighbours(a1),neighbours(a2)),"Here we are common")
        #print(size(intersection(neighbours(a1),neighbours(a2))),"size of intersection")
        #print()        
        if (size(intersection(neighbours(a1),neighbours(a2)))<kk-2):
            #print("This edge ",a1,a2," must be removed")
            rx=[]
            rx.append(a1)
            rx.append(a2)
            #print(rx)
            #print(a)
            a.remove(rx)
            #print(a)
            ff=1
            break
        #else:
            #print("This edge ",a1,a2,"must be not removed")
            i=i+1
        if ff==1:
            #print("Just after the first break")
            break
    ###################
    #if ff==1:
     #   print("Just after the first break")
      #  print("A line has been read")
########################################################
#print(a)
######################################################################################
h=0         # Number of unique nodes
b=[]        # List of unique nodes
for hh in a:
    a1=hh[0]
    a2=hh[1]
    if len(b)==0:
        b.append(a1)
        #print(a1," has added in b")
        b.append(a2)
        #print(a2," has added in b")
    else:        
        #  check if a1 exists in b
        l=0
        flag=False
        while l<len(b) and flag==False:
            if a1==b[l]:
                #print("The number ",a1," exists in list b")
                flag=True
            l=l+1
        if flag==False:
            b.append(a1)
            #print(a1," has added in b")
        ##################################      
        #  check if a2 exists in b
        l=0
        flag=False
        while l<len(b) and flag==False:
            #print(a2)
            #print(l)
            #print(b[l])
            if a2==b[l]:
                #print("The number ",a2," exists in list b")
                flag=True
            l=l+1
        if flag==False:
            b.append(a2)
            #print(a2," has added in b")
#print(b)
b.sort()
#print(b)    
#####################################################
# find
# Εμφάνιση δικτυωμάτων
#############################
kd=[]
for hh in b:
    ed=[]               # each δικτύωμα
    ed.append(hh)
    #print(hh)
    for kk in a:
        a1=kk[0]
        a2=kk[1]
        if(a1==hh):
            ed.append(a2)
            #print(a2)
        if(a2==hh):
            ed.append(a1)
            #print(a1)
    #print(ed)
    ed.sort()
    #print(ed," a new sorted diktyo")
    # check if diktyo exists
    if ed not in kd:
        kd.append(ed)
    #print(kd)
    #print()
    kd.sort()
    #print(kd)
    
###############################
# kd must be sorted
#########################
# print
for gg in kd:
    a="("
    vv=len(gg)
    #print(vv)
    zz=0
    for ll in gg:
        a=a+str(ll)
        if (zz==vv-1):
            a=a
        else:
            a=a+","
        zz=zz+1
    a=a+")"
    print(a)
