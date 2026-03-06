class Person(object):
    
    ## 限制class裡面只能有這些屬性
    __slots__=("_name","_age","_gender")

    
    def __init__(self,name,age):
        self._name=name
        self._age=age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age=age

    def play(self):
        if self._age <= 16:
            print("%s 正在玩手機"%self._name)
        else:
            print("%s 正在玩電腦"%self._name)



def main():
    person=Person("Andy",22)
    person.play()
    person.gender="男"
