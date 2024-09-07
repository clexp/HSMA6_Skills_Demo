
class Integer_Calculator:
    # 2. does not receive the switched on here
    # def __init__(self, switched_on):
    def __init__(self):
        self.switched_on = False
        self.list_of_inputs = []
        self.operator = ""
        
    def switch_on_calculator(self):
        # self.switched_on == True
        # 9. conditional not assignment
        self.switched_on = True
        # 42. undeclared operator variable
        # print "Calculator is now turned off"
        # 4. inaccurate print statement
        # 5. missing brackets
        print ("Calculator is now turned on")

        
    def switch_off_calculator(self):
        self.switched_on == False
        # print "Calculator is now turned on"
        # 72 missing brackets on print function
        print("Calculator is now turned off")

    # def add_numbers(self, list of numbers):
    # 46. list part of object, already referenced as self
    def add_numbers(self):
        # result = sum(self.list_of_integers)
        # 47. variable name change
        # 48. calling line expecting int returned
        # 49. use of assignment??
        return sum(self.list_of_inputs)
    
    #def subtract_numbers(list_of_numbers):
    # 55. belongs to function must hand over self
    def subtract_numbers(self):
        result = self.list_of_inputs[0]
        
        # for x in range(1, len(list_of_number):
        # 56. mis referencing data structure in object
        #for x in range(1, len(self.list_of_inputs):
            # result =- list_of_numbers[number]
            # 56. unknown =- did you mean -=
            # 57. not referencing counter x
            # 58. clumsy use of range for indexing use list slices
        for this_number in self.list_of_inputs[1:]:
            result += this_number
            
        return result
    
    # def multiply_numbers(self, list_of_numbers):
    # 59. double referencing data structure
    def multiply_numbers(self):
        # result = list_of_numbers
        # 60. mis labelling and 
        # 61. using list not int
        result = self.list_of_inputs[0]
        
        #for x in range(1, len(list_of_numbers)):
        #    result = result ** list_of_numbers[x]
        # 62 clumsy use of range, could use list slices
        # 63 use of power not multiple
        # 64 bad naming convention 'x'
        for this_number in self.list_of_inputs[1:]:
            result *= this_number
            
        # return number
        # 65. variable name swap
        return result
    
    # def divide_numbers():
    # 66. failed to reference self in method definition
    def divide_numbers(self):
        """ This function will alway return a float unless corrected.  
        This program is an integer calculator and needs to return an int. """
        result = self.list_of_inputs[0]
        
        # for x in range(1, len(list_of_numbers)):
        # 67. clumsy use of range
        for this_number in self.list_of_inputs[1:]:
            result = result / this_number
        
        # return result
        # 68. not returning an int type
        return int(result)
    
    def input_numbers(self):
        # if switched_on = False:
        # 10. assignment not conditional
        # 11. no reference to self
        if self.switched_on == False:
            # 6. not indented properly
            #print "Calculator is switched off"
            # 71. no brackets on print statement
            print("The calculator is off")
            # return []
            # 7. not expecting to return a list
            return
        # else:
        # 19. no need for else, change indentation
        # keep_inputting = False
        # 8. never goes into for loop
        keep_inputting = True
        
        # while keep_inputting = True:
        # 12. assignment where conditional should be
        while keep_inputting == True:
            try:
                input_number = int(input("Please input number : "))
                # list_of_inputs.add(input_number)
                # 13. undeclared variable list_of_inputs
                # 14. unknown function add
                self.list_of_inputs.append(input_number)
                
                # valid_continue_decision = True
                # 23. variable name change
                # 24. uneeded variable re assignment
                # while valid_continue_decision == False:
                # 15. incorrect logic never enters while loog
                # while valid_continue_decision == True:
                # 25. variable name change
                # while keep_inputting == True:
                # 26. uneeded while loop
                # 27. corrected indentation
                # continue_decision = int(input("Continue (Y/N)? : "))
                # 16. string not integer
                # 17. no bad data capture
                # 19. brittle code, case sensitivity
                # continue_decision = input("Continue (Y/N)? : ")
                # 28. unclear instructions
                continue_decision = input("Continue inputting numbers (Y/N)? : ")
                
                # if continue_decision = "Y":
                # 18. assignment error
                #if continue_decision == "Y":
                #    valid_continue_decision = True
                #elif continue_decision = "N":
                #    valid_continue_decision = True
                # 29. needless double if statement
                # 30. assignment in place of conditional
                if continue_decision == "N":
                    keep_inputting = False
                # 31. wrong location return statment    
            # exception
            # 21 unknown keyword
            except:
                #print "You must input integers only"
                # 73. no brackets on print statement
                print ("You must input integers only")

            # return list_of_inputs
            # 32. undeclared list of inputs
            # 33. no need to return the input data
        # 83. indent for return wrong
        return 
                    
    def input_operator(self):
        if self.switched_on == False:
            print ("Calculator is switched off")
            
            # return ERR
            # 34. wrong use of exception handling
            return
        # except:
        # 35. use of except before try
        # try:
        # 75. not sure why using try, not loading any files...
        # valid_operator = False
        # 37. no need for valid_operator bool
        # alreagy has escape condition
        # while valid_operator == False:
        # 38. has a break condition
        while True:
            print ("Please input : ")
            print ("+ for addition")
            print ("- for subtraction")
            print ("* for multiplication")
            print ("/ for division")
            # selected_operator = int(input "SELECTION : ")
            # 39. this is a string not an int
            # 40. brackets are in the wrong place
            selected_operator = input("SELECTION : ")
            
            # if selected_operator == ["+", "-", "*", "/"]:
            # 36. operator is a single char string, not a list
            if selected_operator in ["+", "-", "*", "/"]:
                # valid_operator = True
                # 41. do not need this check
                self.operator = selected_operator
                # return selected_operator
                # 43. no need to return the operator
                return
            # elif:
            # 74. no conditional on elif, did you mean else?
            else:
                print ("Invalid operator")
                    
# Integer_Calculator()
# 1. instantiate the object properly
my_calculator = Integer_Calculator()

# my_calculator.turn_on_calculator(True)
# 3. do not need to send state
# my_calculator.turn_on_calculator()
# 77. miss named method
my_calculator.switch_on_calculator()

my_calculator.input_numbers()
my_calculator.input_operator()

# if len(list_of_input_numbers) < 0
# 44. all operators need at least 2 number (and 78. greater than)
# and 76. a colon on if statetments
if len(my_calculator.list_of_inputs) >= 2 :
    # 79. 80. 81. 82 using 'chosen operator' not self.operator
    if my_calculator.operator == "+":
        answer = my_calculator.add_numbers()
    # elf chosen_operator == "-":
    # 50. unknown keyword elf, did you mean elif?
    elif my_calculator.operator == "-":
        answer = my_calculator.subtract_numbers()
    # elf chosen_operator == "*":
    # 51. unknown keyword elf, did you mean elif?
    elif my_calculator.operator == "*":
        answer = my_calculator.multiply_numbers()
    # elf chosen_operator == "/":
    # 52. unknown keyword elf, did you mean elif?
    elif my_calculator.operator == "/":
        answer = my_calculator.divide_numbers()
    # els:
    # 53. unknown keyword els, did you mean else?
    else:
        # print ("Error - calculator was switched off")
        # 54. inaccurate statement
        print ("Error - unknown operator")
        
    # print "The answer is {answer}"
    # 69. no brackets calling print
    # 70. no f on f-string
    print(f"the answer is : {answer}.")
else:
    # print ("Only one number given")
    # 45. inaccurate statement
    print ("all operations need at least 2 numbers")

# 77. forgotten to use switch off functions
my_calculator.switch_off_calculator()