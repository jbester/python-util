import unittest
from .. import pubsub


class ShellTest(unittest.TestCase):
    def test_pubsub(self):
        domain = pubsub.Domain()
        called = False
        args = None

        def listener(*params):
            nonlocal called, args
            called = True
            args = params

        # verify callback not called before registration
        domain.emit('topic1')
        self.assertFalse(called)
        domain.register_listener('topic1', listener)
        self.assertFalse(called)
        # verify different topic doesn't trigger callback
        domain.emit('topic2')
        self.assertFalse(called)
        # verify topic *does* trigger callback
        domain.emit('topic1')
        self.assertTrue(called)
        # verify topic handler does get parameters
        domain.emit('topic1', 'a', 'b')
        self.assertEqual(('a', 'b'), args)

    def test_register_annotation(self):
        domain = pubsub.Domain()
        called = False
        # verify annotation causes registration

        @pubsub.register('topic1', domain)
        def listener(*params):
            nonlocal called
            called = True

        self.assertFalse(called)
        pubsub.emit('topic1', domain=domain)
        self.assertTrue(called)


if __name__ == '__main__':
    unittest.main()
