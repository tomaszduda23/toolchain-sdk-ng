import os
import tarfile
import urllib.request
import urllib.error
import platform

VERSION = "0.17.0"
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

sysname = platform.system().lower()
if sysname == "darwin":
    sysname = "macos"
machine = platform.machine()
if machine == "arm64":
    machine = "aarch64"
sys_machine = f"{sysname}-{machine}"

try:
    unpack_remote(f"{BASE_URL}/v{VERSION}/zephyr-sdk-{VERSION}_{sys_machine}_minimal.tar.xz", ROOT_DIR)
    unpack_remote(f"{BASE_URL}/v{VERSION}/toolchain_{sys_machine}_arm-zephyr-eabi.tar.xz", os.path.join(ROOT_DIR, f"zephyr-sdk-{VERSION}"))
except urllib.error.HTTPError as e:
    print(f"Error downloading sdk or toolchain from {BASE_URL}/v{VERSION}/zephyr-sdk-{VERSION}_{sys_machine}_minimal.tar.xz", ROOT_DIR)
    exit(1)

print("Toolchain installed")
open(TOOLCHAIN_INSTALLED, "x")
