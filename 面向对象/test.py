class People:

    def __init__(self):
        self.money = 0  # 账户余额

    def send_msg(self):
        if self.money >= 1:
            self.__send_msg()
        else:
            print("余额不足,请充值")

    def __send_msg(self):
        print("发送短信")


xiaoming = People()
xiaoming.send_msg()
xiaoming.money = 50
xiaoming.send_msg()