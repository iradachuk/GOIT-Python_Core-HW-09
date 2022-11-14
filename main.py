USERS = {}


def input_error(func):
    def inner(data):
        try:
            result = func(data)
            return result
        except KeyError:
            print('No user with given name.')
        except ValueError:
            print('Give me name and phone, please.')
        except IndexError:
            print('Give me name and phone, please.')
    return inner


def greeting(_):
    print('How can I help you?')


def good_bye(_):
    print('Good bye!')


@input_error
def add_contact(data):
    name = data[0]
    phone = data[1]
    USERS[name] = phone
    print(f'The user with name {name} and phone {phone} was added!')


@input_error
def change_phone(data):
    name = data[0]
    phone = data[1]
    for key in USERS.keys():
        if key == name:
            USERS[name] = phone
    print(f'The phone number for name {name} was changed!')


@input_error
def show_phone(data):
    print(f'The phone number is: {USERS[data[0]]}')


def show_all(_):
    for name, phone in USERS.items():
        print(f'{name} - {phone}')


def unknown_command(_):
    print('This command is unknown!')


def get_handler(user_input):
    action = user_input.split()[0].lower()
    data = user_input.split()[1:]
    try:
        handler = COMMANDS[action]
    except KeyError:
        handler = unknown_command
        if not action or action == '.':
            handler = good_bye
    return handler, data

COMMANDS = {
    'hello': greeting,
    'add': add_contact,
    'change': change_phone,
    'phone': show_phone,
    'show_all': show_all,
    'good_bye': good_bye,
    'exit': good_bye,
    'close': good_bye
    }


def main():
    flag = True
    while flag:
        user_input = input('>>> ')
        if user_input in ('good_bye', 'exit', 'close'):
            flag = False
        handler, data = get_handler(user_input)
        try:
            handler(data)
        except KeyError:
            print('Unknown command')

               
if __name__ == '__main__':
    main()