from io import BufferedReader
from mimetypes import init
from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
       def __init__(self, name, age, tracks, score):
           self.name=name
           self.age=age
           self.tracks=tracks
           self.score=score
           print('Name:',name,'\n','Age:', age,'\n','Track:', tracks,'\n','Score:', score)
           
       def change_name(self,name):
           print('\n','Name: ',name)
           
       def change_age(self, age):
           print('Age: ',int(age))
           
       def add_track(self, tracks):
           print('Tracks: ',tracks)
           
       def get_score(self, score):
           print('Score: ',score)
           

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(65)
