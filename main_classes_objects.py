from curses import ACS_GEQUAL


class Student:
    # [assignment] Skeleton class. Add your code here
    #the attributes
    Name = "";
    int Age=0;
    Tracks = [];
    float Score =0.00;

    #init self for the attributes
    def __init__(self,Name, Age, Tracks,Score):
        self.Name = Name
        self.Age = Age
        self.Tracks = Tracks
        self.Score = Score
    
    #the methods
    def change_name(self, who):
        self.Name=who
    
    def change_age(self, number):
        if type(number) =='int':
            self.Age = number
        else:
            print('enter an integer')
    
    
    def Add_track(self, new_track):
        #Tracks= input("Enter new track")
        self.Tracks += new_track
    
    def get_score(self, score):
        return self.score

    
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
