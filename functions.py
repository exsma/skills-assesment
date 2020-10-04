"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here
def home_town (home):
    """returns true if home town is St. Paul"""
    if home == "St. Paul":
        return True
    else:
        return False 

#print(home_town ("St. Paul"))
"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here
def learning_names (first , last):
    """takes in a first and last name and returns a full name"""
    return f"{first} {last}"

"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""
def welcoming_you (first,last,home):
    """a function that prints a greeting."""
    if home == "St. Paul":
        print (f" Hi {first} {last}, we're from the same place!")
    else:
       print (f" Hi {first} {last},  I'd like to visit {home}!") 
# Write your function here


"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""
def check_if_fruit (fruit):
    """function that returns True if a fruit is a berry"""
    berries = ["strawberry" , "rasberry" , "blackberry" , "currant"]
    if fruit in berries:
        return True
    else:
        return False
# Write your function here


"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""
def cost_shipping (item):
    """a function that returns the shipping cost of an item"""
    berries = ["strawberry" , "rasberry" , "blackberry" , "currant"]
    if item in berries:
        shipping_cost = 1
    else:
        shipping_cost= 5
    return f"{shipping_cost}$"
# Write your function here


"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here
def total_cost (price,state,tax=0.05):
    """ function that returns the total cost of something"""
    if state == "CA":
        final_cost= float(int(price) + int(price)*tax + int(price)* 0.03)
    elif state == "PA":
        final_cost= float(int(price) + int(price)*tax + 2)
    elif state == "MA" and price <= 100:
        final_cost= float(int(price) + int(price)*tax + 1)
    elif state == "MA" and price > 100:
        final_cost= float(int(price) + int(price)*tax + 3)
    else: 
        final_cost = float(int(price) + int(price)*tax)
    return f"{final_cost}$"



"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here
def elongate_list (list, *more):
    """function that takes in a list and *any* number of additional arguments."""
    for x in more:
        list.extend(more)
        return list


 #source for amount of arguments is
 # https://beginnersbook.com/2019/06/python-function-arguments-default-keyword-and-arbitrary/#vararg

"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here
def times_three (name):
    """ function that takes in a word and returns a tuple."""
    def multiply_name (name):
        names = name*3
        return names
    a_tuple= (name, multiply_name(name))
    return a_tuple