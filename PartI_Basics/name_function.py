# name_function.py 最终的样子
def get_formatted_name(first, last, middle=''):
    # 改为可妥善处理中间名的，即当没有中间名时也不会报错
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last 
    return full_name.title()