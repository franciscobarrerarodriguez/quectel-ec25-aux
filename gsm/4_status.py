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

send_at('AT+QCFG="nwscanseq",00')

send_at('AT+QCFG="nwscanmode",0,1')

send_at('AT+QCFG="roamservice",255,1')

send_at('AT+QCFG="servicedomain",2,1')

send_at('AT+QCFG="band",0000FFFF,0,0,1')

send_at('ATE1')

send_at('AT+CMEE=2')

send_at('AT+CFUN=1,1')

time.sleep(60)

send_at()

send_at('ATE1')

send_at('AT+CMEE=2')
