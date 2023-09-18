class Apple:
    #Класс яблока
    # ii.	Стадии созревания (цветение, зеленое, красное) - список хранится в классе, как константа
    maturation = ["flower", "green", "red"]

    def __init__(self, index, maturation_stage=maturation[0]):
        # i.	индекс - принимается при инициализации
        self.index = index
        # iii.	Стадия созревания - создается при инициализации, по умолчанию первое значение из списка стадий
        self.maturation_stage = maturation_stage

    def mature(self):
        # i.созревать(переходить на следующую стадию созревания)
        self.maturation_stage = self.maturation[self.maturation.index(self.maturation_stage) + 1]

    def ready(self):
        # ii.предоставлять информацию о своей зрелости - если яблоко созрело метод возвращает True иначе False
        if self.maturation_stage == "red":
            return True
        else:
            return False


class Tree:
    #Класс дерева
    def __init__(self, *args):
        #i.	дерево содержит список яблок которые на нем растут - яблоки принимаются при инициализации, как неизвестное кол-во параметров. Сохраняются в список
        self.apples = list(args)

    def grow(self):
        #i.	расти вместе с яблоками - т.е. каждое яблоко должно созреть на 1 стадию.
        for apple in self.apples:
            apple.mature()

    def tree_ready(self):
        #ii.	предоставлять информацию о зрелости всех яблок - если все яблоки созрели возвращать True иначе False.
        for apple in self.apples:
            if apple.ready() == False:
                break
            else:
                return True
        return False

    def harvest_tree(self):
        #iii.	предоставлять урожай - удалять все яблоки.
        self.apples = list()

class Gardener:

    def __init__(self, name, *args):
        #i.	имя - принимается  при инициализации.
        self.name = name
        #ii.	растения, за которыми следит - принимаются при инициализации, как неизвестное кол-во параметров. Сохраняются в список
        self.trees = list(args)

    def care(self):
        #i.	ухаживать за растениями - для каждого растения вызывать метод роста
        for tree in self.trees:
            tree.grow()

    def harvest_all(self):
        #ii.	собирать урожай - удалять все яблоки - только в том случае если все яблоки созрели. Иначе выдавать предупреждение.
        # i - счетчик, если ли незрелые яблоки. если i=1, то не дает собрать
        i = 0
        for tree in self.trees:
            if tree.tree_ready() == False:
                i = 1
        if i == 1:
            print("NO!")
        else:
            for tree in self.trees:
                tree.harvest_tree()
            print("Урожай собран!")

#Для тестирования:создайте 5 яблок, 1 дерево и 1 садовника
apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)
apple4 = Apple(4)
apple5 = Apple(5)
tree1 = Tree(apple1, apple2, apple3, apple4, apple5)
IvanPetrov = Gardener("Ivan Petrov", tree1)
IvanPetrov.harvest_all()
IvanPetrov.care()
IvanPetrov.harvest_all()
IvanPetrov.care()
IvanPetrov.harvest_all()
