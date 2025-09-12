# AWS Managed AD / AD-Trust

## Ressourcen

- [Bewertungskriterien](../../../08_Kompetenznachweise/LB2/Kompetenzmatrix-LB2.md)
- [01_A_Planung_AD & Cloud Setup Sheet](../01_Planung/resources/01_A_Planung_AD_&_Cloud_Setup_Sheet.md)

![Modul_159_Architekturdiagramm](../01_Planung/resources/Modul_159_Architekturdiagramm.drawio.svg)



## AWS Managed AD Domain

> [!IMPORTANT]
>
> Tragen Sie das von Ihnen hier festgelegte Passwort unbedingt bei Ihrer Planung ein.

| Schritte  | Printscreens                  |
| --------- | ----------------------------- |
| Schritt 1 | ![Step1](resources/Step1.png) |
| Schritt 2 | ![Step2](resources/Step2.png) |
| Schritt 3 | ![Step3](resources/Step3.png) |
| Schritt 4 | ![Step4](resources/Step4.png) |
| Schritt 5 | ![Step5](resources/Step5.png) |

## Ports aus der Planung nochmal sicherstellen

Sofern die Ports wie geplant eingerichtet wurden, kann mit der Einrichtung des Trusts begonnen werden.

## Conditional Forwarders

Damit Ihr Active Directory in EC die AWS-Managed-Domain sehen kann, muss ein sogenannter Conditional Forwarder eingerichtet werden. Normalerweise gehen AD-Abfragen immer an den eigenen DNS-Server des Active Directory. Da wir bei dieser Abfrage jedoch einen DNS-Server ausserhalb von `ec2.meinedomain.corp` abfragen müssen, benötigen wir diese bedingte Weiterleitung.



![Step5](resources/ConditionalForwarder.png)

![Step5](resources/DNS-Server.png)

> [!TIP]
>
> Testen Sie den Conditional Forwader mit nslookup zb mit `nslookup -type=SOA aws.meinedomain.corp`
>

## Trust einrichten

### EC2 AD

Gehen Sie auf Active Directory Domain and Trusts -> Eigenschaften auf Ihre Domain

| Schritte  | Printscreen                               |
| --------- | ----------------------------------------- |
| Schritt 1 | ![Trust-Step1](resources/Trust-Step1.png) |
| Schritt 2 | ![Trust-Step1](resources/Trust-Step2.png) |
| Schritt 3 | ![Trust-Step1](resources/Trust-Step3.png) |
| Schritt 4 | ![Trust-Step1](resources/Trust-Step4.png) |
| Schritt 5 | ![Trust-Step1](resources/Trust-Step5.png) |
| Schritt 6 | ![Trust-Step1](resources/Trust-Step6.png) |
| Schritt 7 | ![Trust-Step1](resources/Trust-Step7.png) |

### AWS managed AD

| Schritte  | Printscreens                                  |
| --------- | --------------------------------------------- |
| Schritt 1 | ![Trust-Step1](resources/AWS-Trust-Step1.png) |
| Schritt 2 | ![Trust-Step1](resources/AWS-Trust-Step2.png) |
| Schritt 3 | ![add-aws-trust](resources/add-aws-trust.png) |
| Schritt 4 | ![Trust-Step1](resources/AWS-Trust-Step3.png) |



### Trust validieren

Nachdem beide Seiten eingerichtet sind kann die Validierung auf dem EC2 Active Directory gemacht werden

 ![Trust-Step1](resources/validate.png)
