# AD-Aufgaben (LB)

<hr>

| #    | Aufgabe                                                      | Beschreibung                                                 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [Planung](Aufträge/01_Planung)                               | Erstellen einer detaillierten Projektplanung inklusive Definition aller relevanten Parameter. |
| 2    | [Initial Setup](Aufträge/02_Initial_Setup)                   | Grundinstallation und Konfiguration der AWS-Umgebung gemäss Planung, inklusive IP-Adressen, Hostnames, Ports und Standardeinstellungen. |
| 3    | [Gesamtstruktur (erster DC) & Client](Aufträge/03_Neue_Gesamtstruktur_und_Client) | Einrichtung des ersten Domain Controllers, Join des Clients zur Domäne und Umsetzung aller definierten Zusatzanforderungen. |
| 4    | [Freigaben Laufwerke Berechtigungen](Aufträge/04_Freigaben_Laufwerke_Berechtigungen) | Anlegen der benötigten Gruppen und Benutzer, Zuweisung und Test der NTFS- und Freigabeberechtigungen sowie Umsetzung von ABE und Group-Nesting-Konzept. |
| 5    | [AWS Managed Microsoft](Aufträge/05_AWS%20Managed_Microsoft_AD/) | Einrichtung von AWS Managed Microsoft AD, Konfiguration der Ports und Aufbau eines funktionierenden Trusts mit Sicherheitsdokumentation. |
| 6    | [RSAT & Admin Center V2](Aufträge/06_RSAT_&_Admin_Center_V2) | Installation der RSAT-Tools, Einrichtung des Windows Admin Centers für interne und externe Administration unter Berücksichtigung von Sicherheitsmassnahmen. |
| 7    | [DIT & GPO's](Aufträge/07_DIT&GPO's)                         | Erstellung einer korrekten Domänenstruktur (DIT) und Umsetzung der definierten GPO-Aufgaben gemäss Anforderungen. |
| 8    | [MS Entra ID & MS Entra Connect](Aufträge/08_MS_Entra_ID&MS_Entra_Connect) | Verbinden Sie Ihre Active-Directory-Umgebung mit Azure Entra Connect und synchronisieren Sie Objekte zwischen Active Directory und Entra ID. Führen Sie anschließend den Hybrid Join durch, damit die Clients sowohl in AD als auch in Entra ID als Geräte sichtbar sind. |
| 9    | [Servergespeicherte Benutzerprofile](Aufträge/09_Servergespeicherte_Benutzerprofile) | Einrichtung von Roaming Profiles, Folder Redirection oder FS-Logix sowie Migration von Profilordnern nach OneDrive Business. |
| 10   | [Netzlaufwerk to Azure Migration](Aufträge/10_Netzlaufwerk_to_Azure_Migration) | Einrichtung eines Azure Storage Accounts mit File Share und Anbindung über Key oder Entra ID/AD-Integration ohne zusätzliche Authentifizierung. |
| 11   | [SSO Python App](Aufträge/11_SSO_Python_App)                 | Einrichtung und Test einer Python-Webanwendung mit Single Sign-On (SSO) Integration über Entra ID und verschiedenen Authentifizierungsverfahren. |
