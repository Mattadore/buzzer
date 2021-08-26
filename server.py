from sanic import Sanic
from sanic.response import json, file
# import RPi.GPIO as GPIO
import asyncio


app = Sanic("Buzz app")

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(12, GPIO.OUT)
# GPIO.output(12, 0)


@app.route('/buzz')
async def test(request):
    # buzz ppl in
    # GPIO.output(12, 1)
    await asyncio.sleep(10)
    print("hi")
    # GPIO.output(12, 0)
    # return json({'it': 'worked'})  # I just don't want it failing or whatever


@app.route('/')
async def page(request):
    # return html page lol
    return await file('./site.html')

if __name__ == '__main__':
    app.run()
