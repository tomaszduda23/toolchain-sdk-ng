import os
import tarfile
import urllib.request
import platform

VERSION = "0.16.1"
BASE_URL = "https://github.com/zephyrproject-rtos/sdk-ng/releases/download"
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
TOOLCHAIN_INSTALLED = os.path.join(ROOT_DIR, "toolchain_installed")

if os.path.isfile(TOOLCHAIN_INSTALLED):
    exit(0)

def unpack_remote(url, destination):
    local_path = os.path.join(ROOT_DIR, os.path.basename(url))
    urllib.request.urlretrieve(url, local_path)
    tarfile.open(local_path, "r:xz").extractall(destination)
    os.remove(local_path)

unpack_remote(f"{BASE_URL}/v{VERSION}/zephyr-sdk-{VERSION}_linux-{platform.machine()}_minimal.tar.xz", ROOT_DIR)
unpack_remote(f"{BASE_URL}/v{VERSION}/toolchain_linux-{platform.machine()}_arm-zephyr-eabi.tar.xz", os.path.join(ROOT_DIR, f"zephyr-sdk-{VERSION}"))

print("Toolchain installed")
open(TOOLCHAIN_INSTALLED, "x")

