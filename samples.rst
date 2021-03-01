***********
Sample Code
***********

Joystick A arrows
=================

Coloured arrows dependent on direction of button A

.. code-block:: python

    import cbc
    def arrows():
        sprites = {}
        sprites['up'] = cbc.Drawable.from_string(
                                        5, 5,
                                        "  y  "
                                        " yyy "
                                        "yyyyy"
                                        "  y  "
                                        "  y ")
        sprites['right'] = cbc.Drawable.from_string(
                                        5, 5,
                                        "  g  "
                                        "  gg "
                                        "ggggg"
                                        "  gg "
                                        "  g  ")
        sprites['left'] = cbc.Drawable.from_string(
                                        5, 5,
                                        "  r  "
                                        " rr  "
                                        "rrrrr"
                                        " rr  "
                                        "  r  ")
        sprites['down'] = cbc.Drawable.from_string(
                                        5, 5,
                                        "  b  "
                                        "  b  "
                                        "bbbbb"
                                        " bbb "
                                        "  b  ")
        sprites['middle'] = cbc.Drawable.from_string(
                                        5, 5,
                                        "     "
                                        "  y  "
                                        " rmg "
                                        "  b  "
                                        "     ")
        def display_arrow(e):
            if e.action:
                cbc.display.draw(0,0,sprites[e.direction])
        print('adding callback on joystick_a to display arrows')
        cbc.joystick_a.on_direction_any = display_arrow


Force dependent colours (light painting)
========================================

CodeBug Connect's LEDs change colour dependent on the force applied (try gentle shaking)

.. code-block:: python
    import cbc
    def force_colour():
        sat = 1.0
        bright = 0.4
        for vec in cbc.accel_sensor:
            mag = vec.x*vec.x + vec.y*vec.y + vec.z*vec.z
            cbc.display.pixels[:, 0:5] = [[cbc.Color(h=mag/10.0, s=sat, b=bright)] * 5]*5

Pir Alarm
=========

.. code-block:: python

    from machine import Pin
    import cbc

    def pir_alarm():

        pir_power = Pin(18, Pin.OUT, value=1)
        pir = Pin(25, Pin.IN)


        def handle_pir(e):
            if pir.value():
                cbc.display.pixels[:, 0:5] = [[cbc.Color('red')] * 5]*5
            else:
                cbc.display.clear()
                
        pir.irq(handler=handle_pir, trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING)


Cheer lights
============

Tweet @cheerlights a colour and see your CodeBug Connect change colour. (You must have successfully setup a WiFi connection first)

.. code-block:: python

    import cbc
    from remote_manage import WebSocketClient
    from cbc import Color

    def on_event(e):
        cbc.display.pixels[0,2] = Color(e[1].decode())

    ws = WebSocketClient(url="ws://cheerlights.codebug.org.uk/cheer/", on_text_data=on_event)

    