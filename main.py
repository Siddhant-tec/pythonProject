class Jumps:
    def __init__(self, size, my_list):
        self.size = size
        self.my_list = my_list

    def minimum_jump(self):
        jump = 0
        i = 0
        while i <= self.size:
            try:
                if self.my_list[i] == 0:
                    print("0 encountered")
                    i += 1
                else:
                    i += self.my_list[i]
                    jump += 1
                    # print("jumped to: ", self.my_list[i], "Jump: ", jump)
            except IndexError:
                print(jump)
                exit()
        print(jump)


size = int(input("Enter size: "))
list = [int(x) for x in input("Enter list: ").split()]
jp = Jumps(size, list)
jp.minimum_jump()
