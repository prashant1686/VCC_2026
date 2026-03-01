# Assignment2
# GCP Auto-Scaling & Security Implementation

## Overview

This project is a small hands-on implementation of auto scaling and basic security setup on Google Cloud Platform (GCP). 

The main idea was to understand how instances can automatically scale when CPU usage increases, and at the same time make sure the setup follows proper security practices like restricted firewall rules and limited IAM access.

Nothing overly complex — just a clean working cloud setup that actually scales when load increases.

---

## Architecture Highlights

- **Instance Template:** Debian 12 (Bookworm), E2-Micro machine type  
- **Managed Instance Group (MIG):** Used to manage and replicate instances  
- **Auto-Scaling:** Configured to scale out when CPU usage goes above 60%  

### Security Setup

- **Firewall Rule:**  
  Only allows HTTP (Port 80) traffic and only for instances with the `http-server` tag.  
  This prevents unnecessary exposure.

- **IAM:**  
  Followed Principle of Least Privilege.  
  Used "Compute Viewer" role instead of giving broad permissions.

---

## How It Was Done

1. **Infrastructure Setup**  
   Resources were created manually using the GCP Console (Instance Template + Managed Instance Group).

2. **Startup Configuration**  
   A `startup-script.sh` file installs required packages automatically when a new VM starts.  
   So whenever scaling happens, the new instance is ready without manual work.

3. **Testing Auto-Scaling**  
   Used `stress-test.sh` to increase CPU load.  
   Once CPU crossed 60%, new instances were created automatically by the Managed Instance Group.

---

## What This Shows

- How CPU-based scaling works in real time  
- How Managed Instance Groups simplify scaling  
- Basic but important firewall configuration  
- IAM role restriction in practice  

Overall, this project helped in understanding how scaling and security go together in a cloud environment.
