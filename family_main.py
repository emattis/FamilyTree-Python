from person import person
import sys
import os

person1,person2,person3 = "","",""
createdPeople=[]

file= ""
def family_tree(filename):
    global file #declares file to be a global variable
    file = open(filename,'r')


if __name__ == '__main__':
    temp = sys.argv[-1]
    if temp[-4:] in  ".txt":
        family_tree(sys.argv[-1])

    

def isCreated(person):
    if person in createdPeople:
        return
    else:
        createdPeople.append(person)
        
def getPerson(name):
    for person in createdPeople:
        if person.getName() in name:
            return person
        
    return False

#family_tree("familytree.txt")

def printList(thelist):
    for element in thelist:
        print (str(element)+"")



for line in file:

    text = line.split()
    
    if text[0] is 'E':
        if getPerson(text[1]) is not False:
            person1 = getPerson(text[1])
        else:
            person1 = person(text[1])
            
        if getPerson(text[2]) is not False:
            person2 = getPerson(text[2])
        else:
            person2 = person(text[2])
            
        if text[3]:
            if getPerson(text[3]) is not False:
                person3 = getPerson(text[3])
            else:
                person3 = person(text[3])
                
            person1.setSpouse(person2)
            person1.addChild(person3)
            isCreated(person1)
            isCreated(person2)
            isCreated(person3)

        else:
            person1.setSpouse(person2)
            isCreated(person1)
            isCreated(person2)
        

    if text[0] is 'W':
        print("\n"+' '.join(text))
        
        if text[1] in "parent":
            if getPerson(text[2]) is not False:
                person1 = getPerson(text[2])
                
            else:
                person1 = person(text[2])
                isCreated(person1)
                
            printList(person1.getParents())
            
        elif text[1] in "relative":
            if getPerson(text[2]) is not False:
                person1 = getPerson(text[2])
            else:
                person1 = person(text[2])
                isCreated(person1)
                
            printList(person1.getRelatives(createdPeople))
            
        elif text[1] in "unrelated":
            if getPerson(text[2]) is not False:
                person1 = getPerson(text[2])
            else:
                person1 = person(text[2])
                isCreated(person1)

            printList(person1.getUnrelated(createdPeople))
            
        elif text[1] in "sibling":
            if getPerson(text[2]) is not False:
                person1 = getPerson(text[2])
                
            else:
                person1 = person(text[2])
                isCreated(person1)
                
            printList(person1.getSiblings())
            
        elif text[1] in  "ancestor":
            if getPerson(text[2]) is not False:
                person1 = getPerson(text[2])
                
            else:
                person1 = person(text[2])
                isCreated(person1)
                
            printList(person1.getAncestors())
            

    if text[0] is 'X':
        print("\n"+' '.join(text))
        
        if text[2] in "relative":
            if getPerson(text[1]) is not False:
                person1 = getPerson(text[1])
            else:
                person1 = person(text[1])
                isCreated(person1)

            if getPerson(text[3]) is not False:
                person2 = getPerson(text[3])
            else:
                person2 = person(text[3])
                isCreated(person2)

            person1.isARelative(person2)


        if text[2] in "sibling":
            if getPerson(text[1]) is not False:
                person1 = getPerson(text[1])
            else:
                person1 = person(text[1])
                isCreated(person1)

            if getPerson(text[3]) is not False:
                person2 = getPerson(text[3])
            else:
                person2 = person(text[3])
                isCreated(person2)

            person1.isASibling(person2)


        if text[2] in "spouse":
            if getPerson(text[1]) is not False:
                person1 = getPerson(text[1])
            else:
                person1 = person(text[1])
                isCreated(person1)

            if getPerson(text[3]) is not False:
                person2 = getPerson(text[3])
            else:
                person2 = person(text[3])
                isCreated(person2)
                

            person1.isASpouse(person2)


        if text[2] in "parent":
            if getPerson(text[1]) is not False:
                person1 = getPerson(text[1])
            else:
                person1 = person(text[1])
                isCreated(person1)

            if getPerson(text[3]) is not False:
                person2 = getPerson(text[3])
            else:
                person2 = person(text[3])
                isCreated(person2)

            person1.isAParent(person2)


        if text[2] in "unrelated":
            if getPerson(text[1]) is not False:
                person1 = getPerson(text[1])
            else:
                person1 = person(text[1])
                isCreated(person1)

            if getPerson(text[3]) is not False:
                person2 = getPerson(text[3])
            else:
                person2 = person(text[3])
                isCreated(person2)

            person1.isUnrelated(person2)


        if text[2] in "ancestor":
            if getPerson(text[1]) is not False:
                person1 = getPerson(text[1])
            else:
                person1 = person(text[1])
                isCreated(person1)

            if getPerson(text[3]) is not False:
                person2 = getPerson(text[3])
            else:
                person2 = person(text[3])
                isCreated(person2)

            person1.isAnAncestor(person2)
            

    if text[0] is "R":
        print("\n"+' '.join(text))
        
        if getPerson(text[1]) is not False:
            person1 = getPerson(text[1])
        else:
            person1 = person(text[1])
            isCreated(person1)
            

        if getPerson(text[2]) is not False:
            person2 = getPerson(text[2])
        else:
            person2 = person(text[2])
            isCreated(person2)
            

        print(person1.findClosestRelationship(person2))
        
        

        
            
            

    
            
            
            
