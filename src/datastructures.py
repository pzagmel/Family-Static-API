
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
   
    def __init__(self, apellido, group):
        self.last_name = apellido
        # example list of members
        self._family = []

        for member in group:
            new_member = {
                "id": self._generateId(),
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
            self._family.append(new_member)
        print(self._family)
   
    # read-only: Use this method to generate random members ID's when adding members into the list
   
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, first_name, age, lucky_numbers):
        # fill this method and update the return
         new_member = {
        "id": self._generateId(),
        "first_name": first_name,
        "last_name": self.last_name,
        "age": age,
        "lucky_numbers": lucky_numbers
    }
    self._family.append(new_member)

    pass

    def delete_member(self, id):
        # fill this method and update the return
       
    
        for member in self._family:
            if member["id"] == id:
                self._family.remove(member)
                return True
        
        return False  
        

    def get_member(self, id):
        # fill this method and update the return
        for member in self._family:
            if member["id"] == id:
                return member
         
       
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
