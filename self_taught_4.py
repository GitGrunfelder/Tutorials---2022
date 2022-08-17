def square_it(x):
    """
    Returns x squared.
    :param x: int.
    :return: product of int x times int x.
    """
    return(x * x)

def print_it(str):
    """
    Prints whatever is put as a parameter.
    :param str: any str or str variable.
    :return: product of int x times int x
    """
    print(str)

def parameter_Function(age, weight, gender, species="human", planet="Earth"):
    """
    A function with 3 required params, and 2 optional.
    :param age,weight,gender: required params.
    :param species, planet: optional params.
    :prints: Description based on params, including optional.
    """
    print("You are",age,"years old.")
    print("You weigh", weight,"pounds.")
    print("You identify as", gender,".")
    print("You are", species,".")
    print("You are from", planet,".")
    

def halfer(x):
    """
    A function that divides param(x) by 2.
    :param x: int.
    :returns: Half of x integer.
    """
    return x/2

def quad(y):
    """
    A function that multiplies param(y) by 4.
    :param y: int.
    :returns: y int multiplied by 4.
    """
    return y*4

def str_to_float(int):
    """
    A function that converts str to float. Uses exception handling.
    :param int: int.
    :returns: int converted to float. If exception occurs, prints error message.
    """
    try:
        return float(int)
    except ValueError:
        print("Must enter a valid integer.")
        
#----------------------------------------------------------------#       
#1
print(square_it(10)) 
#2
str = "Welcome to Walmart!"
print_it(str)
str = input("Type something you would like printed: ")
print_it(str)   
#3
parameter_Function(30, 140, "male")
#4
halved = halfer(10)
print(quad(halved))
#5
int = input("Please type a number: ")        
print(str_to_float(int))


