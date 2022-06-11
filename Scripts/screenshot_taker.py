from PIL import ImageGrab
import time

im = ImageGrab.grab()

moment = time.strftime("%Y-%b-%d_%H_%M_%S",time.localtime())

im.save(savetime+"SS.jpg")
