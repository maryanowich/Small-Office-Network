# Small-Office-Network
Cisco router and switch configuration for a small office network with 5 departments.

#Network Design Overview
Office Departments:

Administration
Sales
IT
Finance
HR
VLAN Assignments:
Each department is assigned a VLAN and subnet for efficient management and traffic segmentation.

IP Address Allocation:
Each subnet provides 30 usable IPs (supporting the 20 hosts + future expansion).

#Topology:
The network includes:

A core switch is configured for VLANs.
A router (or Layer 3 switch) for inter-VLAN routing.
Access switches connected to end devices.

#Physical Layout
Router/Layer 3 Switch:
Handles inter-VLAN routing and connects to the WAN.

Core Switch:
Configured with VLANs and 802.1Q trunking. Ports are tagged/untagged based on VLAN assignment.

Access Switches:
Connect end-user devices and are assigned to specific VLANs.
