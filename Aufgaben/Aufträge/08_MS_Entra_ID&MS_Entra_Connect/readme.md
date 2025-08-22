# MS Entra ID & MS Entra Connect

## Ressourcen

- [Bewertungskriterien](../../../08_Kompetenznachweise/LB2/Kompetenzmatrix-LB2.md)
- `Start-ADSyncSyncCycle -PolicyType Initial` / `Start-ADSyncSyncCycle -PolicyType Delta`<br>Zwei Befehle für den Entra ID Sync (Initial oder Delta)
- `dsregcmd /status` (Befehl zur Überprüfung der hybriden Mitgliedschaft)

## Azure for Students

Um eine Azure-Umgebung mit 80 $ Guthaben und einem eigenen Tenant zu erhalten, müssen Sie zunächst diese Anleitung befolgen.

[Anleitung für Freischaltung mit neuer nicht TBZ-E-Mail](../../..//02_Unterrichtsressourcen/03_Fachliteratur&Tutorials/Azure/QRC_AzureForStudents.pdf) (Wenn Sie Ihre private E-Mail-Adresse nicht verwenden möchten, können Sie beispielsweise eine Gmail-Adresse erstellen.)



## Entra ID Connect einrichten

| Schritte                                                     | Printscreens                                              |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| Schritt 1                                                    | ![AzureADConnect](resources/AzureADConnect.png)           |
| Schritt 2 (Installation )                                    | ![Setup](resources/Setup.png)                             |
| Schritt 3 (Dass der Suffix nicht machted ist grundsätzlich kein Problem, es wäre aber möglich dies bereits jetzt mit dem öffentlichen Suffix einzurichten, damit dies später nicht mehr gemacht werden muss) | ![suffix-not-matching](resources/suffix-not-matching.png) |
| Schritt 4                                                    | - Password Hash Synchronization (YES)                     |
| Schritt 5                                                    | ![complete](resources/complete.png)                       |
| Schritt 6                                                    | ![service](resources/service.png)                         |
| Schritt 7 (Wenn Sie diese Ansicht sehen, wissen Sie dass die Synchronsiserung funktioniert) | ![status](resources/status.png)                           |

## Custom-UPN (Domain) zu EntraID hinzufügen

| Schritte  | Printscreens                  |
| --------- | ----------------------------- |
| Schritt 1 | ![Step1](resources/Step1.png) |
| Schritt 2 | ![Step2](resources/Step2.png) |
| Schritt 3 | ![Step3](resources/Step3.png) |
| Schritt 4 | ![Step4](resources/Step4.png) |
| Schritt 5 |                               |

## Custom-UPN (Domain) zum EC2 Active Directory hinzufügen





## MS Entra AD (Hybrid-Join)

| Schritte   | Printscreens                                        |      |
| ---------- | --------------------------------------------------- | ---- |
| Schritt 1  | ![Step1-hybrid](resources/Step1-hybrid.png)         |      |
| Schritt 2  | ![Step2-hybrid](resources/Step2-hybrid.png)         |      |
| Schritt  3 | ![Step3-hybrid](resources/Step3-hybrid.png)         |      |
| Schritt 4  | ![Step4-hybrid-GPO](resources/Step4-hybrid-GPO.png) |      |
| Schritt 5  | ![Test](resources/Test.png)                         |      |

