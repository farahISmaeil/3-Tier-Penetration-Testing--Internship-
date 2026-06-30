# 3-Tier-Penetration-Testing--Internship-
Secure 3-Tier Web Architecture Penetration Testing Lab - Ethical hacking project demonstrating vulnerability discovery, exploitation, and remediation
# 3-Tier Penetration Testing Lab

A comprehensive cybersecurity project demonstrating vulnerability discovery, exploitation, and remediation of a 3-tier web architecture.

## Project Overview

This project simulates a real-world penetration testing engagement where Kali Linux (attacker) targets an Ubuntu Server (victim) running a LAMP stack with intentionally vulnerable web applications.

## Architecture

- **Attacker**: Kali Linux 2026.1 (192.168.56.101)
- **Target**: Ubuntu Server 26.04 LTS (192.168.56.102)
- **Network**: Host-Only (192.168.56.0/24)
- **Services**: Apache 2.4.66, MySQL 8.4.8, PHP 8.5, SSH

## Phase 2: Reconnaissance Scripts

1. **port_scanner.py** - Custom Python port scanner (found ports 22, 80 open)
2. **web_fingerprint.py** - Web server identification (Apache 2.4.66)
3. **ip_mapper.py** - Network service mapping (MySQL properly isolated)

## Phase 3: Exploitation Scripts

4. **brute_force.py** - Password cracking (found admin/password123)
5. **keylogger.py** - Keystroke logging simulation
6. **server.py** - Reverse shell server (attacker side)
7. **client.py** - Reverse shell client (target side)
8. **ransomware.py** - File encryption simulation
9. **decrypt_ransomware.py** - Decryption utility

## Vulnerabilities Discovered

- SQL Injection in login.php
- Weak password policies
- No input validation
- Exposed database user privileges

## Security Fixes Implemented

- Parameterized SQL queries (prevent SQL injection)
- Database hardening (GRANT/REVOKE - principle of least privilege)
- Malware cleanup (removed test files)
- Terminal history cleaning

## Deliverables

- **Penetration_Testing_Hardening_Report.pdf** - Complete technical report
- **Architecture_Topology_Diagram.pdf** - Network diagram
- **All Python scripts** - Well-documented and tested

## How to Use

Each script is standalone:

```bash
python3 port_scanner.py
python3 web_fingerprint.py
python3 brute_force.py
python3 keylogger.py
python3 server.py
python3 client.py
python3 ransomware.py
python3 decrypt_ransomware.py
```

## Project Status

✅ Phase 1: Infrastructure - Complete
✅ Phase 2: Reconnaissance - Complete
✅ Phase 3: Exploitation - Complete
✅ Phase 4: Remediation - Complete

## Author

Farah Ismaeil

## Disclaimer

This project is for educational purposes only. All testing was performed in a controlled, isolated lab environment.
