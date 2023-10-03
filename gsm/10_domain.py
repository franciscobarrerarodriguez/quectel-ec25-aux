import serial as ser
import time

tty = '/dev/ttyUSB2'
bd = 9600

def send_at(command = "AT", response_size = 100, use_encode = True): 
    serial = ser.Serial(tty, bd, timeout=1)
    print('Executing {}'.format(command))
    if use_encode:
        formatCommand = command.encode() + b'\r\n'
    else:
        formatCommand = command
    serial.write(formatCommand)
    while serial.inWaiting() == 0:
        print("Waiting...")
        time.sleep(0.5)
        pass
    response = serial.read(response_size)
    print(response.decode())
    serial.close()

send_at()

send_at('ATV1')

send_at('AT+CMEE=2')

send_at('AT+CGATT=1')

send_at('AT+CGQREQ?')

send_at('AT+CGQMIN?')

send_at('AT+CGEQREQ?')

send_at('AT+CGEQMIN?')

send_at('atcom AT+CGACT=0,1')

send_at('AT+CGPADDR=1')

send_at('AT+CGCLASS?')

send_at('AT+CGREG?')

send_at('AT+CGEREP?')

send_at('AT+CEREG=2')

