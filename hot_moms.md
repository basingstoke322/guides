# Volatility  
**System info**  
vol.py -f “/path/to/file” windows.info  
**Process info**  
vol.py -f “/path/to/file” windows.pslist
vol.py -f “/path/to/file” windows.psscan
vol.py -f “/path/to/file” windows.pstree  
**Dump process with dll**  
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑pid <PID>  
**Memdump**  
vol.py -f “/path/to/file” -o “/path/to/dir” windows.memmap ‑‑dump ‑‑pid <PID>  
**Handles**  
vol.py -f “/path/to/file” windows.handles ‑‑pid <PID>  
**cmd**  
vol.py -f “/path/to/file” windows.cmdline  
**Network**  
vol.py -f “/path/to/file” windows.netscan  
vol.py -f “/path/to/file” windows.netstat  
**Registry**  
vol.py -f “/path/to/file” windows.registry.hivescan  
vol.py -f “/path/to/file” windows.registry.hivelist  
vol.py -f “/path/to/file” windows.registry.printkey  
vol.py -f “/path/to/file” windows.registry.printkey ‑‑key “Software\Microsoft\Windows\CurrentVersion”  
**Files**  
vol.py -f “/path/to/file” windows.filescan  
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles  
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑virtaddr <offset>  
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑physaddr <offset>  
**useful**  
vol.py -f “/path/to/file” windows.malfind  
# Binwalk
binwalk --dd ".*" file
# Event Log  
Logins  
4625 - Failed Login (Bruteforce)  
4624 - Succesful Login  
4648 - Logon was attempted using explicit credentials.  
4802 - Screensaver invoked.  
4778 - RDP session reconnected.  
4820 - Kerberos TGT was denied as the device does not meet the access control restrictions.  

USB Connected  
6416 - External device was recognized by the system.  

User account management events: (for example: Using 'net user create'  
4720 - User account created  
4722 - Account enabled  
4723 - Attempt to change account password  
4724 - Attempt to reset user account password  
4781 - The name of an account was changed  

Security policy change events:  
4712 - Created Security-enabled global group.  
4713 - Changed security-enabled global group.  
4714 - Member added to a security-enabled global group.  
4715 - Member was removed from a security-enabled global group.  

Log Cleared:  
104 - System Logs Cleared  
1102 - Security Audit Logs Cleared using wevtutil.exe  

Firewall events:  
5031 - Windows Firewall Service blocked an application from accepting incoming connections on the network.  
4950 - Windows Firewall setting has changed.  
4946 - Firewall rule added will result in changes made to Windows Firewall exception list.  
4947 - Firewall rule modified that will result in changes made to Windows Firewall exception list.  
4948 - Firewall rule deleted that will result in changes made to Windows Firewall exception list.  
4954 - Windows Firewall Group Policy settings has changed.  
5025 - Windows Firewall Service has been stopped.  
5030 - Windows Firewall Service failed to start.  

Security group management events:  
4728 - Member added to security global group  
4729 - Member removed from security global group.  
4732 - Member added to local security group.  
4735 - Security enabled local group was changed.  
4737 - Security enabled global group was changed.  

Audit file system:  
4670 - Permissions on an object were changed  

User Privileged:  
4673 - Privileged service was called and specified user exercised the user right specified in the Privileges field.  

Audit policy change events:  
4738 - User account was changed.  
4740 - User account was locked out.  
4756 - Member was added to a security universal group  
4757 - Member was removed from security universal group  
4767 - Account unlocked.  

Security configuration changes:  
4902 - Per-user audit policy table was created.  
4904 - Attempt was made to register a security event source.  
4907 - Auditing settings on object were changed.  
4912 - Per User Audit Policy was changed.  

Process Created:  
4688 - Process Created - https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4688  
4689 - Documents when a process ends - https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4689  
7045 - New service was installed in the system.  
