# Python code to handle SSHException in Paramiko
import paramiko

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.1.196', username='john', password='demo', look_for_keys=False, allow_agent=False)
    stdin, _stdout,_stderr = client.exec_command('show clock')
    print(_stdout.read().decode())
    
except paramiko.ssh_exception.SSHException as e:
    print(f"Caught SSHException: {e}")
finally:
    client.close()
