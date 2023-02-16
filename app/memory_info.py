import shutil
import socket

import psutil


class MemoryInfo:
    @staticmethod
    def get_computer_name():
        return socket.gethostname()

    @staticmethod
    def get_list_partions():
        result = []
        for i_partition in psutil.disk_partitions():
            if len(i_partition.fstype) > 0:
                result.append(i_partition.mountpoint)
        return result

    @staticmethod
    def get_cpu_percent():
        return psutil.cpu_percent(4)

    @staticmethod
    def get_ram_percent():
        return psutil.virtual_memory()[2]

    @staticmethod
    def get_free_space(partition: str):
        return shutil.disk_usage(partition).free

    @staticmethod
    def get_full_space(partition: str):
        return shutil.disk_usage(partition).total
