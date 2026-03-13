class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit



# TODO: Add your own classes here!

class Building:
    
    def __init__(self):
        self.floor = Floor(self, 1) 

class Floor:
    
    def __init__(self, building: Building, etasje: int):
        self.etasje =  etasje
        self.building = building
        self.room = Room(self) 

class Room: 

    def __init__(self, floor: Floor, roomName = "Inngang", roomArea = 1, device = None):
        self.floor = floor
        self.navn = roomName
        self.areal = roomArea

        if (type is None):
            self.device = []        
        elif(type(device) == list):
            self.device = device
        else:
            self.device = [device]


class Device:

    def __init__(self,id: int, room: Room, produktegenskap: Produktegenskap, huskenavn = None):
        self.id = id
        self.room = room
        self.produktegenskap = produktegenskap
        self.huskenavn = huskenavn
    

class Produktegenskap:

    def __init__(self, supplier: str, model_name : str, enhetstype: str):
        self.supplier = supplier
        self.model_name  = model_name 
        self.enhetstype = enhetstype

class Aktuator(Device):
    
    def __init__(self, tilstand: bool, id: int, room: Room, produktegenskap: Produktegenskap, huskenavn = None ):
        super.__init__(id, room, produktegenskap, huskenavn)
        self.tilstand = tilstand
        
class Sensor(Device):

    def __init__(self, measurement: Measurement, id: int, room: Room, produktegenskap: Produktegenskap, huskenavn = None ):
        super.__init__(id, room, produktegenskap, huskenavn)
        self.measurement = measurement

class KopleksDevice():

    def __init__(self, aktuator = None, sensor = None):
        if sensor is None:
            self.sensorer = []
        elif type(sensor) == list:
            self.sensorer = sensor
        else:
            self.sensorer = [sensor]

        if aktuator is None:
            self.aktuatorer = []
        elif type(aktuator) == list:
            self.aktuatorer = aktuator
        else:
            self.aktuatorer = [aktuator]
        
    def leggTilSensor(self, sensor):
        self.sensorer.append(sensor)

    def leggTilAktuator(self, aktuator):
        self.aktuatorer.append(aktuator)



# class Maaleverdi:

#     def __init__(self, dato, klokkeslett, verdi, enhet):
#         self.dato = dato
#         self.klokkeslett = klokkeslett
#         self.verdi = verdi
#         self.enhet = enhet


class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        pass


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        pass


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        pass


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        pass

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        pass

