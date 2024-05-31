
from datetime import datetime

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lenguage Uzbek>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

user_info = {
    "first_name": "Muhammadxon", "last_name": "Asrorov",
    "card_password": "0000", "card_balance": 10000000,
    "card_number" :"8600963096308520",
    "phone_number": "", "status": False}
data_atm = {"balance": 5000000}

def kod_almashtirish():
    joriy = input("<<<<<<Joriy pin codni kiriting>>>>>> ")
    j = 2
    while user_info["card_password"] != joriy and j != 0:
        j -= 1
        joriy = input("<<<<<<Iltimos joriy pin codni kiriting>>>>>> ")

    if joriy == user_info["card_password"]:
        yangi = input("<<<<<<Yangi pin codni kiriting>>>>>> ")
        j1 = 2
        while len(yangi) != 4 and j1 != 0:

            j1 -= 1
            yangi = input("<<<<<<Iltimos to'g'ri kriting>>>>>> ")

        if len(yangi) == 4:
            user_info.update({"card_password": yangi})
            yana = input(f"""
                    <<<<<< Xizmat muvaffaqiyatli tarzda yakunlandi >>>>>>
                            Boshqa servisdan foydalanishni istaysizmi?
                                1. Ha
                                2. Yo'q  """)

            if yana == "1":
                return uzbek_services()
            elif yana == "2":
                return main()
            else:
                print("Error")
                return main()

        print("Iltimos qaytadan urinib ko'ring!")
        return main()

    print("<<<<<<<Sizning kartangiz bloklandi!>>>>>>>")
    return main()




def en_add_money():
    print("<<<Add money>>>")
    en_money = input("Enter value: ")
    if en_money.isalnum():
        user_info["card_balance"] += int(en_money)
        data_atm["balance"] += int(en_money)
        print("Successfull")
        return english_services()
    else:
        print("Error")
        return main()

def eng_sms_off():
    if user_info["status"] == True:
        print("Succesful!")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return english_services()
    else:
        print("The number has not connected yet")
        return english_services()
def eng_sms_on():
    if user_info["status"] == False:
        number_phone = input(f"""
                    Enter your phone number: 
                        +998 _ >>>> """)
        if len(number_phone) == 9:
            user_info["phone_number"] = number_phone
            user_info["status"] = True
            print("Succesful!")
            return english_services()
        else:
            print("Error")
            return eng_sms_on()
    else:
        print("The number has already connected")
        return english_services()

def sms_message():
    print("<<<Short message service>>>")
    print(f"""
            Status: {user_info["status"]}
            Phone Number {user_info["phone_number"]}
            """)
    servant = input("""
            1. SMS message connect
            2. SMS message delete
                >>> """)
    if servant == "1":
        return eng_sms_on()
    elif servant == "2":
        return eng_sms_off()
    else:
        print("Error")
        return main()
def cash_withdrawl(cash_money):
    procent = cash_money * 1.01
    if user_info["card_balance"] > procent and data_atm["balance"] >= cash_money:
        confirm = input(f"""
                    Money withdrawnn from the card {procent}

                            1. Continue
                            2. Cancel>>> """)
        if confirm == "1":
            user_info["card_balance"] -= procent
            data_atm["balance"] -= cash_money
            print("The operationn was succesfully copleted!")
            get_cheque = input(f"""
                        Do you want to get a cheque
                                1. Yes. I get
                                2. No. thanks>>> """)
            if get_cheque == "1":

                print(f"""
                                CHEQUE

                Balance: {user_info["card_balance"]}
                Card: {12 * "*" + user_info["card_number"][-4::]}
                Time: {datetime.now()}""")

            elif get_cheque == "2":
                print("Cancel")
                return main()
            else:
                print("Error")
                return english_cash()

        else:
            print("Error")
            return english_services()




def english_cash():
    print("<<<<<Cash>>>>>>")
    cash = input("""
        Summani tanlang:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Boshqa summa
            0. Orqaga
                >>> """)

    if cash == "1":
        return cash_withdrawl(50000)
    elif cash == "2":
        return cash_withdrawl(100000)
    elif cash == "3":
        return cash_withdrawl(200000)
    elif cash == "4":
        return cash_withdrawl(300000)
    elif cash == "5":
        return cash_withdrawl(400000)
    elif cash == "6":
        cash_money = input("Summani kiriting: ")
        return cash_withdrawl(int(cash_money))


def english_balance_cheque():
    cheque = f"""
                CHEQUE
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    return main()


def en_change_password():
    x1 = input("<<<<<<Enter pin code>>>>>> ")
    x2 = 2
    while user_info["card_password"] != x1 and x2 != 0:
        x2 -= 1
        x1 = input("<<<<<<Please enter pin code>>>>>> ")

    if x1 == user_info["card_password"]:
        new = input("<<<<<<Yangi pin codni kiriting>>>>>> ")
        x3 = 2
        while len(new) != 4 and x3 != 0:

            x3 -= 1
            yangi = input("<<<<<<Please enter true pin code>>>>>> ")

        if len(new) == 4:
            user_info.update({"card_password": new})
            again = input(f"""
                    <<<<<< The service has been succesfully >>>>>>
                            Do you want another services?
                                1. Yes
                                2. No  """)

            if again == "1":
                return uzbek_services()
            elif again == "2":
                return main()
            else:
                print("Error")
                return main()

        print("Please try again!")
        return main()

    print("<<<<<<<Your card have been blocked!>>>>>>>")
    return main()





def english_balance_screen():
    screen = input(f"""
    You have {user_info["card_balance"]} so'm
    Did you want to use other services?
        1. Yes
        2. No
            >>> """)
    if screen == "1":
        return english_services()

    elif screen == "2":
        return main()

    else:
        print("Error")
        return main()

def english_balance():
    print("<<<English balance>>>")
    english = input(f"""
                1. View on the screen 
                2. View on the cheque>>> """)

    if english == "1":
        return english_balance_screen()
    elif english == "2":
        return english_balance_cheque()
    else:
        print("Error")
        return english_services()


def english_services():
    print("<<<<<Service page>>>>>")
    service = input(f"""
    <<<Choose the type of services>>>

            1. Balance
            2. Cash withdrawl
            3. SMS message
            4. Fill out the card
            5. Change pin code
            0. Back>>> """)
    if service == "1":

        return english_balance()

    elif service == "2":

        return english_cash()

    elif service == "3":

        return sms_message()

    elif service == "4":

        return en_add_money()

    elif service == "5":

        return en_change_password()

    elif service == "0":

        return main()

    else:
        print("Error")
        return main()




def uzbek_balance_display():
    a = input(f"""
    Sizning balansingiz {user_info["card_balance"]} so'm
    Boshqa xizmatdan foydalanishni istaysizmi?
        1. Ha
        2. Yo'q
            >>> """)

    if a == "1":
        return uzbek_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return uzbek_balance_display()

def uzbek_balance_check():
    print("Bizni tanlaganiz uchun tashakkur")
    check = f"""
                CHEQUE
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()

def uzbek_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. Ekranda ko'rish
        2. Chekda ko'rish
            >>> """)
    if services == "1":
        return uzbek_balance_display()

    elif services == "2":
        return uzbek_balance_check()

def check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        Kartadan yechiladigan summa {m}
                            1. Davom etish
                            2. Bekor qilish
                                >>> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("Amaliyot muvaffaqiyatli yakunlandi")
            chek1 = input(f"""
                        Chek olishni xoxlaysizmi?
                                1. Ha. olaman
                                2. Yo'q rahmat>>> """)
            if chek1 == "1":
                print(f"""
                                CHEQUE

                Balance: {user_info["card_balance"]}
                Card: {12 * "*" + user_info["card_number"][-4::]}
                Time: {datetime.now()}""")
            elif chek1 == "2":
                print("Bekor qilindi")
                return main()

        elif tasdiq == "2":
            print("Xizmat bekor qilindi")
            return uzbek_services()

        else:
            print("Error")
            return uzbek_service_money()

    else:
        print("Xatolik!!!")
        return main()


def uzbek_service_money():
    money = input("""
        Summani tanlang:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Boshqa summa
            0. Orqaga
                >>> """)

    if money == "1":
        return check_balance(50000)

    elif money == "2":
        return check_balance(100000)

    elif money == "3":
        return check_balance(300000)

    elif money == "4":
        return check_balance(400000)

    elif money == "6":
        money = input("""Summani kiriting: """)
        return check_balance(int(money))

    elif money == "0":
        return uzbek_services()

    else:
        print("Error")
        return uzbek_service_money

def uz_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            Telefon raqamingizni kiriting: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return uzbek_services()
        else:
            print('Xatolik')
            return uz_sms_on()
    else:
        print("Bu raqamga allaqachon sms xabarnoma ulangan")
        return uzbek_services()

def uz_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return uzbek_services()

    else:
        print("Bu raqamga allaqachon sms xabarnoma ulanmagan")
        return uzbek_services()

def uzbek_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. SMS Xabarnomani ulash
        2. SMS Xabarnomani o'chirish
            >>> """)
    if service == "1":
        return uz_sms_on()

    elif service == "2":
        return uz_sms_off()
    else:
        print("Error")
        return main()


def uzbek_service_add_money():
    print("ADD")
    money = input("Summani kiriting: ")
    if money.isalnum():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return uzbek_services()
    else:
        print("Error")
        return uzbek_service_money()

def uzbek_services():
    print("Service Page")
    services = input("""
        Xizmat turini tanglang:
            1. Balanceni ko'rish
            2. Naqt pul yechish
            3. SMS Xabarnoma
            4. Kartani to'ldirish
            5. Pin codni o'zgartirish
            0. Back
                >>> """)

    if services == "1":
        return uzbek_service_balance()

    elif services == "2":
        return uzbek_service_money()

    elif services == "3":
        return uzbek_service_sms()

    elif services == "4":
        return uzbek_service_add_money()

    elif services == "5":
        return kod_almashtirish()

    elif services == "0":
        print("Bizni tanlaganiz uchun tashakkur!")
        return main()

    else:
        print("Bunday xizmat turi mavjud emas")
        return uzbek_services()


def uzbek():
    print("<<<<<<<<<<<<<<Uzbek Lenguage>>>>>>>>>>>>>>>>")
    password = input("Pin codeni kiriting: ")
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = input("Pin codeni kiriting: ")
        n -= 1

    if user_info["card_password"] == password:
        return uzbek_services()

    print("Sizning Kartangiz bloklandi")
    return main()

def english():
    print("<<<<<<<<<<<<<<English Lenguage>>>>>>>>>>>>>>>>")

    password2 = input("Enter pin code ")
    n2 = 2
    while user_info["card_password"] != password2 and n2 != 0:
        print("Error")
        password2 = input("Enter pin code")
        n2 -= 1
    if user_info["card_password"] == password2:
        return english_services()

    print("Your card have been blocked")
    return main()

def russian_service():
    print("Stranitsa uslugi")
    services3 = input("""
        Пожалуйста, введите действительный пин-код:
            1. Проверьте баланс
            2. Выдача наличных
            3. СМС-уведомление
            4. Заполнение карты
            5. Изменить пин-код
            0. назад
                >>> """)

    if services3 == "1":
        return rus_service_balance()

    elif services3 == "2":
        return rus_service_money()

    elif services3 == "3":
        return rus_service_sms()

    elif services3 == "4":
        return rus_add_money()

    elif services3 == "5":
        return rus_change_pin()

    elif services3 == "0":
        return main()

def rus_change_pin():
    y1 = input("<<<<<<Bведите действительный пин-код>>>>>> ")
    y2 = 2
    while user_info["card_password"] != y1 and y2 != 0:
        y2 -= 1
        y1 = input("<<<<<<Пожалуйста, введите действительный пин-код>>>>>> ")

    if y1 == user_info["card_password"]:
        novy = input("<<<<<<Введите новый пин-код>>>>>> ")
        y = 2
        while len(novy) != 4 and y != 0:

            y -= 1
            novy = input("<<<<<<Пожалуйста, введите правильно>>>>>> ")

        if len(novy) == 4:
            user_info.update({"card_password": novy})
            yesho = input(f"""
                    <<<<<< Служба успешно завершена >>>>>>
                            Хотите воспользоваться другой услугой??
                                1. Ha
                                2. Yo'q  """)

            if yesho == "1":
                return russian_service()
            elif yesho == "2":
                return main()
            else:
                print("Ошибка")
                return main()

        print("Пожалуйста, попробуйте еще раз!")
        return main()

    print("<<<<<<<Ваша карта заблокирована!>>>>>>>")
    return main()

def rus_service_sms():
    print("SMS")
    print(f"""
            Положение дел: {user_info["status"]}
            Номер телефона: {user_info["phone_number"]}
            """)
    service = input("""
            1. SMS-уведомления о подключении
            2. SMS-уведомление o удалить
                >>> """)
    if service == "1":
        return rus_sms_on()

    elif service == "2":
        return rus_sms_off()
    else:
        print("Ошибка")
        return main()

def rus_sms_on():
    if user_info["status"] == False:
        phone_number2 = input("""
            Введите свой номер телефона: 
                +998 _ >>> """)
        if len(phone_number2) == 9:
            user_info["phone_number"] = phone_number2
            user_info["status"] = True
            print("Успешный")
            return russian_service()
        else:
            print('Ошибка')
            return rus_sms_on()
    else:
        print("СМС подключено к этому номеру")
        return russian_service()

def rus_sms_off():
    if user_info["status"] == True:
        print("Успешный")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return russian_service()

    else:
        print("СМС еще не подключено к этому номеру")
        return russian_service()


def rus_add_money():
    print("<<<Добавить деньги>>>")
    ru_money = input("Введите значение: ")
    if ru_money.isalnum():
        user_info["card_balance"] += int(ru_money)
        data_atm["balance"] += int(ru_money)
        print("Успешный")
        return russian_service()
    else:
        print("Ошибка")
        return main()





def rus_service_money():
    money3 = input("""
            Выберите сумму:
                1. 50.000
                2. 100.000
                3. 200.000
                4. 300.000
                5. 400.000
                6. Drugoy summa
                0. назад
                    >>> """)

    if money3 == "1":
        return check_balance(50000)

    elif money3 == "2":
        return check_balance(100000)

    elif money3 == "3":
        return check_balance(300000)

    elif money3 == "4":
        return check_balance(400000)

    elif money3 == "6":
        money3 = input("""Введите сумму: """)
        return check_balance(int(money3))

    elif money3 == "0":
        return russian_service()

    else:
        print("Ошибка")
        return rus_service_money


def rus_service_balance():
    print("<<<<<<<<<Баланс>>>>>>>>")
    services = input("""
            1. Посмотреть на экране
            2. Посмотреть на чек
                >>> """)
    if services == "1":
        return rus_balance_display()

    elif services == "2":
        return rus_balance_check()
def rus_balance_display():
    a2 = input(f"""
        На вашем балансе {user_info["card_balance"]} сум
        Хотите воспользоваться другой услугой?
            1. Да
            2. Нет
                >>> """)

    if a2 == "1":
        return russian_service()

    elif a2 == "2":
        return main()

    else:
        print("Ошибка")
        return rus_balance_display()


def rus_balance_check():
    check1 = f"""
                    Квинтанция
            Баланс: {user_info["card_balance"]}
            Карта: {12 * "*" + user_info["card_number"][-4::]}
            Время: {datetime.now()}
        """
    print(check1)
    return main()

def russian():
    print("<<<<<<<<<<<<<<русский язык>>>>>>>>>>>>>>>>")

    password3 = input("Введите пин-код ")
    n3 = 2
    while user_info["card_password"] != password3 and n3 != 0:
        print("Ошибка")
        password3 = input("Введите пин-код ")
        n3 -= 1
    if user_info["card_password"] == password3:
        return russian_service()

    print("Ваша карта заблокирована ")
    return main()
def main():
    lenguage = input("""
        Tilni tanglang:
            1. Uzbek
            2. English
            3. Russian
                >>> """)

    if lenguage == "1":
        return uzbek()

    elif lenguage == "2":
        return english()

    elif lenguage == "3":
        return russian()

    else:
        print("Bunday til mavjud emas")
        return main()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lenguage English>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





if __name__ == "__main__":
    main()

