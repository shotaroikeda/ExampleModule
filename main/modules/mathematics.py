# I never went over documentation, so here's a little thing for documentation
# Practices.

# You guys already know "#" creates comments. Comments are used to describe
# what a specific lines of code does

# However, good documentation does not necessarily comment every single line of
# code. You should keep comments to a minimum, but enough to describe what each
# function, loop, or whatever does.

# A good practice is to document what you think would not be obvious by reading
# code immediately.

# Here I'll document based on what I think you guys know. Usually you would not
# want to document this much.

class Addition(object):

    def addthree(self,a,b,c):
        "Adds three numbers together."
        # This line is what will show up when type --help in python
        return (a+b+c)

    def addfour(self,a,b,c,d):
        "Adds four numbers together."
        return (a+b+c+d)

    def addfive(self,a,b,c,d,e):
        "Adds five numbers together."
        return (a+b+c+d+e)


class TestClass(Addition):

    def addfour(self, a, b, c, d):
        print "adding four"
        return super(TestClass, self).addfour(a,b,c,d)
        # Do the function that Addition.addfour() was supposed to do.

    def addthree(self, a, b, c):
        return "I don't feel like adding"

    def newfunct(self):
        return "I'm a new function!"

if __name__ == '__main__': # Only run when you do python mathmatic.py
    test = TestClass()
    print test.addfour(1,2,3,4)
