from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User:
   email: str
   senha: str
   is_active: bool = True
   is_anonymous: bool = False
   is_authenticated: bool = True
 
   def get_id(self):
       return self.username

database = {}
 
