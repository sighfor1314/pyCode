class Score():
    def __init__(self, score):
        self.__score = score

    @property
    def sc(self):
        return self.__score


    @sc.setter
    def sc(self, score):
        self.__score = score


stu = Score(0)
# print(stu.sc)
# stu.sc = 80
# print(stu.sc)
stu._Score__sc(50)
