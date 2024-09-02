import serial
import time
from p1 import conditions
import serial.tools.list_ports
from backend.dbConnector import dbconnect
mydb=dbconnect()
cursor=mydb.cursor()
def find_com_port(port_name):
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.device == port_name:
            return port.device
    return None

com_port = find_com_port('COM4')
if com_port:
    try:
        ser = serial.Serial(
            port=com_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        print("Connected to: " + ser.portstr)
        
        count = 0
        order = 2
        while True:
            # print("hi")
          
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("Card UID:"):
                uid = line[len("Card UID:"):].strip()
                print(f"{count}: {uid}")
                # cursor.execute(f"update cards set cardID='{uid}' where id = 7 ")
                cursor.execute(f"select id , type from cards where cardID='{uid}'")
                result = cursor.fetchone()
                if order % 2 == 0:
                    order = 1
                else:
                    order = 2
                print(f"order:{order} result: ", result)
                # mydb.commit()
                # result=[(0,"properties")]
                count += 1
               
                cursor.execute(f"insert into currenttransaction values ({order},{result[0]},'{result[1]}' )")
                cursor.execute(f"insert into log values ({count},{result[0]},'{result[1]}' )")
                mydb.commit()
                cursor.execute("select * from currenttransaction ")
                print(cursor.fetchall())
                if order==2:
                    # conditions()
                    print("out")
                    cursor.execute("delete from currenttransaction")
                    mydb.commit()
                #     # test()
                #     pass#add p1.py call
                # testing code
                

                #insertion code
                # cursor.execute(f"update cards set cardID='{uid}' where id={count}")
                # mydb.commit()
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()
else:
    print("COM port not found or not available")