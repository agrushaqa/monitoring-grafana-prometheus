from app.memory_info import MemoryInfo
import socket
import pytest


class TestMemoryInfo:

    def test_computer_name(self):
        assert MemoryInfo.get_computer_name() == socket.gethostname()
