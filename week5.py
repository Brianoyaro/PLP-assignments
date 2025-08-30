class Device:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

class Smartphone(Device):
    def __init__(self, brand: str, model: str, os: str, battery: int = 100):
        super().__init__(brand, model)
        self.os = os
        self.__battery = battery   # this should throw an error when accessed outside this class because it is private
        self.apps = []

    def install_app(self, app_name: str):
        self.apps.append(app_name)
        return f"{app_name} installed on {self.info()}"

    def use_battery(self, amount: int):
        self.__battery = max(0, self.__battery - amount)
        return f"{self.info()} battery at {self.__battery}%"

    def charge(self):
        self.__battery = 100
        return f"{self.info()} fully charged!"

    # encapsulating battery
    def get_battery(self):
        return f"{self.info()} battery: {self.__battery}%"


class GamingPhone(Smartphone):
    def __init__(self, brand: str, model: str, os: str, battery: int = 100, cooling_system: bool = True):
        super().__init__(brand, model, os, battery)
        self.cooling_system = cooling_system

    def play_game(self, game: str):
        battery_message = self.use_battery(20)  # gaming consumes more power
        return f"Playing {game} on {self.info()} | {battery_message}"

phone1 = Smartphone("Samsung", "S23", "Android")
print(phone1.install_app("WhatsApp"))
print(phone1.use_battery(30))
print(phone1.get_battery())
print(phone1.charge())

gaming_phone = GamingPhone("Asus", "ROG Phone 7", "Android")
print(gaming_phone.install_app("PUBG"))
print(gaming_phone.play_game("Genshin Impact"))
print(gaming_phone.get_battery())

