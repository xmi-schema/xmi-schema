class XmiBase():

    __slots__ = ('_ID', '_Name', '_IFCGUID', '_Description')

    def __init__(self, id: str = None, name: str = None, ifcguid: str = None, description: str = None):
        self.ID = id  # Calls the setter
        self.Name = name
        self.IFCGUID = ifcguid
        self.Description = description

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("ID should be an str or None")
        self._ID = value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Name should be a str or None")
        self._Name = value

    @property
    def IFCGUID(self):
        return self._IFCGUID

    @IFCGUID.setter
    def IFCGUID(self, value):
        if value is not None and not isinstance(value, (str)):
            raise TypeError("IFCGUID should be a string")
        self._IFCGUID = value

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, value):
        if value is not None and not isinstance(value, (str)):
            raise TypeError("Description should be a string")
        self._Description = value

    def to_dict(self):
        return {slot.lstrip('_'): getattr(self, slot) for slot in self.__slots__}
