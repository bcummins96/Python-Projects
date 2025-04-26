#learning about classes 

#In order to be an instance method, a method requires a special parameter, named self by convention. This parameter is a reference to the instance of the class and must always be the first parameter.

#The instantiation creates an empty object. The __init__ method is a special method that allows you to instantiate an object to a customized state. When a class implements an __init__ method, __init__ is automatically called upon instantiation.

#Inside your Board class, delete the spam method and replace it with an __init__ method that includes a self parameter. 


class Board:
    def __init__(self):
        pass

#An attribute is a variable associated with an object, which is used to store data as regular variables.

#The .index() method raises a ValueError exception when the value is not found. To prevent the program from halting execution, you'll nest this line of code inside a try block. The try statement is used to encapsulate code that might raise an exception. The except clause, on the other hand, offers alternative code to execute if an exception

#find_empty_cell returns the position of the empty cell (which list, which element)
#a method named valid_in_row and give it three parameters: self, row, and num. Where self represents the instance of the class, and row and num are the row index and the number to be checked, respectively.


#It's time to test the valid_in_row method. Call valid_in_row on gameboard. Pass it 0 and 8 as the arguments and print the result.
#Again, note how the method is defined with three parameters, yet it is called with only two arguments because self is automatically passed as the object on which the method is called.

#A generator expression in Python offers a memory-efficient way to create iterators. It employs a concise syntax, similar to list comprehensions, but instead of constructing a list in memory, it generates values on-the-fly.
#The generator expression you just wrote in the previous step generates a list of boolean values representing whether the condition self.board[row][col] != num is True or False for each element in the specified column across all rows.
#Pass that generator expression to the all() function to check if all the elements in the column are different from num and return the result.

#A tuple can be unpacked, meaning that the elements contained in the tuple can be assigned to variables, like this:
#spam = ('lemon', 'curry')
item1, item2 = spam
In the example above, item1 would have the value 'lemon' and item2 would have the value 'curry'.

The := operator gives you the ability to assign variables in the middle of an expression. The syntax is: name := val, where name is the variable name and val is the variable value.

If the recursive call returns False, it means the guess led to an unsolvable sudoku. So you'll need to restore the cell to be empty and explore another guess.
After the innermost if statement, set the current cell value back to 0.

The __str__ method is a special method that is called under the hood when the object is printed using the print() function, or converted into a string using the str() function.