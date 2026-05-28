# resolve_logic.py - Core HVAC Triage Module - Needful Thingz LLC

class ResolveEngine:
    def __init__(self, property_id):
        self.property_id = property_id

    # BRANCH 1: The Dead Thermostat / No Power
    def triage_no_power(self, user_input):
        if user_input == "blank_screen":
            return "Action: Check batteries and replace if necessary."
        elif user_input == "breaker_flipped":
            return "Action: Reset HVAC breaker in main electrical panel."
        elif user_input == "switch_off":
            return "Action: Turn indoor service switch to ON."
        else:
            return "Dispatch Authorized: Professional HVAC Tech."

    # BRANCH 2: System Running But Blowing Warm Air
    def triage_warm_air(self, user_input):
        if user_input == "settings_wrong":
            return "Action: Set thermostat to COOL and Fan to AUTO."
        elif user_input == "filter_clogged_replaced":
            return "Action: Issue Resolved. Wait 2 hours to see if cooling resumes."
        elif user_input == "filter_clogged_no_spare":
            self.trigger_maintenance_alert("Filter Drop-off Required")
            return "Action: System OFF. Maintenance will deliver filter to avoid damage."
        elif user_input == "outdoor_dirty_condenser":
            self.trigger_maintenance_alert("Dirty Condenser Coil (Wash with hose)")
            return "Action: Maintenance alerted. Dispatch cancelled."
        elif user_input == "outdoor_fan_off_or_ice":
            return "Dispatch Authorized: Turn thermostat OFF immediately to prevent damage."
        else:
            return "Dispatch Authorized: Professional HVAC Tech."

    # BRANCH 3: Water Leaking Around Indoor Unit
    def triage_water_leak(self, user_input):
        if user_input == "pan_full_of_water":
            self.trigger_maintenance_alert("Likely Clogged Primary Drain Line")
            return "Action: System OFF. Maintenance dispatched with wet/dry vac."
        elif user_input == "frozen_coil":
            return "Dispatch Authorized: Turn thermostat OFF, but switch Fan ON to thaw ice."
        elif user_input == "plumbing_leak":
            return "Reroute to Plumbing Triage Flow. Do not dispatch HVAC."
        else:
            return "Dispatch Authorized: Professional HVAC Tech."

    # THE VALUE ADD: Internal Maintenance Alerts
    def trigger_maintenance_alert(self, issue_type):
        # This flags the PM for an internal fix to save them a contractor dispatch fee
        print(f"--> [ALERT TO PM] Maintenance Opportunity at {self.property_id}: {issue_type}")
        return True

# Test Environment
if __name__ == "__main__":
    engine = ResolveEngine("Test_Property_001")
    
    print("--- Running Resolve System Diagnostics ---")
    print("Test 1 (Branch 2):", engine.triage_warm_air("outdoor_dirty_condenser"))
    print("Test 2 (Branch 3):", engine.triage_water_leak("pan_full_of_water"))