# Method to enter new student details
def accept(self, Name, Rollno, marks1, marks2 ):
    # Creates a new class constructor
    # and pass the details
    ob = Student(Name, Rollno, marks1, marks2 )

    # list containing objects of student class
    ls.append(ob)

# Function to display student details     
def display(self, ob):
    print("Name   : ", ob.name)
    print("RollNo : ", ob.rollno)
    print("Marks1 : ", ob.m1)
    print("Marks2 : ", ob.m2)
    print("\n")    

# Search Function    
def search(self, rn):
    for i in range(ls.__len__()):
        # iterate through the list containing
        # student object and checks through
        # roll no of each object
        if(ls[i].rollno == rn):
            # returns the object with matching 
            # roll number
            return i 