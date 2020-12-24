import epd2in13

try:
    epd = epd2in13.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

except:
    print('error')
    exit()
