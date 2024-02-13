#!/usr/bin/python
import nmap
nm = nmap.PortScanner()
print (nm.nmap_version())
nm.scan('142.250.71.51', '1-1024', '-v --version-all')
print (nm.scanstats())
print(nm.all_hosts())
print (nm['142.250.71.51'].state())
print (nm['142.250.71.51'].all_protocols())
print (nm.scaninfo())
print (nm.csv())
