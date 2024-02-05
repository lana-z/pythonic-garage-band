class Band:
    
    """
    A class for bands
        name: str
        members: list
    """

    instance = []

    def __init__(self, name, members=None):
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
    """
    A class for musicians
        name: str
    """

    def __init__(self, name="unknown"):
        self.name = name

    def get_instrument(self):
        raise NotImplementedError


class Guitarist(Musician):

    """
    A class for guitarists
        Inherits from Musician
    """

    def __init__(self, name):
       super().__init__(name)
       self.instrument = "guitar"
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"
    

class Bassist(Musician):

    """
    A class for bassists
        Inherits from Musician
    """

    def __init__(self, name="unknown"):
        self.name = name
        self.instrument = "bass"
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
 
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):

    """
    A class for drummers
        Inherits from Musician
    """

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