from DB import update_mods, new_task, select_mods
from Config import ModulesDirectory
import os


def check_module_loaded(module_name, randomuri, user, force=False):
    try:
        modules_loaded = select_mods(randomuri)
        if force:
            for modname in os.listdir(ModulesDirectory):
                if modname.lower() in module_name.lower():
                    module_name = modname
            new_task(("loadmodule %s" % module_name), user, randomuri)
        if modules_loaded:
            new_modules_loaded = "%s %s" % (modules_loaded, module_name)
            if module_name not in modules_loaded:
                for modname in os.listdir(ModulesDirectory):
                    if modname.lower() in module_name.lower():
                        module_name = modname
                new_task(("loadmodule %s" % module_name), user, randomuri)
                update_mods(new_modules_loaded, randomuri)
        else:
            new_modules_loaded = "%s" % (module_name)
            new_task(("loadmodule %s" % module_name), user, randomuri)
            update_mods(new_modules_loaded, randomuri)
    except Exception as e:
        print("Error loadmodule: %s" % e)


def run_autoloads(command, randomuri, user):
    if command.lower().strip().startswith("invoke-eternalblue"):
        check_module_loaded("Exploit-EternalBlue.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-psuacme"):
        check_module_loaded("Invoke-PsUACme.ps1", randomuri, user)
    elif command.lower().strip().startswith("bloodhound"):
        check_module_loaded("BloodHound.ps1", randomuri, user)
    elif command.lower().strip().startswith("brute-ad"):
        check_module_loaded("Brute-AD.ps1", randomuri, user)
    elif command.lower().strip().startswith("brute-locadmin"):
        check_module_loaded("Brute-LocAdmin.ps1", randomuri, user)
    elif command.lower().strip().startswith("bypass-uac"):
        check_module_loaded("Bypass-UAC.ps1", randomuri, user)
    elif command.lower().strip().startswith("cred-popper"):
        check_module_loaded("Cred-Popper.ps1", randomuri, user)
    elif command.lower().strip().startswith("cve-2016-9192"):
        check_module_loaded("CVE-2016-9192.ps1", randomuri, user)
    elif command.lower().strip().startswith("convertto-shellcode"):
        check_module_loaded("ConvertTo-Shellcode.ps1", randomuri, user)
    elif command.lower().strip().startswith("decrypt-rdcman"):
        check_module_loaded("Decrypt-RDCMan.ps1", randomuri, user)
    elif command.lower().strip().startswith("dump-ntds"):
        check_module_loaded("Dump-NTDS.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-computerinfo"):
        check_module_loaded("Get-ComputerInfo.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-creditcarddata"):
        check_module_loaded("Get-CreditCardData.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-gppautologon"):
        check_module_loaded("Get-GPPAutologon.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-gpppassword"):
        check_module_loaded("Get-GPPPassword.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-idletime"):
        check_module_loaded("Get-IdleTime.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-ipconfig"):
        check_module_loaded("Get-IPConfig.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-keystrokes"):
        check_module_loaded("Get-Keystrokes.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-hash"):
        check_module_loaded("Get-Hash.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-locadm"):
        check_module_loaded("Get-LocAdm.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-mshotfixes"):
        check_module_loaded("Get-MSHotFixes.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netstat"):
        check_module_loaded("Get-Netstat.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-passnotexp"):
        check_module_loaded("Get-PassNotExp.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-passpol"):
        check_module_loaded("Get-PassPol.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-recentfiles"):
        check_module_loaded("Get-RecentFiles.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-serviceperms"):
        check_module_loaded("Get-ServicePerms.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-userinfo"):
        check_module_loaded("Get-UserInfo.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-wlanpass"):
        check_module_loaded("Get-WLANPass.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-pbind"):
        check_module_loaded("Invoke-Pbind.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-domaingroupmember"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-kerberoast"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("resolve-ipaddress"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-userhunter"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-daisychain"):
        check_module_loaded("invoke-daisychain.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-hostenum"):
        check_module_loaded("HostEnum.ps1", randomuri, user)
    elif command.lower().strip().startswith("inject-shellcode"):
        check_module_loaded("Inject-Shellcode.ps1", randomuri, user)
    elif command.lower().strip().startswith("inveigh-relay"):
        check_module_loaded("Inveigh-Relay.ps1", randomuri, user)
    elif command.lower().strip().startswith("inveigh"):
        check_module_loaded("Inveigh.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-arpscan"):
        check_module_loaded("Invoke-Arpscan.ps1", randomuri, user)
    elif command.lower().strip().startswith("arpscan"):
        check_module_loaded("Invoke-Arpscan.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-dcsync"):
        check_module_loaded("Invoke-DCSync.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-eventvwrbypass"):
        check_module_loaded("Invoke-EventVwrBypass.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-hostscan"):
        check_module_loaded("Invoke-Hostscan.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-ms16-032-proxy"):
        check_module_loaded("Invoke-MS16-032-Proxy.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-ms16-032"):
        check_module_loaded("Invoke-MS16-032.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-mimikatz"):
        check_module_loaded("Invoke-Mimikatz.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-psinject"):
        check_module_loaded("Invoke-PSInject.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-pipekat"):
        check_module_loaded("Invoke-Pipekat.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-portscan"):
        check_module_loaded("Invoke-Portscan.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-powerdump"):
        check_module_loaded("Invoke-PowerDump.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-psexec"):
        check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-reflectivepeinjection"):
        check_module_loaded("Invoke-ReflectivePEInjection.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-reversednslookup"):
        check_module_loaded("Invoke-ReverseDnsLookup.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-runas"):
        check_module_loaded("Invoke-RunAs.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-smblogin"):
        check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-smbclient"):
        check_module_loaded("Invoke-SMBClient.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-smbexec"):
        check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-psexec"):
        check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-shellcode"):
        check_module_loaded("Invoke-Shellcode.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-sniffer"):
        check_module_loaded("Invoke-Sniffer.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-sqlquery"):
        check_module_loaded("Invoke-SqlQuery.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-tater"):
        check_module_loaded("Invoke-Tater.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-thehash"):
        check_module_loaded("Invoke-TheHash.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-tokenmanipulation"):
        check_module_loaded("Invoke-TokenManipulation.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-wmichecker"):
        check_module_loaded("Invoke-WMIChecker.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-wmicommand"):
        check_module_loaded("Invoke-WMICommand.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-wscriptbypassuac"):
        check_module_loaded("Invoke-WScriptBypassUAC.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-winrmsession"):
        check_module_loaded("Invoke-WinRMSession.ps1", randomuri, user)
    elif command.lower().strip().startswith("out-minidump"):
        check_module_loaded("Out-Minidump.ps1", randomuri, user)
    elif command.lower().strip().startswith("portscan"):
        check_module_loaded("PortScanner.ps1", randomuri, user)
    elif command.lower().strip().startswith("powercat"):
        check_module_loaded("powercat.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-allchecks"):
        check_module_loaded("PowerUp.ps1", randomuri, user)
    elif command.lower().strip().startswith("set-lhstokenprivilege"):
        check_module_loaded("Set-LHSTokenPrivilege.ps1", randomuri, user)
    elif command.lower().strip().startswith("sharpsocks"):
        check_module_loaded("SharpSocks.ps1", randomuri, user)
    elif command.lower().strip().startswith("find-allvulns"):
        check_module_loaded("Sherlock.ps1", randomuri, user)
    elif command.lower().strip().startswith("test-adcredential"):
        check_module_loaded("Test-ADCredential.ps1", randomuri, user)
    elif command.lower().strip().startswith("new-zipfile"):
        check_module_loaded("Zippy.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netuser"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-aclscanner"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-dfsshare"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-objectacl"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("add-objectacl"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netuser"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-domainuser"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netcomputer"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-domaincomputer"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netuser"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netgroup"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netgroupmember"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netshare"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-sharefinder"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netdomain"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netdomaincontroller"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netforest"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("find-domainshare"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-netforestdomain"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-mapdomaintrust"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-wmireglastloggedon"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-wmiregcachedrdpconnection"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-wmiregmounteddrive"):
        check_module_loaded("powerview.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-wmievent"):
        check_module_loaded("Invoke-WMIEvent.ps1", randomuri, user)
    elif command.lower().strip().startswith("remove-wmievent"):
        check_module_loaded("Invoke-WMIEvent.ps1", randomuri, user)
    elif command.lower().strip().startswith("invoke-wmi"):
        check_module_loaded("Invoke-WMIExec.ps1", randomuri, user)
    elif command.lower().strip().startswith("get-lapspasswords"):
        check_module_loaded("Get-LAPSPasswords.ps1", randomuri, user)


def run_autoloads_sharp(command, randomuri, user):
    if command.lower().strip().startswith("run-exe seatbelt"):
        check_module_loaded("Seatbelt.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe sharpup"):
        check_module_loaded("SharpUp.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe safetydump"):
        check_module_loaded("SafetyDump.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe rubeus"):
        check_module_loaded("Rubeus.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe sharpview"):
        check_module_loaded("SharpView.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe watson"):
        check_module_loaded("Watson.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe sharphound"):
        check_module_loaded("SharpHound.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe internalmonologue"):
        check_module_loaded("InternalMonologue.exe", randomuri, user)
    elif command.lower().strip().startswith("run-exe sharpsocks"):
        check_module_loaded("SharpSocks.exe", randomuri, user)
    elif command.lower().strip().startswith("sharpsocks"):
        check_module_loaded("SharpSocks.exe", randomuri, user)
