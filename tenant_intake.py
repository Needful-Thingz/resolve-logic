def run_tenant_intake():
    print("=== Welcome to the Resolve Maintenance Assistant ===")
    print("Please answer a few quick questions so we can diagnose the issue.\n")
    
    # Gathering baseline data
    tenant_name = input("Enter your full name: ")
    street_address = input("Enter your street address: ")
    unit_number = input("Enter your apartment/unit number (or type N/A): ")
    
    # Gathering the triage variables for the Resolve engine
    print("\n--- System Status ---")
    system_mode = input("Is your thermostat set to Cool, Heat, or Off?: ").strip().capitalize()
    
    try:
        current_temp = int(input("What is the current temperature inside the unit?: "))
        target_temp = int(input("What is your thermostat set to?: "))
    except ValueError:
        print("Please enter a valid number for the temperature.")
        current_temp = 75
        target_temp = 72

    # Packing everything into a dictionary to hand off to your main logic
    intake_data = {
        "tenant_name": tenant_name,
        "street_address": street_address,
        "unit_number": unit_number,
        "system_mode": system_mode,
        "current_indoor_temp": current_temp,
        "thermostat_target": target_temp
    }
    
    print("\n=== Intake Complete ===")
    return intake_data

# Testing the intake capture
if __name__ == "__main__":
    data_snapshot = run_tenant_intake()
    print("\nData captured for the Resolve Engine:")
    print(data_snapshot)