
import logging


def addition():
    is_entering = True
    result = 0
    digit_counter = 0
    logging.info("Addition was chosen")
    while is_entering:
        x = input("\nEnter digit - ")
        logging.info(f"{x} was chosen")
        if x.isdigit():
            a = float(x)
            digit_counter = digit_counter + 1
            result = result + a
            if digit_counter > 1:
                print(f"\nResult is {result}")
        else:
            logging.info(f"{x} - It's not a digit")
    return result


def subtraction():
    is_entering = True
    while is_entering:
        logging.info("Distinction was chosen")
        x = input("\nEnter first digit - ")
        logging.info(f"{x} was chosen as first digit")
        if x.isdigit():
            a = float(x)
            print("\nEnter second digit - ")
            y = input()
            logging.info(f"{x} was chosen as second digit")
            if y.isdigit():
                b = float(y)
                result = a - b
                print(f"\nResult is {result}")
                return result
            else:
                logging.info(f"{x} - It's not a digit")
        else:
            logging.info(f"{x} - It's not a digit")


def multiplication():
    is_entering = True
    result = 0
    digit_counter = 0
    logging.info("Product was chosen")
    while is_entering:
        x = input("\nEnter digit - ")
        logging.info(f"{x} was chosen")
        if x.isdigit():
            a = float(x)
            digit_counter = digit_counter + 1
            if digit_counter == 1:
                result = a
            if digit_counter > 1:
                result = result * a
                print(f"\nResult is {result}")
            if result == 0:
                digit_counter = 0
        else:
            logging.info(f"{x} - It's not a digit")
    return result


def division():
    is_entering = True
    while is_entering:
        logging.info("Distinction was chosen")
        x = input("\nEnter first digit - ")
        logging.info(f"{x} was chosen")
        if x.isdigit():
            a = float(x)
            y = input("\nEnter second digit - ")
            logging.info(f"{y} was chosen")
            if y.isdigit():
                b = float(y)
                result = a / b
                print(f"\nResult is {result}")
                return result
            else:
                logging.info(f"{x} - It's not a digit")
        else:
            logging.info(f"{x} - It's not a digit")


def choosing_operation():
    while True:
        choice = input(
            "Input correct number and choose operation: 1 addition, 2 subtraction, 3 multiplication, 4 division \n")
        if choice == "1":
            (addition())
        if choice == "2":
            (subtraction())
        if choice == "3":
            (multiplication())
        if choice == "4":
            (division())      


logging.basicConfig(level=logging.DEBUG)
choosing_operation()