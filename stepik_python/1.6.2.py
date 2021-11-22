#https://stepik.org/lesson/24462/step/8?unit=6768
class ExtendedStack(list):
    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)


def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0


def main():
    test()


if __name__ == '__main__':
    main()
