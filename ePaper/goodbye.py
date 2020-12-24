import epd2in13
import traceback
from PIL import Image,ImageDraw,ImageFont
import datetime

try:
    epd = epd2in13.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    epd.init(epd.PART_UPDATE)    
    epd.Clear(0xFF)
    font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
    font17 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 17)
    
    time_image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)
    time_draw = ImageDraw.Draw(time_image)

    time_draw.rectangle((0, 0, 250, 60), fill = 255)
    time_draw.text((10, 10), "Goodbye!", font = font24, fill = 0)

    time_draw.text((10, 74), "Last seen:", font = font17, fill = 0)
    time_draw.text((10, 97), f"{datetime.datetime.now():%d, %B %Y at %H:%M:%S}", font = font17, fill = 0)

    newimage = time_image.crop([10, 10, 250, 60])
    time_image.paste(newimage, (10,10))  
    epd.displayPartial(epd.getbuffer(time_image))

except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()
