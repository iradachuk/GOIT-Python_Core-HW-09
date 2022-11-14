USERS = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'No user with given name.'
        except ValueError:
            return 'Give me name and phone, please.'
        except IndexError:
            return 'Give me name and phone, please.'
    return inner


def greeting(_):
    return 'How can I help you?'


def good_bye(_):
    return 'Good bye!'


@input_error
def add_contact(data):
    name, phone, *_ = data
    USERS[name] = phone
    return f'The user with name {name} and phone {phone} was added!'


@input_error
def change_phone(data):
    name, phone, *_ = data
    for key in USERS.keys():
        if key == name:
            USERS[name] = phone
    return f'The phone number for name {name} was changed!'


@input_error
def show_phone(data):
    return f'The phone number is: {USERS[data[0]]}'


def show_all(_):
    for name, phone in USERS.items():
        return f'{name} - {phone}'


def unknown_command(_):
    return 'This command is unknown!'


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
        if user_input in ('good_bye', 'exit', 'close', '.'):
            flag = False
        handler, data = get_handler(user_input)
        try:
            result = handler(data)
            print(result)
        except KeyError:
            print('Unknown command')

               
if __name__ == '__main__':
    main()