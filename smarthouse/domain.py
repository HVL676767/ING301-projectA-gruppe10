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
        self.floor = []
        self.floor.append(Floor(self, 1))
    
    def addFloor(self, floor: Floor):
        self.floor.append(floor)

    def removeFloor(self, floor: Floor):
        if floor in self.floor:
            self.floor.remove(floor)


class Floor:
    
    def __init__(self, building: Building, etasje: int):
        self.etasje =  etasje
        self.building = building
        for f in building.floor:
            if f == etasje:
                self.building.removeFloor(f)
        self.room = []
        self.room.append(Room(self))
        self.building.addFloor(etasje)


    def addRoom(self, room: Room):
        self.room.append(room)

    def removeRoom(self, room: Room):
        if room in self.room:
            self.room.remove(room)

    def totalAreal(self):
        areal = 0
        for room in self.room:
            areal = areal + room.areal
        return areal

class Room: 

    def __init__(self, floor: Floor, roomName = None, roomAreal = 0, device = None):
        self.floor = floor
        self.navn = roomName
        self.areal = roomAreal

        if (type is None):
            self.device = []        
        elif(type(device) == list):
            self.device = device
        else:
            self.device = [device]

        self.floor.addRoom(self)


    def changeRoomSize(self, newSize):
        self.areal = newSize

    def addDevice(self, device : Device):
        self.device.append(device)

    def removeDevice(self, device : Device):
        if device in self.device:
            self.device.remove(device)
        


class Device:

    def __init__(self,id: str, produktegenskap: Produktegenskap, huskenavn = None):
        self.id = id
        # self.room = room
        self.produktegenskap = produktegenskap
        self.huskenavn = huskenavn
        # self.room.addDevice(self)


    def regRoom(self, room):
        self.room = room
        self.room.addDevice(self)

    def changeRoom(self, newRoom : Room):
        self.room.removeDevice(self)
        self.room = newRoom
        self.room.addDevice(self)   

    def is_actuator(self):
        return False

    def is_sensor(self):
        return False

    def get_device_type(self):
        return self.produktegenskap.enhetstype
    

class Produktegenskap:

    def __init__(self, supplier: str, model_name : str, enhetstype: str):
        self.supplier = supplier
        self.model_name  = model_name 
        self.enhetstype = enhetstype

class Aktuator(Device):
    
    def __init__(self, id: int, produktegenskap: Produktegenskap, state = False, huskenavn = None, targetValue = None):
        super().__init__(id, produktegenskap, huskenavn)
        self.state = state
        self.targetValue = targetValue

    def is_actuator(self):
        return True
    def turn_on(self):
        self.state = True
    def turn_off(self):
        self.state = False
    def is_active(self):
        return self.state    
    
        
class Sensor(Device):

    def __init__(self,  id: int,  produktegenskap: Produktegenskap, huskenavn = None, measurement = 0):
        super().__init__(id, produktegenskap, huskenavn)
        self.measurements = [measurement]

    def is_sensor(self):
        return True
    
    def addMeasurment(self, measurment: Measurement):
        self.measurements.append(measurment)
    
    def last_measurement(self):
        return self.measurements[len(self.measurements)-1]
    
    def all_measurments(self):
        return self.measurements

class KopleksDevice(Device):

    def listTilTupleList(verdi):
        if verdi is None:
            liste = []
        elif type(verdi) == list:
            liste = []
            for enVerdi in verdi:
                if type(enVerdi) == tuple:
                    liste.append(enVerdi)
                else:
                    liste.append(('',enVerdi))
        elif type(verdi) == tuple:
            liste = [verdi]
        else:
            liste = [('', verdi)]
        return liste

    def __init__(self, id:int, room:Room, produktegenskap:Produktegenskap, huskenavn=None, measurment=None, state=None, targetValue = None):
        super().__init__(id, room, produktegenskap, huskenavn)
        self.measurements = self.listTilTupleList(measurment)
        self.states = self.listTilTupleList(state)
        self.targetValue = self.listTilTupleList(targetValue)
    
    def addMeasurement(self, measurement : Measurement, sensorType : str):
        self.measurements.append((sensorType,measurement))

    def addState(self, state, stateType: str):
        self.states.append((stateType, state))

    def addTargetValue(self, targetValue, valueType:str):
        self.targetValue.append((valueType, targetValue))

    def is_sensor(self):
        return bool(self.measurements)
    
    def is_actuator(self):
        return bool(self.states)
    
    def turn_on(self):
        self.state = True
    def turn_off(self):
        self.state = False
    def is_active(self):
        b = True
        for s in self.states:
            b = b and s[1] # Vurderte å implimentere å sjekke om targetValie er 0, men konkluderte att target kan være 0 uten att aktuator er av, eks temperatur til noe som kjøler 
        return b


class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """
    def __init__(self):
        self.buildig = Building()
        self.floors = []
        self.rooms = []
        self.devices = []

    

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        floor = Floor(self.buildig, level)
        self.floors.append(floor)
        return floor

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        room = Room(floor, room_name, room_size)
        self.rooms.append(room)
        return room


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        return self.buildig.floor.sort()


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        allRoom = []

        for floors in self.floors:
            allRoom = allRoom + floors.room

        return allRoom


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """
        areal = 0

        for floor in self.floors:
            areal = areal + floor.totalAreal

        return areal


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        device.regRoom(room)

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        
        returnDevice = None

        for device in self.devices:
            if device.id == device_id:
                returnDevice = device
        
        return returnDevice

