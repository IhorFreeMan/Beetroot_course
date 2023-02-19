# -*- coding: utf-8 -*-
class Gun:
    def __init__(self, name):
        self.name = name
        self.shoot_sound = "BAAANG"

    def shoot(self):
        return self.shoot_sound

    def __str__(self):
        return f"{self.name}"


class Human:
    def __init__(self, name):
        self.name = name
        self.gun = None
        self.life_status = "alive"

    def kill_human_with_gun(self, human):
        if self.gun is None:
            raise RuntimeError("Oh no, i don`t have a gun")
        self.gun.shoot()
        human.die()

    def die(self):
        self.life_status = "dead"

    def take_gun(self, gun):
        self.gun = gun

    def __str__(self):
        return f"{self.name} is holding {self.gun}"


if __name__ == "__main__":
    glock = Gun("glock")
    winsent = Human("Winsent")
    winsent.take_gun(glock)
    print(winsent.name, "took", glock)

    beretta = Gun("beretta")
    juls = Human("Juls")
    juls.take_gun(beretta)
    print(juls.name, "took", beretta)

    print(f"{winsent}\n{juls}")

    print(juls.name, "shoots:", juls.gun.shoot())

    guy = Human("Unknown guy")
    juls.kill_human_with_gun(guy)
    print(f"{guy.name} is {guy.life_status}")
