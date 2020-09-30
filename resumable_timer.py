from threading import Timer
import time

class ResumableTimer:
    """A timer which can be paused and resumed again."""

    def __init__(self, timeout, callback):
        self.timeout = timeout
        self.callback = callback
        self.timer = Timer(self.timeout, self.callback)
        self.active = False

    def start(self):
        self.timer.start()
        self.active = True
        self.start_time = time.time()

    def cancel(self):
        self.timer.cancel()
        self.active = False

    def pause(self):
        if self.active:
            self.timer.cancel()
            self.active = False
            self.pause_time = time.time()
            self._calculate_remaining_time()

    def resume(self):
        if not self.active:
            self.timer = Timer(self.timeout, self.callback)
            self.timer.start()
            self.active = True
            self.start_time = time.time()

    def _calculate_remaining_time(self):
         self.timeout = self.timeout - (self.pause_time - 
            self.start_time)