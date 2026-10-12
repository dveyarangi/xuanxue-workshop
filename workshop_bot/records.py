import ctypes
import os
from contextlib import contextmanager


@contextmanager
def exclusive_record(path):
    """Deny competing writes, truncation and replacement, including non-cooperating editors."""
    if os.name != "nt":
        raise OSError("Record writes are qualified for Windows only")
    import msvcrt
    from ctypes import wintypes

    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    create = kernel.CreateFileW
    create.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
                       wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
    create.restype = wintypes.HANDLE
    close = kernel.CloseHandle
    close.argtypes = [wintypes.HANDLE]
    close.restype = wintypes.BOOL
    handle = create(str(path), 0x80000000 | 0x40000000, 1, None, 3, 0x80, None)
    if handle == wintypes.HANDLE(-1).value:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        final_name = kernel.GetFinalPathNameByHandleW
        final_name.argtypes = [wintypes.HANDLE, wintypes.LPWSTR, wintypes.DWORD, wintypes.DWORD]
        final_name.restype = wintypes.DWORD
        buffer = ctypes.create_unicode_buffer(32768)
        count = final_name(handle, buffer, len(buffer), 0)
        if not count or count >= len(buffer):
            raise ctypes.WinError(ctypes.get_last_error())
        actual = buffer.value.removeprefix("\\\\?\\")
        if actual.startswith("UNC\\"):
            actual = "\\\\" + actual[4:]
        if os.path.normcase(actual) != os.path.normcase(str(path)):
            raise ValueError("Opened record is not the selected path")
        descriptor = msvcrt.open_osfhandle(handle, os.O_RDWR | os.O_BINARY)
    except BaseException:
        close(handle)
        raise
    with os.fdopen(descriptor, "r+b") as record:
        yield record
