# Sequential stuff is all fine and good, but what *if* I want to only do something under a certain condition?
#   Well, you can use If-statements. Good ol' ELIFS, we all love them conditionals. y'know how it is.
#   In Python, we use the keywords "True" and "False" to declare a boolean expression, like so:
isThisABoolean = True
#   And you can print them out like so:
print(isThisABoolean)
#   There are also relational operators, like == (Equal To) and != (Not Equal To)
var1 = True
var2 = False
isThisABoolean = var1 != var2  # Evaluates to true, since var1 doesn't equal var2.
#   The other operators are; >, greater than; >=, greater than or equal to; <, less than; and <=, less than or equal to.
#   They function exactly like every other language's relational operators, so yeah.
#   There's also the usual and (and), or (or) and not (not) operators, too, which function
#   exactly like Java and C++'s, except for the fact that they're words instead of just characters.
print(isThisABoolean)
del var2, var1, isThisABoolean
#   Also, just a note: The type-name for a boolean in Python is "bool", so you can hint something like this:

# What if I want to know what type a variable is? Is there a function for that?
#   In Python, there's an inbuilt function, type(), which accepts a variable and returns the type of it:
variable = "I am a number, totally. Definitely not a string, lol."
type(variable)
#   Now, on it's own, it doesn't actually do anything, so you have to print it out in order to see it:
print(type(variable))

# Okay, but what does this have to do with conditionals?
#   Well, you see, booleans lie at the heart of conditionals, in fact, they're like half of an if-statement.
#   Here's an example if-statement:
if type(variable) == str:
    print("Variable is a string!")
#   You'll notice that we use the keyword "if", before a conditional, then a colon to make an if statement.
#   Next, we go down a line and indent by one, which is how Python denotes a group of statements.

# Alright, but what if I want it to do something *only* if an if-statement was false?
#   We use something called an "else-statement", here's an example:
AFalseCondition = False
if AFalseCondition:
    print("This won't run!")
else:
    print("This else statement ran!")

# Okay, but what if I want to only evaluate a conditional if another conditional was false? (An else-if?)
#   So if you want to evaluate a conditional if another has been false, you can use an elif statement:
if AFalseCondition:
    print("This won't run.")
elif not AFalseCondition:
    print("This elif will run!")
else:
    print("This won't run, since the previous elif statement was correct!")