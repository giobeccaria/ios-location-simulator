import subprocess
import os

os.environ['PATH'] += os.pathsep + '/sbin'

def run_command_with_sudo(command, password):
    try:
        command_str = ' '.join(command)
        print(f"\nExecuting command: sudo -S {command_str}")
        process = subprocess.Popen(['sudo', '-S'] + command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=password + '\n')
        print(stdout)
        if stderr:
            print(stderr)
        return stdout, stderr
    except Exception as e:
        print(f"\nError executing command with sudo: {e}")
        return None, None
