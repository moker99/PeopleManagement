from employee import Employee
import os


class EmployeeManagerSystem(object):
    # 存放員工數據文件
    employee_data_file = 'employee.data'

    def __init__(self):
        # 存放員工數據文件
        self.employee_data_file = 'employee.data'
        # 上次保存前的員工備份文件，而且只備份1份
        self.employee_data_file_backup = 'employee.data.backup'
        self.employee_list = []  # 從文件中加載之後的員工列表
        self.save_flag = True  # 已經保存員工數據

    def main(self):
        """員工管理系統的入口"""
        # 1. 加載和讀取員工數據文件
        self.load_employee()
        while True:
            # 2. 顯示系統歡迎介面
            self.show_hello()

            # 3. 由用戶輸入指定的功能數字
            menu_number = int(input('請輸入你需要的功能編號:'))
            if menu_number == 7:
                self.go_out()
                break
            elif menu_number == 1:
                self.add_employee()
            elif menu_number == 2:
                self.del_employee()
            elif menu_number == 3:
                self.update_employee()
            elif menu_number == 4:
                self.search_employee()
            elif menu_number == 5:
                self.show_all()
            elif menu_number == 6:
                self.save_employee()

    def go_out(self):
        """
        退出程序的需求:如果員工進行了添加、修改、刪除。那必須造保存到文件中
        1. 如果沒有保存.則在退出之前要保存
        2. 怎麼樣: 確定沒有保存呢 ?
        :return:
        """
        if not self.save_flag:  # 員工數據沒有保存
            self.save_employee()
        print('謝謝! 程序退出')

    def save_employee(self):
        """
        保存的需求和步驟:
        1. 先把原來的數據文件備份 (如果已經存在備份文件，則把備份文件刪除)
        2. 創建新文件
        3. 寫入數據
        4. 關閉文件
        :return:
        """
        if os.path.exists(self.employee_data_file_backup):
            os.remove(self.employee_data_file_backup)  # 刪除備份文件
        # 1. 備份
        os.rename(self.employee_data_file, self.employee_data_file_backup)
        # 2. 打開文件流
        with open(self.employee_data_file, 'w', encoding='utf-8') as f:
            # 3. 寫入數據
            new_list = []
            for emp in self.employee_list:  # 原來的列表中是一個個的emp對象
                new_list.append(emp.__dict__)
            # new_list:[{'name':zs...},{},{}]
            f.write(str(new_list))
        self.save_flag = True  # 剛剛已經保存過了

    def show_all(self):
        """展示所有的員工信息"""
        print('姓名\t年齡\t性別\t手機號\t是否離職')
        for emp in self.employee_list:
            print(emp)

    def search_employee(self):
        """根據姓名，查找員工信息"""
        # 1. 輸入員工姓名
        search_name = input('請輸入要查詢的員工姓名:')
        # 2. 遍歷員工列表, 判斷是否存在, 存在則
        for emp in self.employee_list:
            if emp.name == search_name:
                print(emp)
                break
        else:
            print(f'沒有找到名字叫{search_name}的員工')

    def update_employee(self):
        """
        修改員工: 首先需要輸入員工姓名，然後再依修改該員工的屬性
        :return:
        """
        # 1. 輸入員工姓名
        update_name = input('請輸入要修改的員工姓名:')
        # 2. 遍歷員工列表, 判斷是否存在, 存在則修改
        for emp in self.employee_list:
            if emp.name == update_name:
                self.save_flag = False  # 你完成了一次修改，必須保存數據
                # 3. 修改員工其他屬性
                new_name = input('請輸入新的姓名(不修改直接enter)').strip()
                emp.name = new_name if new_name else emp.name

                new_sex = input('請輸入新的性別(不修改直接enter)').strip()
                emp.gender = new_sex if new_sex else emp.gender

                new_age = input('請輸入新的年齡(不修改直接enter)').strip()
                emp.age = int(new_age) if new_age else emp.age

                new_number = input('請輸入新的手機號碼(不修改直接enter)').strip()
                emp.mobile_number = new_number if new_number else emp.mobile_number

                new_leave = input('請輸入是否離職訊，1表示離職、0表示在職(不修改直接enter)').strip()
                if new_leave:
                    emp.is_leave = True if int(new_leave) == 1 else False
                print('員工的信息已經修改完成:')
                print(emp)
                break
        else:
            print(f'沒有找到名字叫{update_name}的員工')

    def del_employee(self):
        """
        刪除員工的徐球: 首先輸入一個被刪除的員工姓名
        :return:
        """
        # 1. 輸入被刪除員工姓名
        del_name = input('請輸入要刪除的員工姓名:')
        # 遍歷員工列表, 判斷是否存在, 存在則刪除
        for emp in self.employee_list:
            if emp.name == del_name:
                self.save_flag = False  # 你完成了一次修改，必須保存數據
                self.employee_list.remove(emp)
                print(f'名字叫:{del_name}的員工已經刪除')
                break
        else:
            print(f'沒有找到名字叫{del_name}的員工')

    def add_employee(self):
        """添加員工訊息"""
        # 1. 由用戶輸入你需要添加員工訊息
        name = input('請輸入員工的姓名:')
        gender = input('請輸入員工的性別:')
        age = int(input('請輸入員工的年齡:'))
        mobile_number = input('請輸入員工的手機號碼:')
        is_leave = int(input('請輸入員工是否離職,1表示離職,0表示在職:'))

        # 2. 創建一個員工對象
        emp = Employee(name, gender, age, mobile_number, is_leave)
        self.save_flag = False  # 你完成了一次修改，必須保存數據
        # 3. 把新加入的員工添加到列表中
        self.employee_list.append(emp)

        # 4. 把剛剛添加的員工訊息，輸出
        print(emp)

    @staticmethod
    def show_hello():
        """顯示系統的歡迎介面"""
        print('歡迎進入企業員工管理系統')
        print('-' * 60)
        print('1:添加員工')
        print('2:刪除員工')
        print('3:修改員工')
        print('4:查找員工')
        print('5:展示員工')
        print('6:保存員工')
        print('7:退出系統')
        print('-' * 60)

    def load_employee(self):
        """
        讀取員工數據文件, 把所有的員工信息都放到一個列表中
        :return:
        """
        try:
            f = open(self.employee_data_file, 'r', encoding='utf-8')
        except Exception as err:
            # 如果抱錯, 很有可能第一次啟動程序,這個文件還不存在,需要創建一下
            f = open(self.employee_data_file, 'w', encoding='utf-8')
        else:  # 沒有抱錯,意味著文件存在
            # 讀取文件中的數據
            data = f.read()
            if data:
                lst = eval(data)  # 把文件的內容(字符串), 當成python表達式解析
                for dict1 in lst:
                    self.employee_list.append(
                        Employee(dict1['name'], dict1['gender'], dict1['age'], dict1['mobile_number'],
                                 dict1['is_leave']))
        finally:
            if f:
                f.close()


if __name__ == '__main__':
    s = EmployeeManagerSystem()
    s.main()
