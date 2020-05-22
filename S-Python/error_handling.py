
def demo_deviding(x, y):
    try:
        print(x / y)
    except ZeroDivisionError as e:
        print('Sorry Something wemt wrong' + str(e))
    except:
        print('Something Really went wrong')
    finally:
        print('Finally it always run')


print('Hello From Error handling')
x = int(input('Input Value of X '))
y = int(input('Input Value of Y '))
demo_deviding(x, y)
