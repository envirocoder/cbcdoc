import cbc
from color import Color


cbc.display.pixels[0:,0:] = [
[Color('#000000'), Color('#000000'), Color('#66cccc'), Color('#66cccc'), Color('#66cccc')],
[Color('#000000'), Color('#66cccc'), Color('#000000'), Color('#000000'), Color('#000000')],
[Color('#66cccc'), Color('#000000'), Color('#000000'), Color('#66cccc'), Color('#66cccc')],
[Color('#66cccc'), Color('#000000'), Color('#66cccc'), Color('#000000'), Color('#000000')],
[Color('#66cccc'), Color('#000000'), Color('#66cccc'), Color('#000000'), Color('#66cccc')]]

# d  = array('L', font._to_colors(font.SmallFont.chars['small_font_Network'], Color('orange'), Color('black')))
# cbc.display.pixels[0:,0:] = d

#network
cbc.display.pixels[0:,0:] = [
[Color('#000000'), Color('#000000'), Color('#00FFFF'), Color('#000000'), Color('#000000')],
[Color('#000000'), Color('#00FFFF'), Color('#000000'), Color('#00FFFF'), Color('#000000')],
[Color('#00FFFF'), Color('#00FFFF'), Color('#00FFFF'), Color('#00FFFF'), Color('#00FFFF')],
[Color('#000000'), Color('#00FFFF'), Color('#000000'), Color('#00FFFF'), Color('#000000')],
[Color('#000000'), Color('#000000'), Color('#00FFFF'), Color('#000000'), Color('#000000')]]

#wifi2
cbc.display.pixels[0:,0:] = [
[Color('#000000'), Color('#000000'), Color('#000000'), Color('#000000'), Color('#000000')],
[Color('#000000'), Color('#000000'), Color('#000000'), Color('#000000'), Color('#000000')],
[Color('#f000f5'), Color('#f000f5'), Color('#000000'), Color('#000000'), Color('#000000')],
[Color('#000000'), Color('#000000'), Color('#f000f5'), Color('#000000'), Color('#000000')],
[Color('#f000f5'), Color('#000000'), Color('#f000f5'), Color('#000000'), Color('#000000')]]

#wifi3
cbc.display.pixels[0:,0:] = [
[Color('#00FFFF'), Color('#00FFFF'), Color('#00FFFF'), Color('#000000'), Color('#000000')],
[Color('#000000'), Color('#000000'), Color('#000000'), Color('#00FFFF'), Color('#000000')],
[Color('#00FFFF'), Color('#00FFFF'), Color('#000000'), Color('#000000'), Color('#00FFFF')],
[Color('#000000'), Color('#000000'), Color('#00FFFF'), Color('#000000'), Color('#00FFFF')],
[Color('#00FFFF'), Color('#000000'), Color('#00FFFF'), Color('#000000'), Color('#00FFFF')]]