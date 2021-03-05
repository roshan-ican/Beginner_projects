print('imported my_module')
test = 'Test String'

def find_index(to_search, target):
    """Find a index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i
        return -1
#import
    from my_module import find_index, test

    courses = ['history', 'math', 'physics']
    index = find_index(courses, 'math')
    print(index)
    print(test)