# модуль 

def import_data(data, sep=None):
    with open(r'C:\Users\79104\Desktop\GeekBrains materials\Programming\Python_lessons\home_work_python\home_work7\phone.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")