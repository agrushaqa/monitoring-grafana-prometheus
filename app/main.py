import platform

from app.memory_info import MemoryInfo

print(platform.system())

for i_partion in MemoryInfo.get_list_partions():
    print(MemoryInfo.get_free_space(i_partion) / 1024 / 1024)
