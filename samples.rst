******
Sample
******

import cbc
import cbc.network
from cbc import Color

def on_event(e):
    cbc.display.pixels[0,2] = Color(e.decode())

ws = cbc.network.WebSocketClient(url="ws://cheerlights.codebug.org.uk/cheer/", on_data=on_event)