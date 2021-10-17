# What is Python?
#   Python is an interpreted language; eg, it isn't compiled.
#   As a result, Python suffers from an extreme lack of speed.
#   In fact, C++ is somewhere around 400 times faster than Python.

#   But anyway, Python is basically just another programming language.
#   It's good at AI and machine learning, plus GPIO and all that, since
#   it's a newer language and people have chosen to support those on
#   this language.

# How do you write comments in Python?
#   Prepend the comment line with a pound sign (#) in order to denote it as a comment.

# How do you output to the console?
#   Much like Java's System.out.println("") or C++'s std::cout << "" command,
#   Python has a print command, print(""), too.
#   Here's an example:
print("Hello World")

#   Notably, Python, unlike Java or C++, doesn't require semicolons at the end of their lines.

# How do we create variables in Python?
#   In Python, we can create variables simply, like this:
varName = "I'm a variable!"
#   Note, it doesn't require a class denotion or anything, since
#   Python will figure it out anyway. It's like using the var keyword in Java
#   or the auto keyword in C++.

#   We can *even* call the print method using it!
print(varName)

#   Variables are updated like so:
varName = 5
#   And since Python doesn't have any fancy class stuff, we can change a variable's
#   class after it's been made, like here, where I go from a String to an Integer.
#   Also, you can do something called a "hint" towards what class a variable should be
#   by putting a colon and then a type after the name of the variable, before the "=".
#   (See line 92 or 68 for an example of hinting.)

# What kinds of numbers are there in Python?
#   In Python, there are integers and floats:
float = 5.3
integer = 3
#   We can *even* do the usual things with them, like add and subtract and all that.
varName = float + integer
print(varName)  # 8.3
#   However, the distinction between floats and integers is fixed at runtime,
#   and in fact, adding numbers of different types throws no errors or anything
#   since Python (versions 2.8 and later) automatically convert all ints to floats
#   when they're involved in math with floats.

# Errors? What are they?
#   In Python, there are several kinds of errors, just like Java and C++.
#   For example, here's a division by zero error to end off the file.
number1 = 0
number2 = 2
# print(number2 / number1)   #jkjk I need to write some more garbage

# Can you flat-out delete variables in Python?
#   Unlike Java or C++, Python *does* let you delete stuff, using
#   the del keyword:
del number2, number1, varName
#   You can also delete

# What are the math operators in Python?
#   Well, in Python, we've got normal math operators, assignment operators, and shift operators.
#   Here's an example using addition of each of the first two types:
exampleVar: int = 10
exampleVar = exampleVar + 2
exampleVar += 2  # exampleVar is now 14.

#   And here's an example using a shift marker.
#       Shift markers basically move bits in memory over by a number,
exampleVar = exampleVar << 2  # exampleVar is now 56.
print(exampleVar)
#   Here's the math explaining this shift above.
#       14 in binary is 000001110
#       000001110 shifted over by three is 000001110000
#       000001110000 in decimal is 56.

#   Also, you can do exponential math using the ** operator:
exampleVar = 8
print(exampleVar ** 2)  # outputs 64
#   As a note, Python follows the same PEMDAS system as Java and C++.
#   Wikipedia has a bit to say on this: https://en.wikipedia.org/wiki/Order_of_operations
del exampleVar

# String concatenation? Can you multiply strings? Is that a thing?
#   Yep, just like any other language, you cna concatenate strings by "adding" them.
#   HOWEVER, you can multiply a string by an INTEGER (no floats), to add itself
#   to itself, multiple times.
exampleVar: str = "A string."
print(exampleVar * 5)
del exampleVar

# How do you do multi-line strings? Do you just use \n or %n or something?
#   In Python, there are two ways to make multiline strings:
#   the first is, of course, \n, in a string, like this:
print("Hello\nWorld!")  # Outputs Hello and World on different lines.
#   The second, however, is by using triple quotes, since they never appear
#   in serious media:
exampleVar: str = """
wow
look
I'm a string on multiple lines!
And I can have " quotes and ' apostrophes in me!"""
