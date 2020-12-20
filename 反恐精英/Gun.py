
class Gun:
    def __init__(self, modal, damage):
        self.modal = modal  # 型号
        self.damage = damage  # 伤害
        self.bullet_count = 0  # 剩余子弹数量

    def add_bullets(self, count):
        """装填子弹

        :param count:装填的子弹数量
        """
        self.bullet_count += count
        print(f"装填子弹完成, 剩余子弹数量: {self.bullet_count}")

    def shoot(self, enemy):
        """

        :type enemy: object
        """
        if self.bullet_count == 0:
            print("子弹数量为0,无法射击")
        else:
            self.bullet_count -= 1
            # TODO 敌人受伤
            enemy.hurt(self.damage)

    def __str__(self):
        return f"{self.modal}: {self.damage}, 剩余子弹:{self.bullet_count}"

class Player:
    def __init__(self,name):
        self.name = name  # 角色
        self.gun = None  # 枪
        self.hp = 100  # 血量

    def fire(self, enemy):
        """攻击敌人"""
        if self.gun is None:  # 没有枪
            print("没有枪, 用眼神杀死他")
        else:  # 有枪
            if self.gun.bullet_count > 0:  # 有子弹,用枪射击
                self.gun.shoot(enemy)
            else:  # 没有子弹,自动添加子弹
                self.gun.add_bullets(30)

    def hurt(self, gun_damage):
        """受伤"""
        self.hp -= gun_damage
        if self.hp > 0:
            print(f"玩家受伤, 血量:{self.hp}")
        else:
            print("玩家死亡")

    def __str__(self):
        if self.hp > 0:
            return f"玩家:{self.name}, 血量:{self.hp}, 枪:{self.gun}"
        else:
            return f"玩家:{self.name} 死亡"

def test():
    """测试函数"""
    ak47 = Gun("ak47", 40)
    badman = Player("匪徒")
    print(badman)
    policeman = Player("警察")
    print(policeman)
    policeman.gun = ak47

    for _ in range(3):
        policeman.fire(badman)
    print(policeman)
    print(badman)


if __name__ == '__main__':
    test()