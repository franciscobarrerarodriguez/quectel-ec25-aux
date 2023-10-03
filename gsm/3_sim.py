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

print('AT+QSIMDET (U)SIM Card Detection')
print('The command enables (U)SIM card hot-swap function. (U)SIM card is detected by GPIO interrupt. The level of (U)SIM card detection pin should also be set when the (U)SIM card is inserted.')
send_at('AT+QSIMDET=1,1')

print('Done!, needs restart...')
send_at('AT+CFUN=1,1')
time.sleep(60)

send_at('ATE1')

send_at('AT+CMEE=2')

print('AT+QSIMSTAT (U)SIM Card Insertion Status Report')
print('The command queries (U)SIM card insertion status or determines whether (U)SIM card insertion status report is enabled. The configuration of this command can be saved by AT&W.')
send_at('AT+QSIMSTAT=1')