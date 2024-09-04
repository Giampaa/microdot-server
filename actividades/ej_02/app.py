from boot import do_connect
from boot import led1, led2, led3
from microdot import Microdot, send_file

do_connect()
app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def index(request, dir, file):
    return send_file("/{}/{}".format(dir, file))

@app.route('/led/toggle/<led>')
async def led_toggle(request, led):

    if led == "led1":
        led1.value(not led1.value())

        #añadir el resto de ifs y probar
app.run(port=80)