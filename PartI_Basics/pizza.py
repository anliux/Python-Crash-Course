# 8.6章 - import测试 

# pizza.py
# 包含模块make_pizza

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print('\nMaking a ' + str(size) +
         '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)