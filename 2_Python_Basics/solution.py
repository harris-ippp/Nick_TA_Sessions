'''
Hi! Today we are going to solve a serious problem - 
who is coming to Harris After Hours, and how much did they drink?

This thing here is called a Doc String, and is very important to coding.

It is a reference point for any program file or function, and will be
used either by you or any programmer working for you.

A Doc String is a triple-quote string at the beginning of a file or function.

To use a Doc String - do the following in an interpreter:

    import after_hours
    after_hours?

The purpose of this assignment is to become familar with Functions,
but we will also a first peek at some data structures.
'''

STUDENTS = {}
NUM_BEERS = []

def sign_in():
    '''
    This function takes in user input to store 
    a student and the number of beers they had.

    Let's use what we know about input() and while loops
    to find a solution.
    ''' 
   
    print('Enter a student and the number of beers they drank.')
    print('A value of -1 for beers will exit!')
    
    while True:
        student_name, beer_count = read_in_student()
        if beer_count == -1:
            break
        add_student(student_name, beer_count)

    beers = total_beers()
    
    return ('{} students came to After Hours. '
            'They drank a total of {} beers!'.format(len(STUDENTS), beers))

def read_in_student():
    '''
    Read in a student and the number of beers they drank.
    Input: 
          From the user!
    Output: 
          student_name (string)
          beer_count (int)
    '''
    
    student_name = input('Student Name: ')
    beer_count = int(input('Number of beers: ')) 
    return student_name, beer_count

def add_student(student_name, beer_count):
    '''
    Given a student and the number of beers they drank, this function
    stores useful info in STUDENTS (dict) and NUM_BEERS (list).

    Input: 
          student_name (string)
          beer_count (int)
    Output:
          None, this function only modifies our data structures.
          Remeber, None is still a variable type being returned!
    '''
    STUDENTS[student_name] = beer_count
    NUM_BEERS.append(beer_count)

def total_beers():
    '''
    Find the total number of beers...

    '''
    return sum(NUM_BEERS)
