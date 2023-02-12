import asyncio
import logging
from unittest.mock import MagicMock, patch
from cbpi.api import *

logger = logging.getLogger(__name__)

try:
    import RPi.GPIO as GPIO
except Exception:
    logger.warning("Failed to load RPi.GPIO. Using Mock instead")
    MockRPi = MagicMock()
    modules = {
        "RPi": MockRPi,
        "RPi.GPIO": MockRPi.GPIO
    }
    patcher = patch.dict("sys.modules", modules)
    patcher.start()
    import RPi.GPIO as GPIO

mode = GPIO.getmode()
if (mode == None):
    GPIO.setmode(GPIO.BCM)

@parameters([Property.Select(label="GPIO", options=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]), 
             Property.Select(label="Pull_Up_Down", options=["Up", "Down"],description="Use internal Pull Up resistor (actor is ON when GPIO is Low) or Pull Down resistor (actor is ON when GPIO is High)")])
class GPIOInputActor(CBPiActor):
    
    async def on_start(self):
        self.gpio = self.props.GPIO
        self.pud = GPIO.PUD_UP if self.props.get("Pull_Up_Down", "Down") == "Up" else GPIO.PUD_DOWN
        self.state = False
        GPIO.setup(self.gpio, GPIO.IN, pull_up_down=self.pud)

    def get_state(self):
        return self.state
        
    async def run(self):
        while self.running == True:
            if self.pud == GPIO.PUD_UP and GPIO.input(self.gpio) == GPIO.LOW:
                self.state = True
            elif self.pud == GPIO.PUD_DOWN and GPIO.input(self.gpio) == GPIO.HIGH:
                self.state = True
            else:
                self.state = False
            await asyncio.sleep(1)
            
def setup(cbpi):

    '''
    This method is called by the server during startup 
    Here you need to register your plugins at the server
    
    :param cbpi: the cbpi core 
    :return: 
    '''

    cbpi.plugin.register("GPIO Input Actor", GPIOInputActor)
