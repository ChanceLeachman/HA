
from enum import Enum

class Key(Enum):
    POWER = 0x0
    SCHEDULE = 0x1
    SYSTEM = 0x3
    FAN_SPEED = 0x4
    FAN_MODE = 0x5
    UP = 0x6
    DOWN = 0x7

class FanMode(Enum):
    AUTO = 0x0
    CONTINUOUS = 0x2

class System(Enum):
    AUTO = 0x1
    COOL = 0x2
    HEAT = 0x3
    FAN = 0x4

class FanSpeed(Enum):
    # OFF = 0x1
    LOW = 0x2
    MED = 0x3
    HIGH = 0x4
    AUTO = 0x5

class Power(Enum):
    OFF = 0b0000
    ON = 0b1000

class Schedule(Enum):
    OFF = 0b0000
    ON = 0b0100

class Kuhl:

    def __init__(self):
        self.power = Power.ON
        self.schedule = Schedule.OFF
        self.auto_temp = 72
        self.heat_temp = 70
        self.cool_temp = 60
        self.key = Key.DOWN
        self.fan_mode = FanMode.CONTINUOUS
        self.system = System.COOL
        self.fan_speed = FanSpeed.MED

    def build(self):
        a = [
            self.key.value << 4 | 0x3, 
            0x0<< 4 | self.power.value ^ self.schedule.value ^ self.fan_mode.value,
            self.auto_temp,
            self.heat_temp,
            self.cool_temp,
            self.system.value <<4 | self.fan_speed.value
        ]
        return a
    
    def checksum(self, hex_array):
        return sum(hex_array) % 256
    
    def __repr__(self):
        hex_array = self.build()
        check_sum = self.checksum(hex_array)
        full_array = [check_sum] + hex_array
        print("hex", [hex(i) for i in full_array])
        binary_array = ['{:08b}'.format(i) for i in full_array]
        print("binary", binary_array)
        bits = "".join(binary_array)[::-1]
        return hex(int(bits, base=2))

kulh = Kuhl()
print(kulh)
