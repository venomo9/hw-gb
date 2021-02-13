from sys import argv

def validate (args):
    error = 0

    try:
        for _ in range(len(args)):
            args[_] = float(args[_])
    except ValueError:
        error = 1

    return error, args

if len(argv) != 4:
    print(f"usage: {argv[0]} <выработка> <ставка в час> <премия>")
    exit(1)
else:
    error, vals = validate(argv[1:])
    if error:
        print("Validation error")
        exit(1)
    else:
        print(f"Ты заработал: {vals[0] * vals[1] + vals[2]} биткоинов!")

