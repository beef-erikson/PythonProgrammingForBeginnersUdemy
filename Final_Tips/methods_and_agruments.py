"""Shows the various ways of using methods and arguments.
"""


def example_method(mandatory_parameter, default_parameter='Default',
                   *args, **kwargs):
    print(f"""
          mandatory_parameter = {mandatory_parameter} 
          default_parameter = {default_parameter} 
          args = {args} 
          kwargs = {kwargs} 
          """)


# Different ways of using the arguments of example_method
example_method(15)
example_method(25, 'Not default')
example_method(25, 'Also not default', 'string1', 'string2', 'string3', 'string4', 'string5')
example_method(25, 'Still not default', 'string1', 'string2', key1='a', key2='b')
example_method(key1='a', key2='b', mandatory_parameter=25, default_parameter='Nope, not default!')

# Unpacking lists and dictionaries
number_list = [1, 2, 3, 4, 5, 6]
example_method(*number_list)
some_dict = {'a': '1', 'b': '2', 'c': '3'}
example_method(*number_list, **some_dict)
