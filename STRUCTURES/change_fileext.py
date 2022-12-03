# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
def change_ext(filenames, old, new):
    return [filename.replace(old, new) if filename.endswith(old) else filename for filename in filenames]

newfilenames = change_ext(filenames, "hpp", "h")
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# # ALTERNATIVES | 1

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# def change_ext(filenames, old, new):
#     newfilenames = []
#     for filename in filenames:
#         index = filename.index(".") + 1
#         if filename[index:] == old:
#             filename = filename[:index] + new
#         newfilenames.append(filename)
#     return newfilenames
    
# newfilenames = change_ext(filenames, "hpp", "h")
# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# # ALTERNATIVES | 2

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# def change_ext(filenames, old, new):
#     newfilenames = []
#     for filename in filenames:
#         index = len(filename) - len(old)
#         if filename[index:] == old:
#             filename = filename[:index] + new
#         newfilenames.append(filename)
#     return newfilenames

# newfilenames = change_ext(filenames, "hpp", "h")
# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]