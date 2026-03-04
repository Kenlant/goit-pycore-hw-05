# Не думаю, що в цьому коді можливі IndexError, бо немає звернення через індек. Додав в обробку бо було в вимогах

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if (name not in contacts.keys()):
        return "Contact is not found."

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name, = args
    if (name not in contacts.keys()):
        return "Contact is not found."

    return contacts[name]


def show_all(contacts):
    return "\n".join(f"{key} - {value}" for key, value in contacts.items())


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if (__name__ == "__main__"):
    main()
