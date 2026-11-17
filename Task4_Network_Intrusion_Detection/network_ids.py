# TASK 4: NETWORK INTRUSION DETECTION SYSTEM

from collections import Counter

# Sample simulated network events
events = [
    {"ip": "192.0.2.10", "event": "failed_login", "port": 22},
    {"ip": "192.0.2.10", "event": "failed_login", "port": 22},
    {"ip": "192.0.2.10", "event": "failed_login", "port": 22},
    {"ip": "192.0.2.20", "event": "successful_login", "port": 443},
    {"ip": "192.0.2.30", "event": "connection_attempt", "port": 23},
]

print("NETWORK INTRUSION DETECTION SYSTEM")
print("----------------------------------")

# Count failed login attempts
failed_logins = Counter(
    event["ip"]
    for event in events
    if event["event"] == "failed_login"
)

# Detect repeated failed logins
for ip, count in failed_logins.items():
    if count >= 3:
        print("ALERT: Repeated failed login attempts!")
        print("Source IP:", ip)
        print("Attempts:", count)
        print("----------------------------------")

# Detect unusual port activity in sample logs
for event in events:
    if event["port"] == 23:
        print("WARNING: Unusual port activity detected!")
        print("Source IP:", event["ip"])
        print("Port:", event["port"])
        print("----------------------------------")

print("Detection completed.")