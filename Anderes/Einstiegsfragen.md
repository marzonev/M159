# Directory Services – Fragen & Antworten

## Aus technischer Sicht ist ein Verzeichnisdienst nichts anderes als
Eine **spezialisierte Datenbank**, die Objekte hierarchisch speichert und für Abfragen optimiert ist.

---

## 4 Kernaufgaben eines Directory Services
1. Benutzeranmeldung
2. Autorisierung (Zugriffsrechte)
3. Geräteverwaltung
4. Verzeichnisabfragen & Suche

---

## 5 Objekte in einem Directory
- Benutzer
- Gruppen
- Computer
- Drucker
- Freigaben

---

## 5 Merkmale eines Directory Services
1. Hierarchische Struktur
2. Replikation
3. Zentrale Verwaltung
4. Skalierbarkeit
5. Standardisierte Protokolle (LDAP, Kerberos)

---

## Zusammenhang Objekt – Attribut – Wert

**Korrekt:**
- Benutzerattribute haben einen Namen und einen Wert
- Passwortattribut mit Name/Wert ist ein Benutzerattribut
- Vorname ist ein Benutzerattribut

**Falsch:**
- Benutzerattribute sind Eigenschaften von Computern
- Druckerobjekte haben keine Attribute

---

## Was ist eine Objektklasse?
Ein **Bauplan für Objekte**, der vorgibt, welche Attribute Pflicht oder optional sind.

---

## Zwei Nachteile eines Directory Services
1. Single Point of Failure ohne Redundanz
2. Hohe Komplexität in Betrieb & Pflege

---

## IT-Situation MIT Directory Service
Firma mit 200 Mitarbeitern / zentrale Anmeldung(user), Richtlinien, Ressourcenverwaltung.

## IT-Situation OHNE Directory Service
Kleiner Betrieb mit 5 PCs. keine zentrale Verwaltung nötig.

---

## Lokaler Administrator
Vollzugriff nur auf einem einzelnen Gerät.

## Domänenadministrator
Vollzugriff in der gesamten Domäne.

---

## Aufgaben des Domänenkontrollers
- Benutzer authentifizieren
- Richtlinien anwenden
- Änderungen speichern & replizieren

---

## Abkürzungen
- **DC** = Domain Controller
- **OU/OE** = Organizational Unit / Organisationseinheit

---

## On-Premises
Lokaler Betrieb im eigenen Rechenzentrum (nicht Cloud).

---

## Unterschied AD DS vs. Entra ID
- **MS AD DS**: klassisch On-Premises, LDAP/Kerberos.
- **Entra ID (Azure AD)**: Cloud-basiert, OAuth/OpenID.

---

## Intune, MDM & MAM
- **Intune**: Geräte- & App-Management von Microsoft
- **MDM**: Mobile Device Management (Geräte)
- **MAM**: Mobile Application Management (Apps)

---

## Tenant
Eine eigene M365-Umgebung

---

## AD-Umgebung mit Entra ID Integration
Hybrid Identity / Hybrid-Umgebung