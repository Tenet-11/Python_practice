from time import time,localtime,sleep

class Clock:
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second

    @classmethod
    # 這是類別的方法，要操作的是類別本身
    def now(cls):
        ctime=localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)
    
    def run(self):
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1
            if self._minute==60:
                self._minute=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0
    
    def show(self):
        return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"

def main():
    clock=Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()