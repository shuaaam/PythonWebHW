from abc import ABCMeta, abstractmethod
import json
import pickle


class Serialization(metaclass=ABCMeta):
    def __init__(self, data, filename: str):
        self.data = data
        self.filename = filename

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class TypeJson(Serialization):

    def save(self):
        """
        Save data in JSON
        """
        with open(self.filename, 'w', encoding='UTF-8') as f:
            json.dump(self.data, f, ensure_ascii=False)

    def load(self):
        """
        Load data from JSON
        """
        with open(self.filename, 'r', encoding='UTF-8') as f:
            restore_data = json.load(f)
            print(restore_data)


class TypePickle(Serialization):

    def save(self):
        """
        Save data using pickle
        """
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)

    def load(self):
        """
        Load data using pickle
        """
        with open(self.filename, 'rb') as f:
            db = pickle.load(f)
        print(db)


def serialize(dat):
    if not isinstance(dat, Serialization):
        raise TypeError('Is not Serialization!')
    print('Data saved!')


test = {'name': 'Sasha', 'phone': ['0991831411', '0509934058'], 'age': 20}

j = TypeJson(test, 'saved.json')
j.save()
j.load()

p = TypePickle(test, 'saved.bin')
p.save()
p.load()

# serialize(j)
# serialize(p)
# serialize(str)
