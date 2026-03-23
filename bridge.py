import requests
import asyncio
import websockets

async def handler(websocket):
    while True:
        try:
            RES = requests.get("http://192.168.4.1/sensor")

            if RES.status_code == 200:
                data = RES.text
                print(f"Sensor: {data}")
                await websocket.send(data)
            else:
                print(f"Server responds with status code: {RES.status_code}")
        except requests.ConnectionError:
            print("Connection time out")
        await asyncio.sleep(0.01)
 
async def main():
    print("Bridge running on wifi... Refresh your website!")
    async with websockets.serve(handler, "localhost", 8081):
        await asyncio.Future()
 
if __name__ == "__main__":
    asyncio.run(main())
