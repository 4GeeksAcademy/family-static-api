from random import randint
"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })

        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })
        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    # This method generates a unique incremental ID
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        #si no tiene id, se genera
        if "id" not in member:
            member["id"] = self._generate_id()
        
        # Forzamos que el apellido sea siempre el de la familia
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        # Buscar y eliminar
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return True # Retornamos True si se borró
        return False # False si no existía

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members