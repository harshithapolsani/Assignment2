# function that returns the full name
def fullname(first_name,last_name):
# concatenation of strings and returning the full name
    return (first_name + " " + last_name)
# function that returns every other character in the full name string
def string_alternative(full_name):
    modified_string = ""
    for i in range(0,len(full_name),2):
        modified_string += full_name[i]
# returning the modified string
    return modified_string
# this is the main function
def main():
# taking user input first_name and last_name.
   first_name = input('Enter the first name:')
   last_name = input('Enter the last name:')
# calling full_name function
   temp = fullname(first_name=first_name,last_name=last_name)
# dislaying the full name
   print("The full name is :",temp)
# displaying the modified string
   print("The modified String is:",string_alternative("Good evening"))
# calling the main function..
main()