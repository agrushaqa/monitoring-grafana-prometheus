import platform

from memory_info_windows import MemoryInfoWindows

print(platform.system())

for i_partion in MemoryInfoWindows.get_list_partions():
    print(MemoryInfoWindows.get_free_space(i_partion) / 1024 / 1024)
