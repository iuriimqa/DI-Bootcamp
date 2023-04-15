class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
            person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.priority or person.age > 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
        self.rearange_queue()

    def find_in_queue(self, person):
        for i, p in enumerate(self.humans):
            if p.id_number == person.id_number:
                return i
        return None

    def swap(self, person1, person2):
        i = self.find_in_queue(person1)
        j = self.find_in_queue(person2)
        if i is not None and j is not None:
            self.humans[i], self.humans[j] = self.humans[j], self.humans[i]
            self.rearange_queue()

    def get_next(self):
        if self.humans:
            person = self.humans.pop(0)
            self.rearange_queue()
            return person
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for i, person in enumerate(self.humans):
            if person.blood_type == blood_type:
                self.humans.pop(i)
                self.rearange_queue()
                return person
        return None

    def sort_by_age(self):
        priority_list = []
        older_list = []
        younger_list = []
        for person in self.humans:
            if person.priority:
                priority_list.append(person)
            elif person.age > 60:
                older_list.append(person)
            else:
                younger_list.append(person)
        self.humans = priority_list + older_list + younger_list
        self.rearange_queue()

    def rearange_queue(self):
        for i in range(len(self.humans) - 1):
            if self.humans[i].family and self.humans[i + 1].family:
                if self.humans[i].family[0] == self.humans[i + 1].family[0]:
                    for j in range(i + 2, len(self.humans)):
                        if not self.humans[j].family or self.humans[j].family[0] != self.humans[i].family[0]:
                            self.humans[i + 1], self.humans[j] = self.humans[j], self.humans[i + 1]
                            break

queue = Queue()
person1 = Human("1234", "John", 65, True, "A")
queue.add_person(person1)
person2 = Human("5678", "Mary", 35, False, "O")
queue.add_person(person2)
person3 = Human("2006", "Mike",75,True,"B")
queue.add_person(person3)
next_person = queue.get_next()
print(next_person.name)



