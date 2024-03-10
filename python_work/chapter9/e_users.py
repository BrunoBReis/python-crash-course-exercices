class User:
    """Creating a user"""

    def __init__(self, first_name:str, last_name:str):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        # Default Value
        self.logging_atempts = 0

    def describe_user(self):
        """Shows attributes"""
        return f"{self.first_name} {self.last_name}"

    def greet_user(self):
        """Greeting user"""
        print(f"Welcome {self.describe_user()}")
    
    def increment_login_attempts(self):
        """Increment loggin attempts by 1"""
        self.logging_atempts += 1

    def reset_loggin_attempts(self):
        self.logging_atempts = 0




user = User('bruno', 'braganca')

user.describe_user()
user.greet_user()

for times in range(10):
    user.increment_login_attempts()

print(user.logging_atempts)
user.reset_loggin_attempts()
print(user.logging_atempts)
