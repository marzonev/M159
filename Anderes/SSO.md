# Aufgabenblatt: **SSO in verschiedenen Situationen**

## Aufgabe 1 – Netzlaufwerk (klassisches AD)

Ein Benutzer klickt auf ein Netzlaufwerk, um Dateien anzuzeigen. Beschreiben Sie in **5 Schritten**, was im Hintergrund passiert. Ergänzen Sie die fehlenden Begriffe.

1. Der Benutzer meldet sich mit seinem **Passwort** an Windows an.
2. Windows holt beim **Domain Controller** ein **Ticket-Granting-Ticket (TGT)**.
3. Beim Zugriff auf den Fileserver fragt Windows beim Domain Controller ein **Service-Ticket** für diesen Server an.
4. Windows übergibt das Ticket an den **Fileserver**.
5. Der Server prüft das Ticket und erlaubt den Zugriff auf die **Dateien**.

*(Begriffe zur Auswahl: Passwort, Kerberos, Service, Domain Controller, Dateien, Ticket Granting, Fileserver)*

------

## Aufgabe 2 – Word Online über Windows-Session (Azure AD / Entra ID)

Ein Benutzer öffnet **word.office.com** auf einem PC, der in Azure AD eingebunden ist und mit der Windows-Session arbeitet. Ergänzen Sie die fehlenden Begriffe.

1. Der Benutzer meldet sich an Windows an und erhält ein **Primary Refresh Token (PRT)**.
2. Im Browser ruft er **word.office.com** auf.
3. Der Browser sendet im Hintergrund eine Anfrage an den **Identity Provider (Entra ID)**.
4. Entra ID prüft den PRT und stellt ein **Access Token** für Word Online aus.
5. Der Benutzer ist ohne zusätzliche Eingabe von Benutzername und Passwort in **Word** eingeloggt.

*(Begriffe zur Auswahl: Refresh, Word, Entra, Access, word)*

------

## Aufgabe 3 – Word Online nach Login auf anderer Webseite (Cookie-SSO)

Ein Benutzer hat sich vorher bei **outlook.office.com** angemeldet und möchte jetzt **word.office.com** öffnen. Ergänzen Sie die fehlenden Begriffe.

1. Beim ersten Login bei Outlook gibt der Benutzer Benutzername, Passwort und ggf. **MFA** ein.
2. Der Identity Provider (Entra ID) gibt dem Browser ein **Session-Cookie**.
3. Der Benutzer ruft **word.office.com** auf, und der Browser schickt automatisch den gespeicherten **Cookie** mit.
4. Entra ID erkennt den Benutzer und stellt direkt ein neues **Access Token** für **Word** aus.
5. Der Benutzer ist nun ohne erneute Eingabe auch in Word Online **angemeldet**.

*(Begriffe zur Auswahl: Cookie, MFA, Word, angemeldet, Session-Cookie)*