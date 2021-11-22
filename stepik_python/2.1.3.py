# https://stepik.org/lesson/24463/step/9?unit=6771
class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError()
        else:
            super(PositiveList, self).append(x)
            # or list.append(self, x)


def main():
    l = PositiveList()
    l.append(1)
    print(l)
    l.append(-2)


if __name__ == '__main__':
    main()
