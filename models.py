from pydantic import BaseModel
from typing import Optional, List, ClassVar
from enum import Enum
import random

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    
class SportsPlayed(str, Enum):
    basketball = "basketball"
    football = "football"
    badminton = "badminton"
    golf = "golf"
    tt = "table tennis"
    

class Student(BaseModel):
    roll_no: Optional[int] = None #roll no will be assigned automatically
    first_name: str
    last_name: str
    gender: Gender
    sports_played: Optional[List[SportsPlayed]] = None
    
    generated_ids: ClassVar[set] = set()


    def generate_unique_id(self):
        if len(self.generated_ids) >= 5:
            raise ValueError("Only 5 members are allowed in the cohort")
        while True:
            student_id = random.randint(1,5)
            if student_id not in self.generated_ids:
                self.generated_ids.add(student_id)
                return student_id
            
    def assign_roll_no(self):
        if self.roll_no is None:
            self.roll_no = self.generate_unique_id()
            
    