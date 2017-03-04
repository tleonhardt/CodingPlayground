#!/usr/bin/env python
# coding=utf-8
"""
This module is a simple Producer/Consumer example of sending data between threads in a queue.
"""
import random
import threading
import time

# Python 3 has "queue" but Python 2 has "Queue"
try:
    import queue
except ImportError:
    import Queue as queue


class Producer:
    """A Producder puts plates of food on the table."""
    def __init__(self):
        self.food = ["ham", "soup", "salad"]
        # nextTime simply randomizes the amount of time inbetween putting a new plate of food on the table
        self.nextTime = 0

    def run(self):
        """Thread function for Producer class - puts food in the table queue"""
        global q
        # Only run for up to 10 seconds
        while time.clock() < 10:
            if self.nextTime < time.clock():
                f = self.food[random.randrange(len(self.food))]
                q.put(f)
                print("Adding " + f)
                # Wait between 0.0 and 1.0 seconds before putting more food on the table
                self.nextTime += random.random()


class Consumer:
    """A Consumer consumes plates of food on the table."""
    def __init__(self):
        self.nextTime = 0

    def run(self):
        """Thread function for Consumer class - gets food from the table queue"""
        global q
        while time.clock() < 10:
            if self.nextTime < time.clock() and not q.empty():
                f = q.get()
                print("Removing " + f)
                # Make the consumer slower than the producer, on averge
                self.nextTime += random.random() * 2


if __name__ == '__main__':
    # FIFO queue representing the order in which food is placed on the table
    q = queue.Queue(10)

    p = Producer()
    c = Consumer()

    pt = threading.Thread(target=p.run, args=())
    ct = threading.Thread(target=c.run, args=())

    pt.start()
    ct.start()
