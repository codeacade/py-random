##  hyperskills decorators explained
#######################################
##  PART 1.

def our_decorator(other_func):
  def wrapper(args_for_function):
    print("This happens before we call the function")
    return other_func(args_for_function)
  return wrapper

#######################################
##  PART 2.

@our_decorator
def greet(name):
  print("Hello", name)
  
greet("Suzie")  # this will return two lines:
                # "This happens before..."
                # "Hello Suzie"

######################################### END

##  DECORATORS FOR DUMMIES ##
##  PART 1.

def this_is_decorator(pass_function_here):
  def this_is_only_wrapper(pass_arguments_pattern_here):  #  safe arguments (*x)
    print("This is part from Deccorator")           #  any Decorator content here
    return pass_function_here(pass_arguments_pattern_here)  # THIS IS IMPORTANT
  return this_is_only_wrapper        #  REMEMBER NO PARHENTASIS ()-NO

##  PART 2.

@this_is_decorator                    #  from the first line of PART 1.
def any_new_function(arguments):      #  IMPORTANT - this function will be "decorated"
  print(arguments)                    #  IMPORTANT - this content will be "decorated"
  
  any_new_function("Try print this")  #  ...any time you call "deccorated function"
                                      #  ...its result will be "mixed" with "decorator" results
    
###################################################################################################


