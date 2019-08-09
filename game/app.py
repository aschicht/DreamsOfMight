import sys

from engine import Engine

__author__ = 'rumm'


class App:
    def __init__(self):
        self.engine = Engine()

    def run(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == "--step":
                self.engine.run_step_dungeon()
        else:
            self.engine.run()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
