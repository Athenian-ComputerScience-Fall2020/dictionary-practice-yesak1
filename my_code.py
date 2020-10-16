# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def make_dict():
    '''
    use the following information to create a dictionary called currency:
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    '''
    currency = {"Ten": 10, "Twenty": 20, "Thirty": 30}         # complete this line

    return currency

def add_element():
    foods = {'fruit': 'apple', 'veggie': 'carrot', 'grain': 'barley'}
    # add a key value pair 'dairy': 'yogurt' to the following dictionary

    foods.update({"dairy": "yogurt"})

    return foods

def remove_element():
    foods = {'fruit': 'apple', 'veggie': 'carrot', 'grain': 'barley'}
    # remove 'veggie': 'carrot' from the dictionary
    del foods["veggie"]


    return foods

def merge_dict():
    # Merge these two dictionaries together so the contents are in numerical order:
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    
    dict1.update(dict2) 
    return dict1  # return new dictionary

def access_key():
    # return the value of the key 'Twenty'
    currency = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

    val = currency.get("Twenty", 'not found')           # add code to assign the desired value to 'val'
    return val





if __name__ == '__main__':
    # Test your code with this first
    # Change the function to test different sections
    print(merge_dict())

