##  hyperskills decorators explained
#######################################
##  PART 1.Declaration

def our_decorator(other_func):
  def wrapper(args_for_function):
    print("This happens before we call the function")
    return other_func(args_for_function)
  return wrapper

#######################################
##  PART 2.Execution

@our_decorator
def greet(name):
  print("Hello", name)
  
greet("Suzie")  # this will return two lines:
                # "This happens before..."
                # "Hello Suzie"

##  PART 2.1 Simpler Execution

def greet(name):
  print("Hello", name)
  
greet = our_decorator(greet)  ## use this instead of @
greet("John") ## call newly decorated function

## new way of calling Decor (2023)
our_decorator(greet)("John")     
######################################### END

##  DECORATORS FOR DUMMIES ##
##  PART 1.Declaration

def this_is_decorator(pass_function_here):
  def this_is_only_wrapper(pass_arguments_pattern_here):  #  safe arguments (*x)
    print("This is part from Deccorator")           #  any Decorator content here
    
    return pass_function_here(pass_arguments_pattern_here)  # THIS IS IMPORTANT
    # "decorated" function can be returned like above
    pass_function_here(pass_arguments_pattern_here)   #  THIS IS ALSO IMPORTANT
    # "decorated" function can be launched like above
  
    print("THis is more from Decorator")    #  Decorator content after "decorated" function
  return this_is_only_wrapper        #  REMEMBER NO PARHENTASIS ()-NO

##  PART 2.Execution

@this_is_decorator                    #  from the first line of PART 1.
def any_new_function(arguments):      #  IMPORTANT - this function will be "decorated"
  print(arguments)                    #  IMPORTANT - this content will be "decorated"
  
  any_new_function("Try print this")  #  ...any time you call "deccorated function"
                                      #  ...its result will be "mixed" with "decorator" results
    
###################################################################################################


