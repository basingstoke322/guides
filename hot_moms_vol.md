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
