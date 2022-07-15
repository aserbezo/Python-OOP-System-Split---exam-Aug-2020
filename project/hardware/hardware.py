from project.software.software import Software
from typing import List


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        # using a Typing list to display software attributes
        self.software_components: List[Software] = []

    @property
    def available_memory(self):
        return self.memory - self.used_memory

    @property
    def available_capacity(self):
        return self.capacity - self.used_capacity

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

    # tipizaciq
    def install(self, software: Software):
        if software.capacity_consumption <= self.available_capacity and \
                software.memory_consumption <= self.available_memory:

            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

# h = Hardware("a","a", 200,500)
# a = Software("name","type", 100,200)
#
# h.uninstall(a)
