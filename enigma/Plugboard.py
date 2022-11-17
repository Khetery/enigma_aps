class Plugboard :
    wiring = None
    def __init__(self, connections) :
        self.wiring = self.decodePlugboard(connections)
   
    def  forward(self, c) :
        return self.wiring[c]
    
    @staticmethod
    def  identityPlugboard() :
        mapping = [0] * (26)
        i = 0
        while (i < 26) :
            mapping[i] = i
            i += 1
        return mapping
   
    @staticmethod
    def  getUnpluggedCharacters( plugboard) :
        unpluggedCharacters =  set()
        i = 0
        while (i < 26) :
            unpluggedCharacters.add(i)
            i += 1
        if (plugboard=="") :
            return unpluggedCharacters
        pairings = plugboard.split("[^a-zA-Z]")
        # Validate and create mapping
        for pair in pairings :
            c1 = ord(pair[0]) - 65
            c2 = ord(pair[1]) - 65
            unpluggedCharacters.remove(c1)
            unpluggedCharacters.remove(c2)
        return unpluggedCharacters
    
    @staticmethod
    def  decodePlugboard( plugboard) :
        if (plugboard == None or plugboard=="") :
            return Plugboard.identityPlugboard()
        pairings = plugboard.split("[^a-zA-Z]")
        pluggedCharacters =  set()
        mapping = Plugboard.identityPlugboard()
        # Validate and create mapping
        for pair in pairings :
            if (len(pair) != 2) :
                return Plugboard.identityPlugboard()
            c1 = ord(pair[0]) - 65
            c2 = ord(pair[1]) - 65
            if (c1 in pluggedCharacters or c2 in pluggedCharacters) :
                return Plugboard.identityPlugboard()
            pluggedCharacters.add(c1)
            pluggedCharacters.add(c2)
            mapping[c1] = c2
            mapping[c2] = c1
        return mapping
