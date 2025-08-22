# Initial Setup

## Ressourcen

- [Bewertungskriterien](../../../08_Kompetenznachweise/LB2/Kompetenzmatrix-LB2.md)
- [01_A_Planung_AD & Cloud Setup Sheet](../01_Planung/resources/01_A_Planung_AD_&_Cloud_Setup_Sheet.md)



## AWS-EC2 gemäss Ihrer Planung aufsetzen

- VPC inkl. öffentlichen und privaten Subnetzen, kein Gateway (wenn später bei einem privaten Subnetz Internet benötigt wird, kann man immer noch einen NAT Gateway hinzufügen - aber Achtung diese gehen schnell ins Budget) & Security Groups erstellen (Sie können den VPC-Assistenten verwenden)
- Konfigurieren Sie die beiden Security Groups
- EC2 Instanzen erstellen (Achten Sie darauf, dass beim erstellen die richtigen IP-Adressen ausgewählt werden, da sonst AWS automatisch welche verwendet)
- Benennen Sie die EC2-Instanzen gleich wie die Hostnames



## Windows-Einstellungen vornehmen

#### Hostname setzen

- Setzen Sie die richtigen Computernamen (Hostnames)

#### Firewall (Core & Desktop)

- Ping erlauben

#### Tastaturlayout (Core & Desktop)

- CH

#### Verstärkte Sicherheitskonfiguration ausschalten für IE (Desktop)

- Im Server Manager Ausschalten

#### Netzwerkadapter (Core & Desktop)

- Deaktivieren Sie TCP/IP V6

#### Anzeige & Ordneroptionen (Desktop)

- Deaktivieren «Erweiterungen bei unbekannten Dateitypen ausblenden»

- Deaktivieren «Freigabeassistenten verwenden»

- Deaktivieren «Geschützte Systemdateien ausblenden» und aktivieren Sie "Alle Dateien anzeigen"

- Erstellen Sie eine Verknüpfung für CMD und PS auf dem Desktop

- Blenden Sie Desktopsymbole ein (Dieser PC, Systemsteuerung, Netzwerk)



