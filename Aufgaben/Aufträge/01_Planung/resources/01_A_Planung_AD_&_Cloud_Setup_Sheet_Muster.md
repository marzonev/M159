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

| Feld                                | Wert        |
| ----------------------------------- | ----------- |
| Vorname                             | Jonas       |
| Nachname                            | Aeschlimann |
| Klasse                              | Teacher     |
| Dokumentation (GIT-Repository-Link) | kein        |

---

## 3. Ressourcen

| Feld                                                         | Wert                   |
| ------------------------------------------------------------ | ---------------------- |
| Active Directory Second-Level-Domäne                         | meine-domain.local     |
| Geplante öffentliche Domain (UPN) -> Registrieren Sie einen Namen unter https://dynv6.com/ | m159tbz.v6.rocks       |
| Azure Education Account mit 80$ ([Anleitung für Freischaltung mit neuer nicht TBZ-E-Mail](../../..//02_Unterrichtsressourcen/03_Fachliteratur&Tutorials/Azure/QRC_AzureForStudents.pdf))<br />(Wenn Sie Ihre private E-Mail-Adresse nicht verwenden möchten, können Sie beispielsweise eine Gmail-Adresse erstellen.) | modul159SJ25@gmail.com |
| Azure Education Account Passwort                             | sdf3432lk4nsdfäö$3244  |

---

## 4. AWS VPC Setup

**Hinweis:**  
Alle Instanzen liegen in einem öffentlichen Subnetz und sind über RDP (Port 3389) von außen erreichbar.  
Alle weiteren Ports sind nur innerhalb des VPCs offen.  

| Komponente                    | VPC-ID                | CIDR          | Name                            | Öffentlich/Privat |
| ----------------------------- | --------------------- | ------------- | ------------------------------- | ----------------- |
| VPC                           | vpc-0470f613e45697700 | 10.0.0.0/16   |                                 |                   |
| Subnetz EC2 (DC/Client/Admin) |                       | 10.0.0.0/20   | M159-subnet-public1-us-east-1a  | Öffentlich        |
| Subnetz AWS AD                |                       | 10.0.128.0/20 | M159-subnet-private1-us-east-1a | Privat            |
|                               |                       | 10.0.144.0/20 | M159-subnet-private2-us-east-1b | Privat            |
|                               |                       |               |                                 |                   |

---

## 5. AWS Sicherheitsgruppen

### Sicherheitsgruppe für Domain Controller

| Regeltyp | Port(e)          | Quelle                                           |
| -------- | ---------------- | ------------------------------------------------ |
| RDP      | 3389             | 10.0.0.0/20 <br>10.0.128.0/20<br>10.0.144.0/20   |
| LDAP     | 389 (TCP/UDP)    | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| LDAPS    | 636              | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| Kerberos | 88 (TCP/UDP)     | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| SMB      | 445              | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| DNS      | 53 (TCP/UDP)     | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| RPC      | 135, 49152-65535 | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| ICMP     | Alle             | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |

### Sicherheitsgruppe für Clients

| Regeltyp | Port(e)     | Beschreibung                             | Quelle                                           |
| -------- | ----------- | ---------------------------------------- | ------------------------------------------------ |
| RDP      | 3389        | Remote Desktop                           | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| TCP      | 88          | Kerberos Authentication                  | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| TCP      | 135         | RPC Endpoint Mapper                      | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| TCP      | 139         | NetBIOS Session Service                  | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| TCP      | 389         | LDAP                                     | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| UDP      | 53          | DNS                                      | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| TCP      | 445         | SMB/CIFS (Dateifreigabe, AD-Operationen) | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| TCP      | 49152-65535 | RPC Ephemeral Ports                      | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |
| ICMP     | Alle        | Ping etc.                                | 10.0.0.0/20 <br/>10.0.128.0/20<br/>10.0.144.0/20 |

---

## 6. Active Directory Umgebung

### On-Premises Active Directory (AWS EC2)

| Feld                                  | Wert                   |
| ------------------------------------- | ---------------------- |
| Active Directory Third-Level-Domäne-1 | ec2.meine-domain.local |
| Öffentlicher UPN-Suffix (später)      | m159tbz.v6.rocks       |
| Domänenadministrator                  | Administrator          |
| Kennwort Domänenadministrator         | sdfdsf9889sdfdsfà£é    |

### Azure AD (Entra ID)

| Feld                         | Wert |
| ---------------------------- | ---- |
| Entra AD Tenant Name         |      |
| Azure Administrator (UPN)    |      |
| Kennwort Azure Administrator |      |
| Entra Connect Server (Name)  |      |

### AWS Managed AD

| Feld                                  | Wert                   |
| ------------------------------------- | ---------------------- |
| Active Directory Third-Level-Domäne-2 | aws.meine-domain.local |
| Trust-Typ                             | Tree-Root Trust        |
| AWS Managed Admin User                | admin                  |
| AWS Managed Admin Passwort            |                        |
| IP-Adresse                            |                        |
| DNS-Server 1                          |                        |
| DNS-Server 2                          |                        |
| Trust Passwort                        |                        |

---

## 7. EC2-Instanzen

| Komponente                                       | FQDN | Elastic IP | Private IP (CIDR) | Subnetz | Öffentlich/Privat | Gateway | DNS-Server 1 | DNS-Server 2 | Lokaler Admin | Kennwort |
| ------------------------------------------------ | ---- | ---------- | ----------------- | ------- | ----------------- | ------- | ------------ | ------------ | ------------- | -------- |
| IaaS/OnPrem AD DC                                |      |            |                   |         | Öffentlich        |         |              |              |               |          |
| Windows Server (Client)                          |      |            |                   |         | Öffentlich        |         |              |              |               |          |
| Managed AWS EC2 DC                               |      |            |                   |         |                   |         |              |              |               |          |
| Windows Server Admin Center (Managed AWS EC2 DC) |      |            |                   |         | Öffentlich        |         |              |              |               |          |

---

## 8. Abteilungen & Benutzer

Definieren Sie je einen Benutzer dieser 3 Abteilungen 

| Abteilung | Name der Abteilung | Benutzername | Vorname | Nachname | Kennwort | Bereiche |
| --------- | ------------------ | ------------ | ------- | -------- | -------- | -------- |
| 1         | Sekretariat        |              |         |          |          | intern   |
| 2         | Buchhaltung        |              |         |          |          | intern   |
| 3         | GL                 |              |         |          |          | intern   |
| 4         | Promoter           |              |         |          |          | extern   |

## 09. Python-App-Registration (Entra-ID)

| Name                    | Wert |
| ----------------------- | ---- |
| Directory (tenant) ID   |      |
| Application (client) ID |      |
| Client Secret ID        |      |



## 10. Hinweise

- Beginnen Sie mit der lokalen Domain-Umgebung und konfigurieren Sie **später den UPN-Suffix** mit der öffentlichen Domain.  
- Achten Sie auf **richtige Portfreigaben** in den AWS Sicherheitsgruppen, insbesondere für RDP, SMB und AD-Dienste.  
- Dokumentieren Sie alle IP-Adressen, Benutzernamen und Kennwörter konsequent in dieser Vorlage.
- Diese Vorlage wurde für das Schuljahr 2025/26 komplett neu erstellt. Falls Ihnen etwas fehlt, ist die Lehrperson dankbar, wenn Sie ihr dies mitteilen.