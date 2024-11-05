import subprocess
import sys
import platform
from datetime import datetime

# Function to install psutil if not already installed
def install_psutil():
    try:
        import psutil
        return True  # Return True if psutil is already installed
    except ImportError:
        print("psutil not found. Installing...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])
        return True  # Return True after installation

# Import psutil after ensuring it is installed
if install_psutil():
    import psutil  # Import here after installation check

def get_system_info():
    uname = platform.uname()
    print("="*40, "System Information", "="*40)
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def get_boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print("="*40, "Boot Time", "="*40)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

def get_cpu_info():
    print("="*40, "CPU Info", "="*40)
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def get_memory_info():
    memory = psutil.virtual_memory()
    print("="*40, "Memory Info", "="*40)
    print(f"Total Memory: {memory.total / (1024 ** 2):.2f} MB")
    print(f"Available Memory: {memory.available / (1024 ** 2):.2f} MB")
    print(f"Used Memory: {memory.used / (1024 ** 2):.2f} MB")
    print(f"Memory Usage Percentage: {memory.percent}%")

def get_storage_info():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print("="*40, f"Storage Info for {partition.device}", "="*40)
            print(f"Total Size: {usage.total / (1024 ** 3):.2f} GB")
            print(f"Used Space: {usage.used / (1024 ** 3):.2f} GB")
            print(f"Free Space: {usage.free / (1024 ** 3):.2f} GB")
            print(f"Usage Percentage: {usage.percent}%")
        except PermissionError:
            # This can happen if the partition is not ready
            continue

if __name__ == "__main__":
    get_system_info()
    get_boot_time()
    get_cpu_info()
    get_memory_info()
    get_storage_info()
