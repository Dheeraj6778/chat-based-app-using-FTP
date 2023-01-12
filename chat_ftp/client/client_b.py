from ftplib import FTP
import os
ftp = FTP(timeout=30)
host = '10.1.38.38'
port = 2121
ftp.connect(host, port)
ftp.login()


print(ftp.pwd())

while True:
    print('Enter 1 for reading message\n')
    print('Enter 2 to send message\n')
    print('Enter 3 to exit\n')
    command = input()
    if command == "1":
        #for reading message
        ftp.cwd('./b')

        def display(mesg):
            print(mesg)
        files = []
        ftp.dir(files.append)
        for file in files:
            lst = file.split(' ')
            fname = lst[-1]
            ftp.retrbinary('RETR '+fname, display, 1024)
            ftp.delete(fname)
        ftp.cwd('..')

    elif command == "2":
        send_to = input(
            'Enter the person to which you want to send message to : a b c d e\n')
        fpath = 'from_b.txt'
        f = open(fpath, 'w')
        mesg = input('Enter the message: ')
        f.write('b: '+mesg+'\n')
        f.close()
        server_path = './'+send_to+'/'+fpath
        with open(fpath, 'rb') as text_file:
            ftp.storbinary('STOR '+server_path, text_file)
    elif command == "3":
        break
    elif command == "WHO AM I":
        print("client B")
