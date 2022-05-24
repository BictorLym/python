class TV:
    #def __init__(self, c, v):
        #self.channel = c
        #self.volume = v
        #self.on = 1
    def turnOn(self):
        self.on = 1
    def turOff(self):
        self.off = 0
    def setChannel(self, channel):
        self.channel = channel
    def setVolume(self, volum):
        self.volume = volum



mytv = TV()
mytv.setChannel(11)
mytv.setVolume(6)
print(f'TV의 채널: {mytv.channel}   TV의 음량: {mytv.volume}')
