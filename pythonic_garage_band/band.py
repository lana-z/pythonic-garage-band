class Band:

    instance = []

    def __init__(self, name):
        self.name = name
        self.members = members if members is not None else []
        Band.instance.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
    
    def __str__(self):
        return f"Band name: {self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"
    
    @classmethod
    def to_list(cls):
        return cls.instance

class Musician:

    def __init__(self, name="unknown"):
        self.name = name

    def get_instrument(self):
        raise NotImplementedError
    


class Guitarist(Musician):
    def __init__(self, name):
       super().__init__(name)
       self.instrument = "guitar"
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"[{self.instrument}ist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"
    
class Bassist(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.instrument = "bass"
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
 
    def __repr__(self):
        return f"{self.instrument}ist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.instrument = "drums"
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument
    
    def play_solo(self):
        return "rattle boom crash"