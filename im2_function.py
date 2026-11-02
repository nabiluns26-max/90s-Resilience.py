# 1. Import module
import greetings

greetings.greet_user("alex")


# 2. Import specific function
from greetings import greet_user

greet_user("sam")


# 3. Import function with alias
from greetings import greet_user as gu

gu("jordan")


# 4. Import module with alias
import greetings as gr

gr.greet_user("taylor")


# 5. Import all functions
from greetings import *

greet_user("casey")