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

| Feld                                                         | Wert |
| ------------------------------------------------------------ | ---- |
| Active Directory Second-Level-Domäne                         |      |
| Geplante öffentliche Domain (UPN) -> Registrieren Sie einen Namen unter https://dynv6.com/ |      |
| Azure Education Account mit 80$ ([Anleitung für Freischaltung mit neuer nicht TBZ-E-Mail](../../../../02_Unterrichtsressourcen/03_Fachliteratur&Tutorials/Azure/QRC_AzureForStudents.pdf))<br />(Wenn Sie Ihre private E-Mail-Adresse nicht verwenden möchten, können Sie beispielsweise eine Gmail-Adresse erstellen.) |      |
| Azure Education Account Passwort                             |      |

---

## 4. AWS VPC Setup

**Hinweis:**  
Alle Instanzen liegen in einem öffentlichen Subnetz und sind über RDP (Port 3389) von außen erreichbar.  
Alle weiteren Ports sind nur innerhalb des VPCs offen.  

| Komponente                    | VPC-ID | CIDR         | Name | Öffentlich/Privat |
| ----------------------------- | ------ | ------------ | ---- | ----------------- |
| VPC                           |        | 10.30.0.0/16 |      |                   |
| Subnetz EC2 (DC/Client/Admin) |        | 10.30.0.0/16 |      | Öffentlich        |
| Subnetz AWS AD                |        |              |      | Privat            |
|                               |        |              |      | Privat            |
|                               |        |              |      |                   |

## 5. AWS Sicherheitsgruppen

### Sicherheitsgruppe für Domain Controller

| Regeltyp | Port(e)          | Quelle    |
| -------- | ---------------- | --------- |
| RDP      | 3389             | 0.0.0.0/0 |
| LDAP     | 389 (TCP/UDP)    |           |
| LDAPS    | 636              |           |
| Kerberos | 88 (TCP/UDP)     |           |
| SMB      | 445              |           |
| DNS      | 53 (TCP/UDP)     |           |
| RPC      | 135, 49152-65535 |           |
| ICMP     | Alle             |           |

### Sicherheitsgruppe für Clients

| Regeltyp | Port(e)     | Beschreibung                             | Quelle |
| -------- | ----------- | ---------------------------------------- | ------ |
| RDP      | 3389        | Remote Desktop                           |        |
| TCP      | 88          | Kerberos Authentication                  |        |
| TCP      | 135         | RPC Endpoint Mapper                      |        |
| TCP      | 139         | NetBIOS Session Service                  |        |
| TCP      | 389         | LDAP                                     |        |
| UDP      | 53          | DNS                                      |        |
| TCP      | 445         | SMB/CIFS (Dateifreigabe, AD-Operationen) |        |
| TCP      | 49152-65535 | RPC Ephemeral Ports                      |        |
| ICMP     | Alle        | Ping etc.                                |        |

---

## 6. Active Directory Umgebung

### On-Premises Active Directory (AWS EC2)

| Feld                                  | Wert                             |
| ------------------------------------- | -------------------------------- |
| Active Directory Third-Level-Domäne-1 |                                  |
| Öffentlicher UPN-Suffix (später)      |                                  |
| Domänenadministrator                  | Administrator                    |
| Kennwort Domänenadministrator         | lt8v2TbtuO5i5=d=0Oihy1=xM3t?LxAT |

### Azure AD (Entra ID)

| Feld                         | Wert |
| ---------------------------- | ---- |
| Entra AD Tenant Name         |      |
| Azure Administrator (UPN)    |      |
| Kennwort Azure Administrator |      |
| Entra Connect Server (Name)  |      |

### AWS Managed AD

| Feld                                  | Wert            |
| ------------------------------------- | --------------- |
| Active Directory Third-Level-Domäne-2 |                 |
| Trust-Typ                             | Tree-Root Trust |
| AWS Managed Admin User                | admin           |
| AWS Managed Admin Passwort            |                 |
| IP-Adresse                            |                 |
| DNS-Server 1                          |                 |
| DNS-Server 2                          |                 |
| Trust Passwort                        |                 |
|                                       |                 |
|                                       |                 |

---

## 7. EC2-Instanzen

| Komponente                                       | FQDN                 | Elastic IP   | Private IP (CIDR) | Subnetz      | Öffentlich/Privat | Gateway   | DNS-Server 1 | DNS-Server 2 | Lokaler Admin | Kennwort                         |
| ------------------------------------------------ | -------------------- | ------------ | ----------------- | ------------ | ----------------- | --------- | ------------ | ------------ | ------------- | -------------------------------- |
| IaaS/OnPrem AD DC                                | dcm159.ec2.platanera | 107.22.113.8 | 10.30.0.10/20     | 10.30.0.0/20 | Öffentlich        | 10.30.0.1 | 127.0.0.1    |              | Administrator | lt8v2TbtuO5i5=d=0Oihy1=xM3t?LxAT |
| Windows Server (Client)                          | clm159.ec2.platanera | 3.93.132.83  | 10.30.0.20/20     | 10.30.0.0.22 | Öffentlich        | 10.30.0.1 | 10.30.0.10   |              | Adinistrator  | 4ZmBQ2rP0EqAZ0wP77j3F$x)uR!1RAjJ |
| Managed AWS EC2 DC                               |                      |              |                   |              |                   |           |              |              |               |                                  |
| Windows Server Admin Center (Managed AWS EC2 DC) |                      |              |                   |              | Öffentlich        |           |              |              |               |                                  |

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