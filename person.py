import random

class person():
    

    def __init__(self, PersonName):
        
        self.name = PersonName
        self.character = {"name":PersonName,"siblings":[],"parents":[],"currentSpouse": "","spouses":[],"children":[],"ancestors":[],"relatives":[]}

    #tostring for python
    def __repr__(self):
        return self.name
    #makes sure the object is iterable
    def __eq__(self, other):
        return self.name is other.name
    #if object is present
    def __contains__(self,other):
        return True if other == self else False
    #makes the object hashables. we need it for set
    def __hash__(self):
        return hash(str(self.name))
        
        


    def getName(self):

        return (self.name)


    def setSpouse(self,person):
        self.character['spouses'].append(person)
        self.character['currentSpouse'] = person
        person.character['spouses'].append(self)

    def getSpouse(self):
        return sorted(self.character['spouses'], key=lambda self: self.name)

    def getCurrentSpouse(self):
        return self.character['currentSpouse']

    def addChild(self,person):
        self.character['children'].append(person)
        self.getCurrentSpouse().character['children'].append(person)
        person.addParents(self)
        person.addParents(self.getCurrentSpouse())
        
        

    def getChildren(self):
        return sorted(self.character['children'], key=lambda self: self.name)

    def addParents(self,parent1):
        self.character['parents'].append(parent1)

    def getParents(self):
        return sorted(self.character['parents'], key=lambda self: self.name)

    def getSiblings(self):
        siblings =[]
        if self.getParents():
            temp =self.getParents()
            siblings = temp[0].getChildren()
            siblings.extend(temp[1].getChildren())
        if siblings:
            siblings.remove(self)
            siblings.remove(self) #two times because the person appears twice before using set
            
        return sorted(set(siblings), key=lambda self: self.name)

    def getAncestors(self):
        ancestors =[]

        if not self.getParents():
            ancestors.append(self)

        for parent in self.character['parents']:
            ancestors.append(parent)
            ancestors.extend(parent.getAncestors())

        return sorted(set(ancestors), key=lambda self: self.name)

    def getRelatives(self, createdPeople):
        relatives = []
        for person in createdPeople:
            temp = person.getAncestors()
            if any([item in self.getAncestors() for item in temp]):
                relatives.append(person)
        relatives.remove(self)
        return sorted(set(relatives), key=lambda self: self.name)

    def getUnrelated(self,createdPeople):
        unrelated =[]
        for person in createdPeople:
            temp = person.getAncestors()
            if not any([item in self.getAncestors() for item in temp]):
                unrelated.append(person)
        
        return sorted(set(unrelated), key=lambda self: self.name)

    def isASpouse(self,person):
        if person in self.getSpouse():
            print("Yes")
        else:
            print ("No")

    def isAParent(self,person):
        if self in person.getParents():
            print("Yes")
        else:
            print ("No")

    def isASibling(self,person):
        if self in person.getSiblings():
            print("Yes")
        else:
            print("No")

    def isAnAncestor(self, person):
        if self in person.getAncestors():
            print ("Yes")
        else:
            print("No")

    def isARelative(self, person):
        if any([item in self.getAncestors() for item in person.getAncestors()]):
            print("Yes")
        else:
            print("No")

    def isUnrelated(self,person):
        if any([item in self.getAncestors() for item in person.getAncestors()]):
            print("No")
        else:
            print("Yes")

    def findClosestRelationship(self,person):
        if self in person.getSpouse():
            return "Spouse"
        elif self in person.getParents():
            return "Parent"
        elif self in person.getSiblings():
            return "Sibling"
        elif self in person.getAncestors():
            return "Ancestor"
        elif any([item in self.getAncestors() for item in person.getAncestors()]):
            return "Relative"
        else:
            return "Unrelated"
        
    




        
    
