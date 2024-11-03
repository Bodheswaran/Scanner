import subprocess
import sys
import psutil

def install(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def check_and_install_psutil():
    """Check if psutil is installed, and install it if not."""
    try:
        import psutil
        print("psutil is already installed.")
    except ImportError:
        print("psutil not found. Installing...")
        install('psutil')

def get_active_connections():
    """Retrieve active network connections."""
    connections = psutil.net_connections(kind='inet')
    return connections

def assess_risk_level(status):
    """Assess risk level based on connection status."""
    if status == 'ESTABLISHED':
        return "High Risk"  # Established connections can be exploited
    elif status in ['LISTEN', 'CLOSE_WAIT']:
        return "Medium Risk"  # Listening ports can be exploited if not secured
    else:
        return "Low Risk"  # Other statuses may indicate less risk

def check_vulnerabilities(connections):
    """Check for potential vulnerabilities based on active connections."""
    vulnerabilities = []

    for conn in connections:
        local_address = conn.laddr
        remote_address = conn.raddr if conn.raddr else "N/A"
        status = conn.status
        pid = conn.pid
        
        # Check if the port is open and the connection is established
        if status in ['ESTABLISHED', 'LISTEN', 'CLOSE_WAIT']:
            risk_level = assess_risk_level(status)
            vulnerabilities.append({
                'local_address': f"\n{local_address.ip}:{local_address.port}",
                'remote_address': remote_address,
                'status': status,
                'pid': pid,
                'risk_level': risk_level
            })

    return vulnerabilities

def display_vulnerabilities(vulnerabilities):
    """Display found vulnerabilities with risk levels."""
    if not vulnerabilities:
        print("No active vulnerabilities found.")
        return

    print("Active Vulnerabilities Found:")
    for vuln in vulnerabilities:
        print(f"Local Address: {vuln['local_address']} | "
              f"Remote Address: {vuln['remote_address']} | "
              f"Status: {vuln['status']} | "
              f"PID: {vuln['pid']} | "
              f"Risk Level: {vuln['risk_level']}\n")

def main():
    check_and_install_psutil()  # Check and install psutil if necessary

    print("Retrieving active network connections...")
    active_connections = get_active_connections()
    
    print(f"Total Active Connections: {len(active_connections)}")
    
    vulnerabilities = check_vulnerabilities(active_connections)
    
    display_vulnerabilities(vulnerabilities)

if __name__ == "__main__":
    main()
