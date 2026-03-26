import serial      # lets me read data coming from the Arduino over USB/COM port
import asyncio     # used for running an async loop without blocking
import websockets  # allows me to create a WebSocket server for the website
import time        # gives me sleep() for small delays

# Try to open the Arduino's COM port
try:
    ser = serial.Serial('COM6', 115200, timeout=1)  # COM6, baud=115200
    time.sleep(2)                                   # give Arduino a moment to reset
    print("connected to Arduino")
except Exception as e:
    # If the port doesn't exist or is busy, I see the error here
    print(f"Error:{e}")

# This function runs whenever the website connects to the WebSocket
async def handler(websocket):
    print("Website connected to bridge!")
    
    while True:
        # Read from Arduino if there is data waiting
        while ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()  # read + decode + clean it up
            print(data)                                    # show the value in console
            await websocket.send(data)                     # send the value to browser
        
        # Tiny delay so the loop doesn't eat 100% CPU
        await asyncio.sleep(0.01)

# Start a WebSocket server on localhost:8081
async def main():
    print("Bridge is running on COM5... Refresh your website!")
    
    # Run the WebSocket server forever
    async with websockets.serve(handler, "localhost", 8081):
        await asyncio.Future()  # never ends → keeps server alive

# Start the async event loop
if __name__ == "__main__":
    asyncio.run(main())