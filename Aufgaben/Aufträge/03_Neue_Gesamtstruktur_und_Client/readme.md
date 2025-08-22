# Gesamtstruktur (erster DC) & Client

Unter einer neuen Gesamtstruktur versteht man eine neue Domäne aufsetzen. Dies bedeutet ein Windows Server wird zu einem Domänen Controller gemacht.

## Ressourcen

- [Bewertungskriterien](../../../08_Kompetenznachweise/LB2/Kompetenzmatrix-LB2.md)
- [01_A_Planung_AD & Cloud Setup Sheet](../01_Planung/resources/01_A_Planung_AD_&_Cloud_Setup_Sheet.md)



### Video zur Aufgabe 3

Falls Sie nicht wissen, wie man einen DC promotet, finden Sie unter folgendem Link Videos zu diesem Thema.

[Einen ersten Domänencontroller installieren](https://gitlab.com/ch-tbz-it/Stud/m159/-/blob/main/02_Unterrichtsressourcen/03_Fachliteratur&Tutorials/Videos.md) (Die Videos sind zwar etwas in die Jahre gekommen, für On-Premises/Iaas-Setups aber immer noch relevant.)



## AD aufsetzen

### AD DS-Rolle auf dem DC1 hinzufügen

- Server Manager Rolle hinzufügen

### DC1 promoten

- Neue Gesamtstruktur
- Standardspeicherorte belassen

### DNS

- Richten Sie eine DNS-Weiterleitung an 9.9.9.9 (Erklären Sie der Lehrperson oder in der Dokumentation, warum 9.9.9.9 besser ist als 8.8.8.8.)

- Forward-Zone einrichten (Wird beim Promoten eines DC automatisch erstellt)
- Für Jedes Subnetz müssen Sie eine «Reverse-Zone» einrichten -> Das ist sehr wichtig bei AWS da man sonst einen falschen FQDN bei der Reverse Auflösung erhält
- Wenn Sie Ihren DC in der Forward-Zone finden, machen Sie eine Aktualisierung des PTR-Records, damit der Host auch in der Reverse-Zone zu finden ist.

- «NS LOOKUP» auf dem Server vorwärts und rückwärts testen

### Diverse AD-Einstellungen

- Aktivieren Sie den AD-Papierkorb



## Client in die Domäne einbinden

Damit sich Active-Directory-Benutzer anmelden können und der Computer im Active Directory verfügbar ist, muss der Client der Domäne hinzugefügt werden. Mit anderen Worten: Der Computer muss ein Objekt im Active Directory werden.

Voraussetzung dafür ist, dass der Domänencontroller und das DNS korrekt installiert sind. Windows 7/10/11 Home Premium und Basic können keiner Domäne hinzugefügt werden. Hierzu sind die Editionen Professional, Enterprise, Ultimate oder Education erforderlich.

**Vorbereitung**

Damit Sie den Client zur Domäne hinzufügen können, müssen TCP/IP und vor allem der DNS richtig konfiguriert sein.

Bei AWS muss zusätzlich dafür gesorgt werden, dass die benötigten Ports eingerichtet sind.

(Falls der Domain-Join extrem lange dauert und dann mit einer Erfolgsmeldung und anschließend einer Fehlermeldung abschließt, handelt es sich um Netzwerk- bzw. Portprobleme.)

#### Benötigte Ports

| Port        | Protokoll | Beschreibung                                                 |
| ----------- | --------- | ------------------------------------------------------------ |
| 88          | TCP       | Kerberos-Authentifizierung – Netzwerk-Authentifizierungsprotokoll |
| 135         | TCP       | RPC Endpoint Mapper – Lokalisiert andere RPC-Dienste         |
| 139         | TCP       | NetBIOS Session Service – Veraltet, aber teilweise noch im Einsatz |
| 389         | TCP       | LDAP – Zugriff auf das Active Directory-Verzeichnis          |
| 53          | UDP       | DNS – Namensauflösung, z. B. um Domain Controller zu finden  |
| 445         | TCP       | SMB/CIFS – Datei-/Druckfreigabe sowie gewisse AD-Funktionen  |
| 49152–65535 | TCP       | Dynamische RPC-Ports (Ephemeral) – Für RPC-Dienste nach Verbindungsaufbau über Port 135 |

> [!TIP]
>
> Testen Sie anschliessend mit  Test-NetConnection -ComputerName dc1.m159.tbz -Port XY ob die Ports offen sind.
>



## Client in die Domain einbinden

|                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Um den Client in die Domäne aufzunehmen unter Systemsteuerung\Alle Systemsteuerungselemente\System im Bereich Einstellungen für Computernamen, Domäne und Arbeitsgruppe den Punkt Einstellungen ändern aufrufen. | ![Client](..\..\images/04-Picture1.png)                      |
| Im Reiter Computername auf Ändern klicken.                   | ![Client](..\..\images/04-Picture2.png)                      |
| Den Name des Computers angeben. Dieser muss eindeutig sein und darf im Active Directory noch nicht vorhanden sein. Unter Domäne die URL der Domäne eintragen. Mit einem Klick auf OK, wird nach dem Domänencontroller gesucht. Wurde der Domänencontroller gefunden, erscheint ein Anmeldefenster. | <img src="..\..\images/04-Picture3.png" alt="Client" style="zoom:75%;" /> |
| Einen Domänenbenutzer angeben, der über die Rechte verfügt einen Computer der Domäne hinzuzufügen. Standardmäßig haben dieses Recht Domänen-Administratoren. | ![Client](..\..\images/04-Picture4.png)                      |
|                                                              | ![Client](..\..\images/04-Picture5.png)                      |
| Nach einem Neustart ist der Computer der Domäne hinzugefügt.Domänenbenutzer können sich jetzt am Computer anmelden. Der neu hinzugefügte Domänencomputer befindet sich standardmäßig in der Organisationseinheit Computer. | ![Client](..\..\images/04-Picture6.png)                      |

#### Updaten Sie auch den «PTR-Record» für Ihre Clients in der DNS Reverse-Zone

#### Wichtig: Merken Sie sich folgenden für das Anmelden in Zukunft

- .\Logonname -> Anmeldung lokal am Client

- Computername\Logonname -> Anmeldung lokal am Client

- Domain\Logonname -> Anmeldung an Domäne über NETBIOS-Name

- Logonname@Domain -> Anmeldung an Domäne über DNS-Name



## Remote Desktop Konzept

Erstellen Sie ein RDP-Konzept wie Sie Ihre User welche Remotedesktop verwenden dürfen berechtigen wollen. 

Konfigurieren Sie Ihre Umgebung entsprechend und dokumentieren Sie das Ganze.
