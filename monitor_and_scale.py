import psutil
import time
import os

# --- CONFIGURATION ---
CPU_THRESHOLD = 75
PROJECT_ID = "m25ai2050"
ZONE = "us-central1-a"
TEMPLATE_NAME = "hybrid-lab-template"
NEW_CLOUD_VM = "burst-cloud-node-01"

print("Starting Hybrid Cloud Monitor (Local Node)...")
print(f"Target Threshold: {CPU_THRESHOLD}%")

def trigger_cloud_burst():
    print(" triggering Cloud Burst for the  GCP...")
    gcloud_cmd = f"gcloud compute instances create {NEW_CLOUD_VM} \
                   --source-instance-template={TEMPLATE_NAME} \
                   --zone={ZONE} \
                   --project={PROJECT_ID} \
                   --quiet"
    
    # Execute the command
    result = os.system(gcloud_cmd)
    
    if result == 0:
        print(f"✅ SUCCESS: {NEW_CLOUD_VM} provisioned on GCP.")
        print("🌐 Application is now scaling to the public cloud.")
    else:
        print("❌ ERROR: Failed to provision Cloud VM.")

# --- MONITORING LOOP ---
while True:
    # Check local CPU usage
    cpu_usage = psutil.cpu_percent(interval=2)
    print(f"Current Local CPU Usage: {cpu_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        print(f"⚠️ ALERT: CPU exceeded {CPU_THRESHOLD}%! Local resources exhausted.")
        trigger_cloud_burst()
        
        # Stop monitoring after bursting to prevent creating infinite VMs
        print("🛑 Monitoring suspended. Cloud Burst complete.")
        break