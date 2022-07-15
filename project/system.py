from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from typing import List

from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        # опитваме се да филтрираме имена при hardware , ако не намерим нито едни име оставяме с празен лист , индекс 0 който не съществува
        #  и ще ни хвърли IndexError , но ако мине взимаме нулевия елемент и създаваме  software ExpressSoftware
        # създавайки софтуера се опитваме да инсталираме софтъера през install метода на Hardware  и ако нямамеме
        # достатъчни memory или capacity ще хвърли except str(ex) тъй като в самия инсталл метода имаме Exception
        # като минат успешно hardware sofware и install  тогава го append в _software
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum([h.memory for h in System._hardware])}\n"\
               f"Total Capacity Taken: {sum([h.used_capacity for h in System._hardware])} / {sum([h.capacity for h in System._hardware])} "

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"
            express_software_componets = [s for s in h.software_components if s.__class__.__name__ == "ExpressSoftware"]
            result += f"Express Software Components: {len(express_software_componets)}\n"
            light_software_componets = [s for s in h.software_components if s.__class__.__name__ == "LightSoftware"]
            result += f"Light Software Components: {len(light_software_componets)}\n"
            result += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}\n"
            result += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}\n"
            result += f"Type: {h.hardware_type}\n"
            names = ', '.join([s.name for s in h.software_components])
            result += f"Software Components: {names if names else None}\n"

        return result