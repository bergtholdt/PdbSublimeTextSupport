import os, sys
import os.path

from os.path import exists

def launch(self):
    frame, lineno = self.stack[self.curindex]
    filename = self.canonic(frame.f_code.co_filename)
    if exists(filename):
        if sys.platform == 'win32':
            import subprocess
            command = ["subl.exe", '-b', "%s:%d" % (filename, lineno)]
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            if input is not None:
                p = subprocess.Popen(command, stdout=subprocess.PIPE, startupinfo=startupinfo)
        else:
            command = 'subl -b "%s:%d"' % (filename, lineno)
            os.system(' '.join(command))


def preloop(self):
    launch(self)

def precmd(self, line):
    launch(self)
    return line
