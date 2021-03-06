import paramiko
import time


def open_ssh_conn(ip):
    #Change exception message
    try:
        
        username = 'cat'
        password = 'dog'
        
        #Logging into device
        session = paramiko.SSHClient()
		
		#For testing purposes, this allows auto-accepting unknown host keys
		#Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
		#Passing the necessary parameters
        session.connect(ip, username = username, password = password,look_for_keys=False, allow_agent=False)
        #working for routers as well now with additional commands
        #credits - https://pynet.twb-tech.com/blog/python/paramiko-ssh-part1.html

		#Start an interactive shell session on the router
        connection = session.invoke_shell()	
        
        #Setting terminal length for entire output - no pagination
        cmd = 'term len 0 \nsh ip int brief\n'
        connection.send(cmd)
        time.sleep(1)

        output = connection.recv(65535)
        print(output)

        session.close()

    except paramiko.AuthenticationException:
        print ("* Invalid username or password. \n* Please check the username/password file or the device configuration!")
        print ("* Closing program...\n")

#ip = '192.168.56.101'
ip = '10.1.2.1'
open_ssh_conn(ip)