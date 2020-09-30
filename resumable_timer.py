from threading import Timer
import time

class ResumableTimer:
    """A timer which can be paused and resumed again."""

    def __init__(self, timeout, callback):
        """Initialise resumable timer attributes."""
        self.timeout = timeout
        self.callback = callback
        self.timer = Timer(self.timeout, self.callback)
        self.active = False

    def start(self):
        """Start the timer, set timer to active and record the current time."""
        if not self.active:
            self.timer.start()
            self.active = True
            self.start_time = time.time()

    def cancel(self):
        """Stop the timer and set the timer to not active."""
        if self.active:
            self.timer.cancel()
            self.active = False

    def pause(self):
        """Cancel timer and record pause time to determine new timeout."""
        if self.active:
            self.timer.cancel()
            self.active = False
            self.pause_time = time.time()
            self._calculate_remaining_time()

    def resume(self):
        """Create new Timer but use the updated timeout."""
        if not self.active:
            self.timer = Timer(self.timeout, self.callback)
            self.timer.start()
            self.active = True
            self.start_time = time.time()

    def _calculate_remaining_time(self):
        """Calculate the remaining timeout from when the timer was paused."""
        self.timeout = self.timeout - (self.pause_time - 
            self.start_time)