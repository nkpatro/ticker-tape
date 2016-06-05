from __future__ import print_function
import time


# TODO: add thread locking for _events

class Reporter:
    """
    Receives FeedEvents from FeedHandlers and decides upon
    the order in which to publish FeedEvents.
    """

    def __init__(self, tape):
        self._events = []
        self._tape = tape

    def report(self):
        self.print_status()
        for e in self._events:
            self._tape.display(e.content)

        self._events = []

    def receive(self, event):
        print('Reporter receiving event: {}'.format(event))
        self._events.append(event)

    def print_status(self):
        if self._events:
            print('{0} new events received'.format(len(self._events)))
        else:
            print('No new events received')
