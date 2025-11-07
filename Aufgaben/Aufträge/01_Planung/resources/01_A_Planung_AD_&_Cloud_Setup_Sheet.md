# M159 - Projekt-Setup-Sheet

In diesem Dokument werden sämtliche Angaben sowie Passwörter, welche Sie für die Installation Ihrer Umgebung benötigen, festgehalten.

![Modul_159_Architekturdiagramm](Modul_159_Architekturdiagramm.drawio.svg)



---

## 1. Übersicht Umgebung

Diese Umgebung umfasst:

- **1x Windows Server (DC)** auf AWS EC2  
- **1x Windows Server (Client)** auf AWS EC2 (da AWS keine Windows Clients anbietet)  
- **1x Windows Server (Admin Center)** auf AWS EC2 zur Verwaltung der AWS Managed AD  
- **AWS Managed AD** mit Trust zur On-Premises(EC2) AD  
- **Entra Connect** zur Synchronisation mit Entra ID sowie Entra AD  
- **Lokale AD-Domain** (zu Beginn), später **öffentliche Domain als UPN**  

---

## 2. Allgemeine Angaben

| Feld                                | Wert                             |
| ----------------------------------- | -------------------------------- |
| Vorname                             | Nevio                            |
| Nachname                            | Marzo                            |
| Klasse                              | PE23e                            |
| Dokumentation (GIT-Repository-Link) | https://github.com/marzonev/M159 |

---

## 3. Ressourcen

| Feld                                 | Wert                              |
| ------------------------------------ | --------------------------------- |
| Active Directory Second-Level-Domäne | ec2.platanera                     |
| Geplante öffentliche Domain          | platanera.dynv6.net               |
| Azure Education Account mit 80$      | Administrator@platanera.dynv6.net |
| Azure Education Account Passwort     | Nevio1234                         |

---

## 4. AWS VPC Setup

**Hinweis:**  
Alle Instanzen liegen in einem öffentlichen Subnetz und sind über RDP (Port 3389) von außen erreichbar.  
Alle weiteren Ports sind nur innerhalb des VPCs offen.  

| Komponente                    | VPC-ID                | CIDR          | Name                           | Öffentlich/Privat |
| ----------------------------- | --------------------- | ------------- | ------------------------------ | ----------------- |
| VPC                           | vpc-001964a21a602be6c | 10.30.0.0/16  | M159-vpc                       | Öffentlich        |
| Subnetz EC2 (DC/Client/Admin) | vpc-001964a21a602be6c | 10.30.0.0/20  | M159-subnet-public1-us-east-1a | Öffentlich        |
| Subnetz AWS AD                | vpc-001964a21a602be6c | 10.30.16.0/20 | M159-subnet-public2-us-east-1b | Öffentlich        |

## 5. AWS Sicherheitsgruppen

### Sicherheitsgruppe für Domain Controller

| Regeltyp | Port(e)          | Quelle       |
| -------- | ---------------- | ------------ |
| RDP      | 3389             | 0.0.0.0      |
| LDAP     | 389 (TCP/UDP)    | 10.30.0.0/20 |
| LDAPS    | 636              | 10.30.0.0/20 |
| Kerberos | 88 (TCP/UDP)     | 10.30.0.0/20 |
| SMB      | 445              | 10.30.0.0/20 |
| DNS      | 53 (TCP/UDP)     | 10.30.0.0/20 |
| RPC      | 135, 49152-65535 | 10.30.0.0/20 |
| ICMP     | Alle             | 10.30.0.0/20 |

### Sicherheitsgruppe für Clients

| Regeltyp | Port(e)     | Beschreibung                             | Quelle       |
| -------- | ----------- | ---------------------------------------- | ------------ |
| RDP      | 3389        | Remote Desktop                           | 0.0.0.0      |
| TCP      | 88          | Kerberos Authentication                  | 10.30.0.0/20 |
| TCP      | 135         | RPC Endpoint Mapper                      | 10.30.0.0/20 |
| TCP      | 139         | NetBIOS Session Service                  | 10.30.0.0/20 |
| TCP      | 389         | LDAP                                     | 10.30.0.0/20 |
| UDP      | 53          | DNS                                      | 10.30.0.0/20 |
| TCP      | 445         | SMB/CIFS (Dateifreigabe, AD-Operationen) | 10.30.0.0/20 |
| TCP      | 49152-65535 | RPC Ephemeral Ports                      | 10.30.0.0/20 |
| ICMP     | Alle        | Ping etc.                                | 10.30.0.0/20 |

---

## 6. Active Directory Umgebung

### On-Premises Active Directory (AWS EC2)

| Feld                                  | Wert                             |
| ------------------------------------- | -------------------------------- |
| Active Directory Third-Level-Domäne-1 | dcm159.ec2.platanera             |
| Öffentlicher UPN-Suffix (später)      | platanera.dynv6.net              |
| Domänenadministrator                  | Administrator                    |
| Kennwort Domänenadministrator         | lt8v2TbtuO5i5=d=0Oihy1=xM3t?LxAT |

### Azure AD (Entra ID)

| Feld                         | Wert                              |
| ---------------------------- | --------------------------------- |
| Entra AD Tenant Name         | Standardverzeichnis               |
| Azure Administrator (UPN)    | Administrator@platanera.dynv6.net |
| Kennwort Azure Administrator | Nevio1234                         |
| Entra Connect Server (Name)  | dcm159.ec2.platanera              |

### AWS Managed AD

| Feld                                  | Wert            |
| ------------------------------------- | --------------- |
| Active Directory Third-Level-Domäne-2 | aws.platanera   |
| Trust-Typ                             | Tree-Root Trust |
| AWS Managed Admin User                | admin           |
| AWS Managed Admin Passwort            | Nevio1234       |
| IP-Adresse                            | 10.30.16.10     |
| DNS-Server 1                          | 10.30.0.10      |
| DNS-Server 2                          | 9.9.9.9         |
| Trust Passwort                        | Nevio1234       |

---

## 7. EC2-Instanzen

| Komponente                                       | FQDN                  | Elastic IP   | Private IP (CIDR) | Subnetz       | Öffentlich/Privat | Gateway    | DNS-Server 1 | DNS-Server 2 | Lokaler Admin | Kennwort                         |
| ------------------------------------------------ | --------------------- | ------------ | ----------------- | ------------- | ----------------- | ---------- | ------------ | ------------ | ------------- | -------------------------------- |
| IaaS/OnPrem AD DC                                | dcm159.ec2.platanera  | 107.22.113.8 | 10.30.0.10/20     | 10.30.0.0/20  | Öffentlich        | 10.30.0.1  | 127.0.0.1    |              | Administrator | lt8v2TbtuO5i5=d=0Oihy1=xM3t?LxAT |
| Windows Server (Client)                          | clm159.ec2.platanera  | 3.93.132.83  | 10.30.0.20/20     | 10.30.0.0/20  | Öffentlich        | 10.30.0.1  | 10.30.0.10   |              | Adinistrator  | 4ZmBQ2rP0EqAZ0wP77j3F$x)uR!1RAjJ |
| Managed AWS EC2 DC                               | aws.platanera         |              | 10.30.0.170       | 10.30.16.0/20 | Öffentlich        | 10.30.16.1 | 10.30.0.10   |              | Admin         | Nevio1234                        |
| Windows Server Admin Center (Managed AWS EC2 DC) | dasm159.aws.platanera | 3.213.209.15 | 10.30.16.20       | 10.30.16.0/20 | Öffentlich        | 10.30.16.1 | 10.30.0.10   |              | Administrator | !@*DwM9ceEGwz-aW?((lDTjgS?&sB(IO |

---

## 8. Abteilungen & Benutzer

Definieren Sie je einen Benutzer dieser 3 Abteilungen 

| Abteilung | Name der Abteilung | Benutzername | Vorname | Nachname | Kennwort  | Bereiche |
| --------- | ------------------ | ------------ | ------- | -------- | --------- | -------- |
| 1         | Sekretariat        | frarog       | Roger   | Franklin | Nevio1234 | intern   |
| 2         | Buchhaltung        | fraros       | Rosche  | Franco   | Nevio1234 | intern   |
| 3         | GL                 | sybgur       | Gurt    | Sybau    | Nevio1234 | intern   |
| 4         | Promoter           | friate       | Ate     | Fries    | Nevio1234 | extern   |

## 09. Python-App-Registration (Entra-ID)

| Name                    | Wert                                     |
| ----------------------- | ---------------------------------------- |
| Directory (tenant) ID   | a5e03f37-fb3d-4d2a-b4b4-a14b5139b035     |
| Application (client) ID | a5e03f37-fb3d-4d2a-b4b4-a14b5139b035     |
| Client Secret ID        | fZt8Q~NOKFDWsPuiTD64un231Pe3x9rKltlGNaa7 |



## 10. Hinweise

- Beginnen Sie mit der lokalen Domain-Umgebung und konfigurieren Sie **später den UPN-Suffix** mit der öffentlichen Domain.  
- Achten Sie auf **richtige Portfreigaben** in den AWS Sicherheitsgruppen, insbesondere für RDP, SMB und AD-Dienste.  
- Dokumentieren Sie alle IP-Adressen, Benutzernamen und Kennwörter konsequent in dieser Vorlage.
- Diese Vorlage wurde für das Schuljahr 2025/26 komplett neu erstellt. Falls Ihnen etwas fehlt, ist die Lehrperson dankbar, wenn Sie ihr dies mitteilen.