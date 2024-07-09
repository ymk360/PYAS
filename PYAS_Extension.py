from subprocess import *
import os, re, sys

class ExtenRules:
    def __init__(self):
        self.exten = {}
        self.pyas = sys.argv[0].replace("\\", "/")
        self.dir = os.path.dirname(self.pyas)
        self.exten = os.path.join(self.dir, "Exten")

    def bdc_scan(self, file):
        if self.exten.replace("\\", "/") not in file.replace("\\", "/"):
            cmd = f'"{self.exten}\\Bitdefender\\bdc.exe" "{file}"'
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True)
            for matchs in re.finditer(r'(?P<filename>[^\s]+)\s+infected:\s+(?P<virusname>.+)', p.communicate()[0]):
                return matchs
        return False

    def mem_scan(self, p):
        if self.exten.replace("\\", "/") not in p.exe().replace("\\", "/"):
            cmd = f'"{self.exten}\\hollows_hunter\\hollows_hunter.exe" /ofilter 2 /pid "{p.pid}"'
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True)
            return 'Detected' in p.communicate()[0]
        return False
