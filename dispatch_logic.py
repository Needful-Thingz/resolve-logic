def generate_dispatch_report(intake_data):
    print("\n" + "="*45)
    print(" 🚨 URGENT: RESOLVE HVAC DISPATCH TICKET 🚨 ")
    print("="*45)
    
    report = f"""
PRIORITY MAINTENANCE REQUEST
----------------------------
Tenant Name:    {intake_data.get('tenant_name', 'Unknown')}
Address:        {intake_data.get('street_address', 'Unknown')}
Unit/Property:  {intake_data.get('unit_number', 'Unknown')}

SYSTEM STATUS SNAPSHOT:
- Thermostat Mode: {intake_data.get('system_mode', 'Unknown')}
- Current Temp:    {intake_data.get('current_indoor_temp', 'N/A')}°F
- Target Temp:     {intake_data.get('thermostat_target', 'N/A')}°F

ACTION REQUIRED: 
Please review the master logic triage tree before truck roll.
"""
    print(report)
    print("="*45)
    print(">> Automated dispatch sent to on-call technician.\n")

# Testing the report layout with some dummy data
if __name__ == "__main__":
    # We create a fake "snapshot" just to see what the tech will receive
    test_snapshot = {
        "tenant_name": "Mike Grueber",
        "street_address": "123 Main Street",
        "unit_number": "Apt 4B",
        "system_mode": "Cool",
        "current_indoor_temp": 85,
        "thermostat_target": 70
    }
    
    # Run the generator
    generate_dispatch_report(test_snapshot)