import threading

class messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


send = messenger(name="Send Message")
receive = messenger(name="Receive Message")
send.start()
receive.start()

