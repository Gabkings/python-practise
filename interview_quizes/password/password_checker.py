'''
    Question:
    A website requires the users to input username and password to register. 
    Write a program to check the validity of password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    Your program should accept a sequence of comma separated passwords and
     will check them according to the above criteria.
    Passwords that match the criteria are to be printed, each separated by a comma.
    Example
    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    ABd1234@1
    '''
def pword_checker():
    #declaring the vriables
    special_str = "$#@"
    accepted = []
    #getting the user input
    passwords = input("Enter comma-separated passwords: ").split(',')
    #
    for password in passwords:

        lower_characters = 0
        upper_characters = 0
        numbers = 0
        special_characters = 0

        for char in password:
            #At least 1 letter between [a-z]
            if char.islower():
                lower_characters += 1
            #At least 1 letter between [A-Z]
            elif char.isupper():
                upper_characters += 1
            #At least 1 letter between [1-9]
            elif char.isdigit():
                numbers += 1
            #At least 1 character from [$#@]
            elif special_str.find(char) != -1:
                special_characters += 1

        if lower_characters >= 1 and upper_characters >= 1 and numbers >= 1 and special_characters >= 1 and len(password) in range(6, 13):
            accepted.append(password)
        #end of the second loop
    #end of the first loop
    print(",".join(accepted))

pword_checker()