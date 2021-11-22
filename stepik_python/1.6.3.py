import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, msg):
        super(LoggableList, self).append(msg)
        super(LoggableList, self).log(msg)


def main():
    a = LoggableList()
    a.append('msg 1')
    a.append('msg 2')
    print(a)


if __name__ == '__main__':
    main()
