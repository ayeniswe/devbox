from enum import StrEnum


class Platform():
    """
    Platform is responsible for detecting the current system's OS and architecture
    to aid in platform-specific logic and deployment handling.
    """

    def __init__(self):
        self.os = self._detect_os()
        self.arch = self._detect_arch()

    def _detect_os(self):
        from sys import platform
        if platform.startswith("win"):
            return Os.Windows
        elif platform.startswith("darwin"):
            return Os.Mac
        else:
            return Os.Linux  # default fallback

    def _detect_arch(self):
        import platform as py_platform
        machine = py_platform.machine().lower()
        if "arm64" in machine or "aarch64" in machine:
            return Arch.Arm64
        elif "arm" in machine:
            return Arch.Arm32
        elif "x86_64" in machine or "amd64" in machine:
            return Arch.X86_64
        elif "x86" in machine or "i386" in machine:
            return Arch.X86
        else:
            return Arch.NoArch

    def __str__(self):
        return f"Platform OS: {self.os}\nPlatform Arch: {self.arch}"


class Os(StrEnum):
    """Operating System"""
    Windows = "Windows"
    Linux = "Linux"
    Mac = "Mac"


class Arch(StrEnum):
    """Platform architecture"""
    Arm64 = "ARM64"
    Arm32 = "ARM32"
    X86_64 = "X86_64"
    NoArch = "NOARCH"
    X86 = "X86"
    X64 = "X64"


class Context():
    """
    Context is responsible for exposing deployment environment information
    so other components can respond appropriately in dynamic conditions.
    """
    is_online: bool
    platform: Platform

    def __init__(self):
        self.is_online = self._is_online()
        self.platform = Platform()

    def _is_online(self):
        import socket
        try:
            # Arbitrary connection just to
            # test we can reach online by
            # hitting Google's DNS servers
            socket.create_connection(("8.8.8.8", 53))
            return True
        except Exception:
            return False
