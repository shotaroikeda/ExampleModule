# Turns out I had my folder hiearchy wrong, you have to put your modules
# under the folder you are running your python program

from modules.mathematics import * # You tell python to import the module
# There are many ways to import Addition. Another way is:
# "from modules import mathematics"

addition = mathematics.Addition()
# Tell the python program to use initalize addition
print addition.addfour(1,2,3,4)

# Notice how the python program does not run the "if __name__ == '__main__':"
# part!
