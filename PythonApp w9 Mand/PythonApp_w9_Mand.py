#Christmas

#define lists
nameList    = []
presentList = []
priceList   = []


#methods 
def getNumber():
    #number of people to buy presents for
    numPeople = int(input("Enter Number of people "))
    return numPeople
#end getNumber

def fillLists(numPeople):
    for i in range(numPeople):
        name = input("Enter Name : ")
        nameList.append(name)
        present = input("Enter Present ")
        presentList.append(present)
        price = float(input("Enter Price "))
        priceList.append(price)
    #end for
    return nameList, presentList, priceList

def findMin(priceList):
    #read through the list and find 
    minPrice = None
    position = None
    if len(priceList) > 0:
        minPrice = priceList[0]  # Price = first item in list
        for item in priceList:
            if minPrice > item:
                minPrice = item
                position = priceList.index(item) # get index value
            #end if
        #end for
    #end if

    #print min
    print ("Minimum price is £ ", minPrice)
    return 
#end findMin

def findMax(priceList):
    #read through the list and find max
    maxPrice = None
    position = None
    if len(priceList) > 0:
        maxPrice = priceList[0]  # Price = first item in list
        for item in priceList:
            if maxPrice > item:
                maxPrice = item
                position = priceList.index(item) # get index value
    #print max
    print ("Maximum price is £ ", maxPrice)
    return 
#end findMin

##TO DO
##At a loss for this one so its commented till later
def itemCount(presentList)
occurence = 0
itemCheck = input("Enter Item to be counted")


Line 1 SET occurrence TO 0

Line 2 RECEIVE desired_value FROM KEYBOARD

Line 3 FOR counter FROM 0 TO list length DO

Line 4 IF list [counter] = desired_value THEN

Line 5 SET occurrence TO occurrence + 1

Line 6 PRINT a message to screen with occurrences of desired_value 

#read through the present list and count for this find item
    #return 
#end findMin


#main program

numPeople = getNumber()
nameList, presentList, priceList = fillLists(numPeople)

findMin(priceList)
findMax(priceList)
#itemCount(presentList)


print(nameList)
print(presentList)
print(priceList)

