import math


class Disease(object):
    """
    A Disease is an illness

    Attributes:
        name: a string that is the name of the disease
        symptoms: a list of strings representing the symptoms
        dtype: an integer value symbolising the type of disease
        transmission: a list of strings representing the method(s)
        of transmission
        rarity: an int or float that represents number of cases per year
            cases per year/100,000
        likeness:an in or float representing how likely a person is to 
        have a disease, initially zero.
    Class Constants:
        BACT:Bacteria
        VIR=Virus
        FUNG=Fungus
        PAR=Parasite
        MENT=Mental disorder
        CAN=Cancer
    """
    BACT = 0
    VIR = 1
    FUNG = 2
    PAR = 3
    MENT = 4
    CAN = 5

    def __init__(self, name='', symps=[], dt=None, tr=[], r=1):
        """
        Initializes a Disease object

        Parameter name: name of disease
        Precondition name: non-empty string

        Parameter symps: list of symptoms
        Precondition symps: list of non-empty strings

        Parameter dt: one of the class constants
        Precondition dt: None or int between 0 and 5, inclusive
    
        Parameter tr: list of strings
        Precondition tr: empty list or list of non-empty strings

        Parameter r: int or float
        Precondition r: r is an int ot float
        """
        assert type(name) == str
        assert type(symps) == list
        assert type(dt) == int
        assert type(tr) == list
        assert type(r) == int or type(r)==float
        self.name = name
        self.symptoms = symps
        self.dtype = dt
        if dt==None:
          self.dtype = Disease.BACT
        self.transmission = tr
        self.rarity = r
        self.likeness=0

    def likehood(self, symps):
        """
        Determines likelyhood of disease based on given symptoms
        returns: an int or float representing likelyhood

        Parameter symps: list of symptoms
        Precondition symps: non-empty list of non-empty strings
        """
        assert type(symps) == list
        sums = 0
        for s in symps:
            if s in self.symptoms:
              	sums += 10 
            else:
                sums -= 20
        sums *= self.rarity
        return sums

    def setName(self,name):
        """
        Changes disease name.
        returns:None

        Parameter name: name of disease
        Precondition name: non-empty string
        """
        assert type(name)==str
        self.name=name

    def setSymp(self,symps):
        """
        Changes disease symptoms
        returns: None

        Parameter symps: list of symptoms
        Precondition symps: non-empty list of non-empty strings
        """
        assert type(symps)==list
        self.symptoms=symps
    
    def setType(self,dt):
        """
        Changes disease type
        returns: None

        Parameter dt: one of the class constants
        Precondition dt: None or int between 0 and 5, inclusive
        """
        assert type(dt)==int
        self.dtype=dt
    
    def setTransmission(self,tr):
        """
        Changes disease transmission
        returns: None

        Parameter tr: list of strings
        Precondition tr: empty list or list of non-empty strings
        """
        assert type(tr)==list
        self.transmission=tr

    def setRarity(self,r):
        """
        Changes disease rarity
        returns: None

        Parameter r: int or float
        Precondition r: r is an int ot float
        """
        assert type(r)==int or type(r)==float
        self.rarity=r

    def __str__(self):
        """
        Converts object into string format.
        returns:string of name along with disease type and transmission(if applicable)
        """
        dtypes=['bacteria','virus','fungus','parasite','mental disorder','cancer']
        trl=', '.join(self.transmission[:len(self.transmission)-1])
        if len(self.transmission)>1:
            s=self.name+' is a type of '+dtypes[self.dtype]+' that is transmitted through '+trl+', and '+self.transmission[len(self.transmission)-1]+'.'
        elif len(self.transmission)==1:
            s=self.name+' is a type of '+dtypes[self.dtype]+' that is transmitted through '+self.transmission[0]+'.'
        else:
            s=self.name+' is a type of '+dtypes[self.dtype]+'.'
        if self.dtype==Disease.MENT or self.dtype==Disease.CAN:
            s=self.name+' is a type of '+dtypes[self.dtype]+'.'
        return s
