import collections

Action = collections.namedtuple('Action', ['command'])


class Actionable:

    def handle_action(self):
        pass