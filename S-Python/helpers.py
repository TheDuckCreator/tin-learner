import  colorama
colorama.init()

def display(message, warning_status=False):
    if warning_status:
        print(colorama.Fore.RED+'Warning')
    print(colorama.Fore.GREEN+ message)
