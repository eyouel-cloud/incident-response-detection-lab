# Threat Detection & Incident Response Simulation Lab

This project simulates a real-world intrusion scenario inside a controlled virtual lab using VMware, Windows Server 2022, Windows 11, Kali Linux, Sysmon, and Splunk/Wazuh.

## Objective
Build a complete SOC-style environment to learn log analysis, threat detection, incident response, and MITRE ATT&CK mapping.

## Tools & Technologies
- VMware Workstation / ESXi
- Windows Server 2022 (Domain Controller)
- Windows 11 Endpoint
- Kali Linux (Attacker)
- Splunk or Wazuh SIEM
- Sysmon
- PowerShell
- MITRE ATT&CK Framework

## Key Scenarios Simulated
### 1. Phishing → Credential Harvesting  
### 2. Malware Execution (Reverse Shell)  
### 3. Lateral Movement (Pass-the-Hash, WMI)  
### 4. Privilege Escalation (Mimikatz)

## Deliverables
- Full IR Report
- Detection Rules (Splunk, Sysmon)
- Timeline Analysis
- SOC Dashboards
- Architecture Diagrams

## MITRE Techniques Used
- T1059 PowerShell
- T1078 Valid Accounts
- T1021 Remote Services
- T1055 Process Injection
- T1086 Command Execution
- T1110 Brute Force

## Author
Eyouel Melaku
