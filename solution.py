from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 RECV reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recvHelo = clientSocket.recv(1024).decode()
    #print(recvHelo)
    #if recvHelo[:3] != '250':
    #    print('250 HELO reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFromCommand = ('MAIL FROM: <Alice@nyu.edu>\r\n')
    clientSocket.send(mailFromCommand.encode())
    recvMailFrom = clientSocket.recv(1024).decode()
    #if recvMailFrom[:3] != '250':
    #    print('250 MAIL FROM reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptToCommand = ('RCPT TO: <mjp269@nyu.edu>\r\n')
    clientSocket.send(rcptToCommand.encode())
    recvRcptTo = clientSocket.recv(1024).decode()
    #if recvRcptTo[:3] != '250':
    #    print('250 RCPT TO reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = ('DATA')
    clientSocket.send(dataCommand.encode())
    recvData = clientSocket.recv(1024).decode()
    #if recvData[:3] != '250':
    #    print('250 DATA reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = ('QUIT')
    clientSocket.send(quitCommand.encode())
    recvQuit = clientSocket.recv(1024).decode()
    #if recvQuit[:3] != '250':
    #    print('250 QUIT reply not received from server.')
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
