class Employee(object):
    """員工類"""
    #is_leave=0 表示在職, 1表示離職
    def __init__(self, name, gender, age, mobile_number, is_leave = 0):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.is_leave = False if is_leave == 0 else True # is_leave=True表示離職,否則在職

    def __str__(self):
        msg = '離職' if self.is_leave else '在職'
        return f'{self.name}\t{self.age}\t{self.gender}\t{self.mobile_number}\t{msg}'

if __name__ == '__main__':
    e = Employee('張三','女',23,'12345')
    print(e.__dict__) # 1, 把python對象轉換成字典
    print(vars(e)) # 2, 把python對象轉換成字典
    e.is_leave = True
    print(e)

