"""
实现猫狗队列，要求如下:
1.用户可以调用add方法将cat类或dog类的实例放入队列中
2.用户可以调用pollAll方法，将队列中所有的实例按照进队列的先后顺序依次弹出
3.用户可以调用pollDog方法，将队列中所有dog类的实例按照进队列的先后顺序依次弹出
4.用户可以调用pollCat方法，将队列中所有cat类的实例按照进队列的先后顺序依次弹出
5.用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例
6.用户可以调用isDogEmpty方法，检查队列中是否还有dog的实例
7.用户可以调用isCatEmpty方法，检查队列中是否还有cat的实例

"""
from ArrayQueue import ArrayQueue
class Pet(object):
    def __init__(self, pettype):
        self.pettype = pettype
    
    def get_pettype(self):
        return self.pettype
    
    def __repr__(self):
        return self.pettype
    
class Dog(Pet):
    def __init__(self):
        Pet.__init__(self,"dog")

class Cat(Pet):
    def __init__(self):
        Pet.__init__(self,"cat")


class PetCount(object):
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count
    
    def getCount(self):
        return self.count
    
    def getpet(self):
        return self.pet
    
    def gettype(self):
        return self.pet.get_pettype()
    

class CatDogQueue(object):
    def __init__(self):
        self.dogqueue = ArrayQueue()
        self.catqueue = ArrayQueue()
        self.count = 0
    
    def add(self,pet):
        if pet.get_pettype() == "dog":
            self.count += 1
            petcount = PetCount(pet, self.count)
            self.dogqueue.push(petcount)
        elif pet.get_pettype() == "cat":
            self.count += 1
            petcount = PetCount(pet,self.count)
            self.catqueue.push(petcount)
        else:
            raise RuntimeError("no pet type")
    
    def pollall(self):
        if not self.isCatEmpty() and not self.isDogEmpty():
            if (self.dogqueue.peek().getCount()) < (self.catqueue.peek().getCount()):
                return self.dogqueue.poll()
            else:
                return self.catqueue.poll()
        elif self.isDogEmpty():
            return self.catqueue.poll()
        elif self.isCatEmpty():
            return self.dogqueue.poll()
        else:
            raise RuntimeError("err, queue is empty")
    
    def pollDog(self):
        if not self.isDogEmpty():
            # print(type(self.dogqueue.poll()))
            return  self.dogqueue.poll()
        else:
            raise RuntimeError("Dog queue is empty")

    def pollCat(self):
        if not self.isCatEmpty():
            return self.catqueue.poll()
        else:
            raise RuntimeError("Cat queue is empty")


    def isCatEmpty(self):
        return self.catqueue.isEmpyt()
    
    def isDogEmpty(self):
        return self.dogqueue.isEmpyt()


if __name__ == "__main__":
    test = CatDogQueue()
    dog1 = Dog()
    dog2 = Dog()
    cat1 = Cat()
    cat2 = Cat()
    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    while not test.isDogEmpty():
        dogpet = test.pollDog()
        print(dogpet.gettype())
        # print()
    while not test.isDogEmpty() and not test.isCatEmpty():
        print(test.pollall().gettype())
    dog3 = Dog()
    test.add(dog3)
    while not test.isCatEmpty():
        print(test.pollCat().gettype())