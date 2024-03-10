from e_users import User

class Admin(User):
    """Creating an admin"""

    def __init__(self, first_name:str, last_name:str):
        """Initialize admin"""
        super().__init__(first_name, last_name)
        # Default value
        self.privilages = Privilages()
    

class Privilages:
    """Creating privilages"""
    
    def __init__(self):
        """Initialize privilages"""
        self.privilages = ['can add post', 'can delete post',
                           'can ban user']

    def show_privilages(self):
        """Prints privilages"""
        for privilage in self.privilages:
            print(privilage)
        


admin = Admin('bruno', 'reis')
admin.privilages.show_privilages()