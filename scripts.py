; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Instalador de Programas Jurídicos"
#define MyAppVersion "1.0"
#define MyAppPublisher "OAB CE"
#define MyAppURL """

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{BC50F00E-1063-4AE0-A171-306794E039F9}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
InfoBeforeFile="C:\Users\arthu\OneDrive\Área de Trabalho\antes.txt"
InfoAfterFile="C:\Users\arthu\OneDrive\Área de Trabalho\poi.txt"
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\arthu\OneDrive\Área de Trabalho
OutputBaseFilename=Instalador de Programas Jurídicos
SetupIconFile="C:\Users\arthu\OneDrive\Área de Trabalho\tela.ico"
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Files]
Source: "C:\Users\arthu\Downloads\jre-8u401-windows-i586.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arthu\Downloads\Firefox Setup 122.0.1.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arthu\Downloads\(64)GDsetupStarsignCUTx64.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arthu\Downloads\(64)SafeSignIC30124-x64-win-tu-admin(1).exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arthu\Downloads\PJEOffice 1.0.28.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arthu\Downloads\shodo 1.1.2.msi"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arthu\Downloads\WebSignerSetup_2.11.1_pt-BR.msi"; DestDir: "{app}"; Flags: ignoreversion


[Run]
Filename: "{app}\jre-8u401-windows-i586.exe"; Parameters: "/s"; WorkingDir: "{app}"; Flags: skipifsilent
Filename: "{app}\Firefox Setup 122.0.1.exe"; Parameters: "-ms"; WorkingDir: "{app}"; Flags: skipifsilent
Filename: "{app}\(64)GDsetupStarsignCUTx64.exe"; Parameters: "/quiet"; WorkingDir: "{app}"; Flags: skipifsilent
Filename: "{app}\(64)SafeSignIC30124-x64-win-tu-admin(1).exe"; Parameters: "/S"; WorkingDir: "{app}"; Flags: skipifsilent
Filename: "{app}\PJEOffice 1.0.28.exe"; Parameters: "/VERYSILENT"; WorkingDir: "{app}"; Flags: skipifsilent
Filename: "{app}\shodo 1.1.2.msi"; Parameters: "/quiet"; WorkingDir: "{app}"; Flags: skipifsilent runhidden
Filename: "{app}\WebSignerSetup_2.11.1_pt-BR.msi"; Parameters: "/quiet"; WorkingDir: "{app}"; Flags: skipifsilent runhidden





