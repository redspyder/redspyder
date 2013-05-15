import subprocess, threading, os

##################################################################################################################################
# Class agTimeout
# Usage:
#   agTimeout([cmd, args,], timeout).Run()
#       cmd: command to be run
#       args: arguments to command
#       timeout: time in seconds to permit thread to execute
# Output:
#   stdout if timeout occurs
##################################################################################################################################

class agTimeout(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        print os.getcwd()
        self.timeout = timeout
        self.out = ""
        self.err = ""

    #Override
    def run(self):
        self.p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.p.wait()
        self.out = self.p.stdout.read()
        self.err = self.p.stderr.read()
        
    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            print("taking too long, terminating it.")
            self.p.terminate()
            self.join()
        return [self.out,self.err]
        
# Example usage: (runs sleep for 5 seconds, timeout in 4 seconds)
#agTimeout(["sleep", "5"], 4).Run()

