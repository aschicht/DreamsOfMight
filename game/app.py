from engine import Engine

__author__ = 'rumm'


class App:
    def __init__(self):
        self.engine = Engine()

    def run(self):
        self.engine.run()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
