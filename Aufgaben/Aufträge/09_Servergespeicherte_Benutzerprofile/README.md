# 12 Servergespeicherte Profile

## Ressourcen

- [Bewertungskriterien](../../../08_Kompetenznachweise/LB2/Kompetenzmatrix-LB2.md)

## FS-Logix

https://www.kreyman.de/index.php/microsoft/ms-sonstiges/163-fslogix-profile-container-schritt-fuer-schritt-anleitung

## OneDrive (OneDrive Known Folder Move (KFM) als Ersatz für lokale Benutzerprofile)

Aktuell nutzen alle Benutzer **lokale Profile**.  
Die Daten (Desktop, Dokumente, Bilder) liegen nur auf dem jeweiligen PC.  
Diese sollen zukünftig automatisch in **OneDrive for Business** synchronisiert werden, um sie auf allen Geräten verfügbar zu machen.

Die Umgebung besteht aus:
- **Windows Server mit Active Directory Domain Services**
- **Windows Clients** in der Domäne
- **Azure for Students Tenant** mit aktivem OneDrive for Business
- Synchronisation von On-Prem AD-Benutzern zu Entra ID via **Azure AD Connect**

---

## Voraussetzungen
- Mindestens **2 Testbenutzer** (in AD und Entra ID)
- OneDrive for Business im Tenant aktiviert
- OneDrive-Client auf den Clients installiert (Standard bei Win10/11)
- Internetzugang für die Clients

---

## Auftrag

### Teil 1 – Vorbereitungen
1. Melden Sie sich als Testbenutzer **an einem Domänen-Client an**, der noch **kein OneDrive** konfiguriert hat.
2. Erstellen Sie **im lokalen Profil** (nicht in OneDrive!) eine Datei:
   - Speicherort: `Desktop`
   - Dateiname: `Testmigration.txt`
   - Inhalt: frei wählbar
3. Abmelden.

---

### Teil 2 – OneDrive Konfiguration via Gruppenrichtlinie
1. Öffnen Sie die Gruppenrichtlinienverwaltung.
2. Erstellen Sie ein neues GPO, verknüpft mit der OU, in der sich Ihre Testbenutzer befinden.
3. Konfigurieren Sie folgende Einstellungen (unter **Benutzerkonfiguration → Administrative Vorlagen → OneDrive**):

   - **Silently configure OneDrive using the primary Windows account**  
     → OneDrive-Tenant-URL eintragen (`https://<TenantName>-my.sharepoint.com`)

   - **Silently move Windows known folders to OneDrive**  
     → Aktivieren

   - **Prevent users from redirecting their Windows known folders back to their PC**  
     → Aktivieren

   - Optional: **Prompt users to move Windows known folders to OneDrive** deaktivieren (für vollautomatische Migration)

---

### Teil 3 – Migrationstest
1. Melden Sie sich wieder mit dem Testbenutzer am Client an.
2. Prüfen Sie:
   - Wird OneDrive automatisch gestartet und angemeldet?
   - Wird der Desktop-Inhalt (inkl. `Testmigration.txt`) in OneDrive verschoben?
3. Öffnen Sie den OneDrive-Ordner im Windows Explorer und kontrollieren Sie, ob die Datei synchronisiert wurde.

---

### Teil 4 – Gerätewechsel-Test
1. Melden Sie sich mit demselben Benutzer an einem anderen PC in der Domäne an.
2. Prüfen Sie, ob die Datei `Testmigration.txt` automatisch im Desktop-Ordner verfügbar ist.
3. Erstellen Sie auf PC2 eine neue Datei `VonPC2.txt` auf dem Desktop und prüfen Sie auf PC1, ob diese nach kurzer Zeit erscheint.

