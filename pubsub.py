import collections
from typing import Callable, Any, Optional


class Domain:
    """Communication domain"""
    def __init__(self):
        self._subscribers = collections.defaultdict(list)
        self._events = []
        self._in_progress = False

    def register_listener(self, topic: Any, handler: Callable[[Any], None]):
        """Listen to the topic specified

        :param topic: topic to listen for
        :param handler: method, static method, or function to handle the topic
        :return: None
        """
        self._subscribers[topic].append(handler)

    def emit(self, topic: Any, *args, **kw):
        """Send a topic

        Note: this function preserves global ordering of topics.
        If you emit topic A which in turn emits topic B.  All handlers
        of A will be called prior to any processing of topic B

        :param topic: topic id
        :param args: ordered arguments
        :param kw: keyword arguments
        """
        self._events.append((topic, args, kw))
        # if an event sends an additional event queue it up
        # this ensures global ordering of topics i.e.
        # if you have an ordered set of three topics A, B, C
        # all of A handlers are processed prior to B being processed
        if not self._in_progress:
            self._in_progress = True
            while len(self._events) > 0:
                (topic, args, kw) = self._events.pop(0)
                for listener in self._subscribers[topic]:
                    try:
                        listener(*args, **kw)
                    finally:
                        pass
            self._in_progress = False


DEFAULT = Domain()


def register(topic_id: Any, domain: Optional[Domain] = None):
    """Decorator that registers for the specified topic id

    :param topic_id: topic to listen for
    :param domain: communication domain (DEFAULT if NOne)
    """
    def register_internal(fn):
        nonlocal domain, topic_id
        if domain is None:
            domain = DEFAULT
        domain.register_listener(topic_id, fn)
    return register_internal


def emit(topic_id: Any, *args, domain: Optional[Domain] = None, **kw):
    """Emit a topic

    Note: this function preserves global ordering of topics.
    If you emit topic A which in turn emits topic B.  All handlers
    of A will be called prior to any processing of topic B
    :param topic_id: topic name
    :param domain: communication domain
    :param args: ordered arguments
    :param kw: keyword arguments
    """
    domain = domain or DEFAULT
    domain.emit(topic_id, *args, **kw)


