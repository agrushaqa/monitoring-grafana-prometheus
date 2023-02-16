import psutil
import speedtest
from app.app_usage_net import AppUsageNet


class NetInfo:
    @staticmethod
    def get_internet_download_speed():
        st = speedtest.Speedtest()
        return st.download()

    @staticmethod
    def get_internet_upload_speed():
        st = speedtest.Speedtest()
        return st.upload()

    @staticmethod
    def get_app_usage_net():
        result = []
        for i in psutil.net_connections():
            result.append(AppUsageNet(ip=i.laddr.ip,
                                      port=i.laddr.port,
                                      app_name=psutil.Process(i.pid).name()))
        return result
