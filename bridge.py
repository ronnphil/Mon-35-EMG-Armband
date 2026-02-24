import serial # pyserial: allows Python talk to COM ports (Arduino)
import asyncio # built-in: event loops, sleeps
import websockets # interactive applications. Python can send commands and interact with the arduino

# Added error handling because the script crashed when COM6 was unplugged
try:
    ser = serial.Serial('COM6', 115200, timeout=1)
    print("Connected to Arduino on COM6")
except Exception as e:
    # if opening port fails (wrong port, permission issue).
    print("ERROR: Arduino not found. Check your cable!")
    print(e)

async def handler(websocket):
    while True:
        try:
            # Added check to see if serial exists before reading

            if 'ser' in locals() and ser.in_waiting > 0:
                # Read a line from serial, decode bytes to text, and strip newline
                data = ser.readline().decode('utf-8').strip()
                # send line to connected websocket client
                await websocket.send(data)
        except:
            pass
        await asyncio.sleep(0.05) 

# start a websocket server at localhost:8031
# run forvever
async def main():
    async with websockets.serve(handler, "localhost", 8081):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())