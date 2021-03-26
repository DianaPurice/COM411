import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.user_input as user_input
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.string_operators as string_operators
import basics.input.review as input_review
import basics.decisions.simple_decision.if_op as if_op
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.decisions.simple_decision.comparation_operator as comperation_operator
import basics.decisions.simple_decision.counter as counter
import basics.decisions.nested_decision.nested as nested
import basics.decisions.nested_decision.nestception as nestception
import basics.decisions.or_operator as or_operator
import basics.decisions.and_operator as and_operator
import basics.decisions.review as decision_review
import basics.repetitions.while_loop.simple as simple_while
import basics.repetitions.while_loop.count as count_while
import basics.repetitions.while_loop.ascii as ascii_while
import basics.repetitions.while_loop.len as len_while
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.for_loop.simple as simple_for
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.range as range_for
import basics.repetitions.for_loop.characters as characters_for
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.nested_loop.nested as nested_for
import basics.repetitions.nested_loop.nesting as nesting
import basics.functions.ascii_code as ascii_code
import basics.functions.ascii_character as ascii_character
import basics.functions.simple_function as simple_function
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.function_calls as function_calls
import basics.modules.guess_the_number as guess_the_number

def run_block_a():
  is_running = True
  while(is_running):
    print("\nWhich program in 'Block A: Basics (Output/Input)' do you wish to run?")
    print()
    print("[1] simple_message")
    print("[2] multiline_message")
    print("[3] escape_characters")
    print("[4] ascii_art")
    print("[5] user_input")
    print("[6] ascii_robot")
    print("[7] data_types")
    print("[8] string_operators")
    print("[9] input_review")
    print("[10] quit")
    print()
    response = input()
    if (response == "1"):
        simple_message.run()
    elif (response == "2"):
        multiline_message.run()
    elif (response == "3"):
        escape_characters.run()
    elif (response == "4"):
        ascii_art.run()
    elif (response == "5"):
        user_input.run()
    elif (response == "6"):
        ascii_robot.run()
    elif (response == "7"):
        data_types.run()
    elif (response == "8"):
        string_operators.run()
    elif (response == "9"):
        input_review.run()
    elif (response == "10"):
      break
    else:
      print("\nInvalid option! Please try again.\n")
    
def run_block_b():
  is_running = True
  while is_running:
    print("\nWhich program in 'Block B: Basics (Decisions)' do you wish to run?\n")
    print("[1] if_op\n[2] if_else\n[3] if_elif_else\n[4] modulo_operator\n[5] comperation_operator\n[6] counter\n[7] nested\n[8] nestception\n[9] or_operator\n[10] and_operator\n[11] decision_review\n[12] quit\n")
    response = input()
    if (response == "1"):
          if_op.run()
    elif (response == "2"):
          if_else.run()
    elif (response == "3"):
          if_elif_else.run()
    elif (response == "4"):
            modulo_operator.run()
    elif (response == "5"):
            comperation_operator.run()
    elif (response == "6"):
            counter.run()
    elif (response == "7"):
            nested.run()
    elif (response == "8"):
            nestception.run()
    elif (response == "9"):
            or_operator.run()
    elif (response == "10"):
            and_operator.run()
    elif (response == "11"):
          decision_review.run()
    elif (response == "12"):
      break
    else:
        print("Invalid option! Please try again.")

def run_block_c1():
  is_running = True
  while is_running:
    print("Which program in 'Block C: Basics (Repetitions: Part 1)' do you wish to run?'")
    print("""[1] simple_while
[2] count_while
[3] ascii_while
[4] len_while
[5] sum_100
[6] sum_user_numbers
[7] factorial
[8] simple_for
[9] count_down
[10] range_for
[11] characters_for
[12] quit """)
    response = input()
    if (response == "1"):
        simple_while.run()
    elif (response == "2"):
        count_while.run()
    elif (response == "3"):
        ascii_while.run()
    elif (response == "4"):
        len_while.run()
    elif (response == "5"):
        sum_100.run()
    elif (response == "6"):
        sum_user_numbers.run()
    elif (response == "7"):
        factorial.run()
    elif (response == "8"):
        simple_for.run()
    elif (response == "9"):
        count_down.run()
    elif (response == "10"):
        range_for.run()
    elif (response == "11"):
        characters_for.run()
    elif (response == "12"):
        break
    else:
      print("Invalid option! Please try again.")

def run_block_c2():
  is_running = True
  while is_running:
    print("Which program in 'Block C: Basics (Repetitions: Part 2)' do you wish to run?'")
    print("[1] reverse\n[2] membership_operators\n[3] nested_for\n[4] nesting\n[5] quit")
    response = input()
    if (response == "1"):
        reverse.run()
    elif (response == "2"):
        membership_operators.run()
    elif (response == "3"):
        nested_for.run()
    elif (response == "4"):
        nesting.run()
    elif (response == "5"):
      break
    else:
      print("Invalid option! Please try again.")

def run_block_d():
  is_running = True
  while is_running:
    print("Which program in 'Block D: Basics (Funcions and Modules)' do you wish to run?'")
    print("[1] ascii_code\n[2] ascii_character\n[3] simple_function\n[4] function_with_nesting\n[5] function_with_parameter\n[6] function_with_loop\n[7] function_with_parameters\n[8] multiple_functions\n[9] return_values\n[10] function_calls\n[11] guess_the_number\n[12] quit")
    response = input()
    if (response == "1"):
      ascii_code.run()
    elif (response == "2"):
        ascii_character.run()
    elif (response == "3"):
        simple_function.run()
    elif (response == "4"):
        function_with_nesting.run()
    elif (response == "5"):
        function_with_parameter.run()
    elif (response == "6"):
        function_with_loop.run()
    elif (response == "7"):
        function_with_parameters.run()
    elif (response == "8"):
        multiple_functions.run()
    elif (response == "9"):
        return_values.run()
    elif (response == "10"):
        function_calls.run()
    elif (response == "11"):
        guess_the_number.run
    elif (response == "12"):
      break
    else:
      print("Invalid option! Please try again.")



def run():
    is_running = True

    while(is_running):
        print("What would you like to do?\n")
        print("[a] Run 'Block A: Basics (Output/Input)' programs")
        print("[b] Run 'Block B: Basics (Decisions)' programs")
        print("[c1] Run 'Block C1: Basics (Repetitions: Part 1)' programs")
        print("[c2] Run 'Block C2: Basics (Repetitions: Part 2)' programs")
        print("[d] Run 'Block D: Basics (Functions and Modules)' programs")
        print("[q] Quit\n")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "b"):
            run_block_b()
        elif (response == "c1"):
            run_block_c1()
        elif (response == "c2"):
            run_block_c2()
        elif (response == "d"):
            run_block_d()
        elif (response == "q"):
            break
        else:
          print("\nInvalid option! Please try again.\n")

run()


