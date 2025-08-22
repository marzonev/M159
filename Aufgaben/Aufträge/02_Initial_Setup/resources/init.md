# Init

Hier ist ein PowerShell-Skript, das die Lehrperson für neue Windows-VMs benutzt.



```
# 1) Pfade und Hilfsfunktion fuer Verknuepfungen
$DefaultDesktop = Join-Path $env:SystemDrive 'Users\Default\Desktop'
$CurrentDesktop = [Environment]::GetFolderPath('Desktop')

foreach ($desk in @($DefaultDesktop, $CurrentDesktop)) {
    if (-not (Test-Path $desk)) {
        New-Item -Path $desk -ItemType Directory -Force | Out-Null
    }
}

function New-Shortcut {
    param(
        [Parameter(Mandatory)] [string] $Path,
        [Parameter(Mandatory)] [string] $Target,
        [string] $Arguments,
        [string] $IconLocation
    )
    $shell = New-Object -ComObject WScript.Shell
    $sc = $shell.CreateShortcut($Path)
    $sc.TargetPath = $Target
    if ($Arguments)    { $sc.Arguments    = $Arguments }
    $sc.WorkingDirectory = Split-Path $Target
    if ($IconLocation) { $sc.IconLocation = $IconLocation }
    $sc.Save()
}

function Add-DesktopShortcuts {
    param([Parameter(Mandatory)][string] $DesktopPath)

$controlExe = Join-Path $env:SystemRoot 'System32\control.exe'
$psExe      = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
$cmdExe     = Join-Path $env:SystemRoot 'System32\cmd.exe'

# PowerShell
New-Shortcut -Path (Join-Path $DesktopPath 'PowerShell.lnk') `
    -Target $psExe -IconLocation "$psExe,0"

# Eingabeaufforderung (cmd)
New-Shortcut -Path (Join-Path $DesktopPath 'Eingabeaufforderung.lnk') `
    -Target $cmdExe -IconLocation "$cmdExe,0"

# Netzwerkverbindungen (ncpa.cpl)
New-Shortcut -Path (Join-Path $DesktopPath 'Netzwerkverbindungen.lnk') `
    -Target $controlExe -Arguments 'ncpa.cpl' `
    -IconLocation "$env:SystemRoot\System32\ncpa.cpl,0"
    
# Remote Desktop (mstsc)
New-Shortcut -Path (Join-Path $DesktopPath 'Remote Desktop.lnk') `
    -Target "$env:SystemRoot\System32\mstsc.exe" `
    -IconLocation "$env:SystemRoot\System32\mstsc.exe,0"

# Systemeigenschaften (sysdm.cpl)
New-Shortcut -Path (Join-Path $DesktopPath 'Systemeigenschaften.lnk') `
    -Target $controlExe -Arguments 'sysdm.cpl' `
    -IconLocation "$env:SystemRoot\System32\sysdm.cpl,0"

# Systemsteuerung (Hauptuebersicht)
New-Shortcut -Path (Join-Path $DesktopPath 'Systemsteuerung.lnk') `
    -Target $controlExe -IconLocation "$controlExe,0"

# Firewall (Defender Firewall in der Systemsteuerung)
New-Shortcut -Path (Join-Path $DesktopPath 'Firewall.lnk') `
    -Target $controlExe -Arguments '/name Microsoft.WindowsFirewall' `
    -IconLocation "$env:SystemRoot\System32\FirewallControlPanel.dll,0"
# Fallback (klassische CPL):
# New-Shortcut -Path (Join-Path $DesktopPath 'Firewall.lnk') -Target $controlExe -Arguments 'firewall.cpl' -IconLocation "$env:SystemRoot\System32\firewall.cpl,0"

}

# Verknuepfungen fuer Default und aktuellen Benutzer
Add-DesktopShortcuts -DesktopPath $DefaultDesktop
Add-DesktopShortcuts -DesktopPath $CurrentDesktop

# 2) Firewall: Ping (ICMP Echo) fuer alle Profile aktivieren
$icmpRules = @('FPS-ICMP4-ERQ-In','FPS-ICMP6-ERQ-In')
try {
    Enable-NetFirewallRule -Name $icmpRules -ErrorAction Stop
} catch {
    Write-Warning "Konnte ICMP-Regeln nicht aktivieren: $($_.Exception.Message). Versuche generisches Matching..."
    try {
        Get-NetFirewallRule |
            Where-Object { $_.Direction -eq 'Inbound' -and ($_.DisplayName -match 'Echo' -or $_.DisplayName -match 'ICMP') } |
            Enable-NetFirewallRule
    } catch {
        Write-Warning "Generisches Aktivieren der ICMP-Regeln ist ebenfalls fehlgeschlagen: $($_.Exception.Message)"
    }
}

# 3) Explorer-Ansicht: versteckte + Systemdateien anzeigen, Dateiendungen anzeigen fuer Default (neue Benutzer) und aktuell (HKCU)
$advDefault = 'Registry::HKEY_USERS\.DEFAULT\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced'
$advHKCU    = 'Registry::HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced'

foreach ($path in @($advDefault,$advHKCU)) {
    New-Item -Path $path -Force | Out-Null
    New-ItemProperty -Path $path -Name 'Hidden'          -PropertyType DWord -Value 1 -Force | Out-Null
    New-ItemProperty -Path $path -Name 'ShowSuperHidden' -PropertyType DWord -Value 1 -Force | Out-Null
    New-ItemProperty -Path $path -Name 'HideFileExt'     -PropertyType DWord -Value 0 -Force | Out-Null
}

# 4) Tastaturlayout: Deutsch Schweiz (de-CH) fuer aktuellen Benutzer und neue Benutzer
try {
    $ll = New-WinUserLanguageList -Language de-CH
    Set-WinUserLanguageList -LanguageList $ll -Force
    Copy-UserInternationalSettingsToSystem -WelcomeScreen $true -NewUser $true
} catch {
    Write-Warning "Set-WinUserLanguageList/Copy-UserInternationalSettingsToSystem nicht verfuegbar: $($_.Exception.Message). Setze Registry-Fallback..."

$hkcuPreload = 'Registry::HKEY_CURRENT_USER\Keyboard Layout\Preload'
$defPreload  = 'Registry::HKEY_USERS\.DEFAULT\Keyboard Layout\Preload'
foreach ($p in @($hkcuPreload,$defPreload)) {
    New-Item -Path $p -Force | Out-Null
    New-ItemProperty -Path $p -Name '1' -Value '00000807' -PropertyType String -Force | Out-Null
    (Get-Item -Path $p).GetValueNames() |
        Where-Object { $_ -ne '1' } |
        ForEach-Object { Remove-ItemProperty -Path $p -Name $_ -ErrorAction SilentlyContinue }
}

}

Write-Host "Fertig: Verknuepfungen erstellt (Default + aktuell), Ping aktiviert, Explorer-Ansichten gesetzt, Tastaturlayout auf Deutsch Schweiz."
```