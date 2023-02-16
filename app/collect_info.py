import yaml
from battery_info import get_battery_percent
from memory_info import MemoryInfo
from netinfo import NetInfo


class CollectInfo:
    yml_memory_info = "memory_info"
    yml_ram_percent = "ram_percent"
    yml_free_space = "free_space"
    yml_cpu_percent = "cpu_percent"

    def __init__(self, config_file=""):
        self.yaml_content = ""
        if len(config_file) > 0:
            with open(config_file, 'r') as file:
                self.yaml_content = yaml.safe_load(file)

    @staticmethod
    def print_data_for_all_paritions(method, divider=1):
        result = ""
        for i_partition in MemoryInfo.get_list_partions():
            result += i_partition
            result += ": "
            result += str(method(i_partition) / divider)
            result += "\n        "
        return result

    @staticmethod
    def print_app_and_net_port():
        result = "\n        ------------------------------------------\n"
        result += "\n        "
        result += "{:<20} {:<20} {:<20}".format(
            "application name",
            "port",
            "ip")
        result += "\n        ------------------------------------------\n"
        result += "\n        "
        for i_app in NetInfo.get_app_usage_net():
            result += "{:<20} {:<20} {:<20}".format(
                i_app.app_name,
                i_app.port,
                i_app.ip)
            result += "\n        "
        return result

    def __str__(self):
        return f'''
        computer_name: {MemoryInfo.get_computer_name()}
        cpu_percent: {MemoryInfo.get_cpu_percent()}
        ram_percent: {MemoryInfo.get_ram_percent()}
        free_space (MB):
        {self.print_data_for_all_paritions(MemoryInfo.get_free_space,
                                           1024 * 1024)}
        full_space (MB):
        {self.print_data_for_all_paritions(MemoryInfo.get_full_space,
                                           1024 * 1024)}
        battery_percent: {get_battery_percent()}
        download_speed: {
        NetInfo.get_internet_download_speed() / 1024 / 1024} MB
        application which use network: {self.print_app_and_net_port()}
        '''


if __name__ == "__main__":
    print(CollectInfo())
