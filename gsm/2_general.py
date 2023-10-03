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

send_at('ATE1')

send_at('AT+CMEE=2')

send_at('ATI')

send_at('AT+GMI')

send_at('AT+GMM')

send_at('AT+GMR')

send_at('AT+CGMI')

send_at('AT+CGMM')

send_at('AT+CGMR')

send_at('AT+GSN')

send_at('AT+CGSN')

send_at('ATQ0')

send_at('ATV1')

send_at('AT+CMEE=2')

