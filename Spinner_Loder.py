import threading
import sys
import time


class SpinnerThread(threading.Thread):
    def __init__(self):
        print("\n")
        super().__init__(target=self._spin)
        self._stopevent = threading.Event()

    def stop(self):
        self._stopevent.set()
        time.sleep(1)

    def _spin(self):
        while not self._stopevent.isSet():
            for t in "|/-\\":
                sys.stdout.write(t)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write("\b")
