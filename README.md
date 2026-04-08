# 🛡️ DMZ-Based Secure E-Commerce Architecture

## 📌 Overview

This project demonstrates the design and implementation of a **secure multi-tier DMZ (Demilitarized Zone) architecture** for an e-commerce system.

It follows a **zero-trust, layered security approach**, ensuring that each component communicates only with explicitly allowed layers.

---

## 🧠 Architecture Summary

The system is divided into three zones:

* **Public Zone** → Internet-facing (WAF)
* **DMZ Zone** → Web layer
* **Internal Zone** → Application + Database + Monitoring

---

## 🏗️ Final Architecture

```
Internet
   ↓
WAF (VM1)
   ↓
Web Server (VM2)
   ↓
Application Server (VM3)
   ↓
Database Server (VM4)
```

---

## 🔄 Request Flow

```
User → WAF → Web → App → Database → Response
```

---

## 💻 System Setup

### Host Machine

* OS: Ubuntu 24.04 LTS
* RAM: 16 GB
* CPU: Intel i7 (12th Gen)
* Virtualization: KVM (QEMU + libvirt)

---

## 🖥️ Virtual Machines

| VM  | Role                | Network        |
| --- | ------------------- | -------------- |
| VM1 | WAF / Reverse Proxy | NAT + DMZ      |
| VM2 | Web Server          | DMZ            |
| VM3 | Application Server  | DMZ + Internal |
| VM4 | Database Server     | Internal       |
| VM5 | Monitoring Server   | Internal       |

---

## 🌐 Network Configuration

### DMZ Network

```
Subnet: 192.168.1.0/24
```

### Internal Network

```
Subnet: 192.168.2.0/24
```

---

## 📍 IP Addressing Plan

### DMZ Layer

* WAF → 192.168.1.1
* Web → 192.168.1.2
* App → 192.168.1.10

### Internal Layer

* App → 192.168.2.10
* DB → 192.168.2.2
* Monitoring → 192.168.2.3

---

## ⚙️ Technologies Used

* **Nginx** → Reverse proxy + Web server
* **Flask (Python)** → Application backend
* **MySQL** → Database
* **UFW** → Firewall management
* **KVM / Virt-Manager** → Virtualization

---

## 🔧 Implementation Steps

### 1. Virtualization Setup

* Installed KVM, libvirt, virt-manager
* Verified using `virsh list`

---

### 2. Network Segmentation

* Created:

  * `dmz-net` → 192.168.1.0/24
  * `internal-net` → 192.168.2.0/24

---

### 3. VM Network Mapping

* WAF → NAT + DMZ
* Web → DMZ
* App → DMZ + Internal
* DB → Internal
* Monitoring → Internal

---

### 4. Static IP Configuration

* Configured using **Netplan**
* Ensured inter-VM connectivity via ping tests

---

### 5. WAF Setup

* Installed Nginx on VM1
* Configured reverse proxy → Web server

```nginx
proxy_pass http://192.168.1.2;
```

---

### 6. Web Server Setup

* Installed Nginx on VM2
* Forwarded requests → Application server

```nginx
proxy_pass http://192.168.1.10:5000;
```

---

### 7. Application Server Setup

* Built Flask app with API endpoints

```python
@app.route('/')
def home():
    return "Hello from Application Server 🚀"
```

---

### 8. Database Setup

* Installed MySQL on VM4

* Created:

  * Database: `ecommerce`
  * User: `appuser`

* Enabled remote access:

```ini
bind-address = 192.168.2.2
```

---

### 9. App ↔ DB Integration

* Used `mysql-connector-python`
* Verified DB connectivity through Flask app

---

### 10. Firewall Configuration (Critical)

#### Allowed Flows

| Source   | Destination | Port |
| -------- | ----------- | ---- |
| Internet | WAF         | 80   |
| WAF      | Web         | 80   |
| Web      | App         | 5000 |
| App      | DB          | 3306 |

#### Blocked

* All other traffic (default deny)

---

## 🔐 Security Features

* Network segmentation (DMZ + Internal)
* Reverse proxy (WAF layer)
* Restricted inter-layer communication
* Database isolation
* Principle of least privilege
* No direct access to backend systems

---

## 🧪 Testing & Validation

### Successful Tests

* Full request flow working
* App connected to DB
* Reverse proxy functioning

### Security Tests

* Web → DB ❌ blocked
* Unauthorized access ❌ blocked
* Only allowed flows permitted ✅

---

## ⚠️ Challenges Faced

* 502 Bad Gateway (fixed by starting app server)
* Firewall over-restriction (fixed by refining UFW rules)
* Network interface misconfiguration

---

## 🚀 Future Enhancements

* Add **Honeypot in DMZ**
* Integrate **ELK Stack (Monitoring)**
* Implement **HTTPS (TLS encryption)**
* Containerize using Docker
* Add **Intrusion Detection System (IDS)**

---

## 🎯 Key Learnings

* Importance of network segmentation
* Real-world firewall configuration challenges
* Layered security architecture
* Debugging distributed systems

---

## 🏁 Conclusion

This project successfully demonstrates a **secure, scalable, and production-style DMZ architecture** for an e-commerce platform, implementing strong access control and layered defense mechanisms.

---

## 👨‍💻 Author

Shivansh Soni
