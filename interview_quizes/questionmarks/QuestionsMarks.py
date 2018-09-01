def QsMarks(string_value):
    #declaring the viriables
    question_mark_number = 0
    second_no = 0
    has_10 = False
    #looping through the given string
    for character in string_value:
      #checking the first number in the string
        if character.isdigit():
            ''' 
              1: converting the first number into integer
              2: checking if first number plus the second number is equal to ten
              3: maintaining the position of every pair of numbers that add up to 10.
              4: If you do find two numbers that add up to 10
              5: determine if exactly 3 specific characters exist somewhere between these two indices.
            '''
            if int(character) + second_no == 10:
              #check if the question marks are 3 btw the two numbers
                if question_mark_number != 3:
                  #return false if question marks are less then 3 
                    return 'false'
                has_10 = True
            #converting the second no to integer
            second_no = int(character)
            question_mark_number = 0
        elif character == '?':
          #incrementing the number of question marks if any found in between the two numbers
            question_mark_number += 1
    return 'true' if has_10 else 'false'

# print(QsMarks("arrb6???4xxbl5???eee5"))
# print(QsMarks("acc?7??sss?3rr1??????5"))
# print(QsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"))
# print(QsMarks("9???1???9???1???9"))
# print(QsMarks("aa6?9"))

