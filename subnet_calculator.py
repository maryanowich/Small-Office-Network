import ipaddress

def calculate_subnets(network, new_prefix):
    """
    Calculates subnets from a given network and prefix length.
    
    Args:
        network (str): The network address in CIDR notation (e.g., 200.152.14.0/24).
        new_prefix (int): The desired subnet prefix length (e.g., 27).
    Returns:
        list: A list of dictionaries containing subnet details.
    """
    try:
        net = ipaddress.IPv4Network(network, strict=False)
        subnets = list(net.subnets(new_prefix=new_prefix))
        results = []
        
        for subnet in subnets:
            results.append({
                "network_id": str(subnet.network_address),
                "broadcast": str(subnet.broadcast_address),
                "first_host": str(list(subnet.hosts())[0]),
                "last_host": str(list(subnet.hosts())[-1]),
                "default_gateway": str(list(subnet.hosts())[0]),
                "subnet_mask": str(subnet.netmask),
            })
        return results
    
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    print("IP Subnet Calculator")
    base_network = input("Enter base network (e.g., 200.152.14.0/24): ")
    new_cidr = int(input("Enter new CIDR (e.g., 27): "))
    
    subnets = calculate_subnets(base_network, new_cidr)
    
    if subnets:
        print("\nCalculated Subnets:")
        for idx, subnet in enumerate(subnets, start=1):
            print(f"\nSubnet {idx}:")
            print(f"  Network ID: {subnet['network_id']}")
            print(f"  Broadcast: {subnet['broadcast']}")
            print(f"  First Host: {subnet['first_host']}")
            print(f"  Last Host: {subnet['last_host']}")
            print(f"  Default Gateway: {subnet['default_gateway']}")
            print(f"  Subnet Mask: {subnet['subnet_mask']}")
    else:
        print("No subnets were calculated.")


