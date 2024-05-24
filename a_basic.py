protocols = ["HTTP", "HTTPS", "FTP", "DNS"]
ports = [80, 443, 21, 53]
# Create dictionary by zipping the two lists together
network_dict = dict(zip(protocols, ports))
print(network_dict)