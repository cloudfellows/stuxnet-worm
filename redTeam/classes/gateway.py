import wmi

# Checking default gateway
def get_defaultGateay():
    gateways =""
    wmi_obj = wmi.WMI()
    wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
    wmi_out = wmi_obj.query( wmi_sql )
    for dev in wmi_out:
        gateways = dev.DefaultIPGateway[0]
    return gateways