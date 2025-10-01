; PDF to Excel Converter Windows Installer
; NSIS Script for creating Windows installer

!define APPNAME "PDF to Excel Converter"
!define COMPANYNAME "PracticePro"
!define DESCRIPTION "Convert PDF quiz files to Excel format with multi-language support"
!define VERSIONMAJOR 1
!define VERSIONMINOR 0
!define VERSIONBUILD 0
!define HELPURL "https://github.com/yourusername/pdf-xlsx-tool"
!define UPDATEURL "https://github.com/yourusername/pdf-xlsx-tool"
!define ABOUTURL "https://github.com/yourusername/pdf-xlsx-tool"
!define INSTALLSIZE 50000

RequestExecutionLevel admin
InstallDir "$PROGRAMFILES\${APPNAME}"
Name "${APPNAME}"
outFile "PDF_to_Excel_Converter_Setup.exe"

!include LogicLib.nsh

page directory
page instfiles

!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin"
    messageBox mb_iconstop "Administrator rights required!"
    setErrorLevel 740
    quit
${EndIf}
!macroend

function .onInit
    setShellVarContext all
    !insertmacro VerifyUserIsAdmin
functionEnd

section "install"
    setOutPath $INSTDIR
    
    ; Copy main executable
    file "dist\PDF_to_Excel_Converter.exe"
    
    ; Copy supporting files
    file /r "pdf_converter_tools"
    file /r "converted_examples"
    file "15100堆高機操作(程式檔)-中+印+越+英.xlsx"
    file "README.md"
    
    ; Create desktop shortcut
    createShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\PDF_to_Excel_Converter.exe"
    
    ; Create start menu shortcut
    createDirectory "$SMPROGRAMS\${APPNAME}"
    createShortCut "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\PDF_to_Excel_Converter.exe"
    createShortCut "$SMPROGRAMS\${APPNAME}\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    
    ; Write uninstaller
    writeUninstaller "$INSTDIR\uninstall.exe"
    
    ; Write registry keys for uninstaller
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayIcon" "$\"$INSTDIR\PDF_to_Excel_Converter.exe$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Publisher" "${COMPANYNAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "HelpLink" "${HELPURL}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLUpdateInfo" "${UPDATEURL}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLInfoAbout" "${ABOUTURL}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayVersion" "${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMajor" ${VERSIONMAJOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMinor" ${VERSIONMINOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoRepair" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "EstimatedSize" ${INSTALLSIZE}
sectionEnd

section "uninstall"
    delete "$INSTDIR\PDF_to_Excel_Converter.exe"
    delete "$INSTDIR\uninstall.exe"
    delete "$INSTDIR\README.md"
    delete "$INSTDIR\15100堆高機操作(程式檔)-中+印+越+英.xlsx"
    
    rmDir /r "$INSTDIR\pdf_converter_tools"
    rmDir /r "$INSTDIR\converted_examples"
    
    delete "$DESKTOP\${APPNAME}.lnk"
    delete "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk"
    delete "$SMPROGRAMS\${APPNAME}\Uninstall.lnk"
    rmDir "$SMPROGRAMS\${APPNAME}"
    
    rmDir "$INSTDIR"
    
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
sectionEnd
