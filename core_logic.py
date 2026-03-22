# SERENA OMNI-ENGINE - VERSION 1.0.0
# Initialized: 2026

def analyze_request(service_type, history, goal):
    print(f"--- SERENA TECHNICAL ANALYSIS: {service_type.upper()} ---")
    
    # Logic based on survey findings (Safety First)
    if "box dye" in history.lower() or "damaged" in history.lower():
        sid_r = 2
        status = "CONTRAINDICATION DETECTED"
    else:
        sid_r = 9
        status = "OPTIMAL"
        
    return f"SID-R: {sid_r} | STATUS: {status}"

# Test the engine
print(analyze_request("Hair", "6 months of box dye", "Platinum blonde"))
