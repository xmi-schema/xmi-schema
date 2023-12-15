# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

import uuid


class XmiBaseEntity():

    __slots__ = ('_id',
                 '_name',
                 '_ifcguid',
                 '_description',
                 '_entity_type')

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 ifcguid: str = None,
                 description: str = None,
                 entity_type: str = "XmiBaseEntity",
                 ** kwargs):

        id = id if id else kwargs.get('id', str(uuid.uuid4()))
        name = name if name else kwargs.get('name', id)
        description = description if description else kwargs.get(
            'description', None)
        ifcguid = ifcguid if ifcguid else kwargs.get('ifcguid', None)

        self.id = id  # Calls the setter
        self.name = name
        self.ifcguid = ifcguid
        self.description = description
        self.entity_type = entity_type

    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        # if value is not isinstance(value, str):
        #     raise TypeError("'entity_type' should be an str")
        self._entity_type = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("ID should be an str or None")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Name should be a str or None")
        self._name = value

    @property
    def ifcguid(self):
        return self._ifcguid

    @ifcguid.setter
    def ifcguid(self, value):
        if value is not None and not isinstance(value, (str)):
            raise TypeError("IFCGUID should be a string")
        self._ifcguid = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Description should be a string")
        self._description = value

    def to_dict(self):
        return {slot.lstrip('_'): getattr(self, slot) for slot in self.__slots__}


class XmiBaseRelationship():
    __slots__ = ('_source', '_target', '_name', '_entity_type')

    def __init__(self,
                 source: XmiBaseEntity,
                 target: XmiBaseEntity,
                 name: str,
                 entity_type: str = "XmiRelBaseRelationship"
                 ) -> XmiBaseRelationship:
        """_summary_

        Parameters
        ----------
        source : XmiBaseEntity
            _description_
        target : XmiBaseEntity
            _description_
        name : str, optional
            _description_, by default None

        Returns
        -------
        XmiBaseRelationship
            _description_
        """

        if not isinstance(source, XmiBaseEntity):
            raise TypeError("'source' should be of type XmiBaseEntity")

        if not isinstance(target, XmiBaseEntity):
            raise TypeError("'target' should be of type XmiBaseEntity")

        if name is None:
            raise ValueError("'name' value should not be None")

        self.source = source
        self.target = target
        self.name = name
        self.entity_type = entity_type

    # Getter and setter for source
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        if not isinstance(value, str):
            raise ValueError("'entity_type' must be of type str")
        self._entity_type = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        if isinstance(source, XmiBaseEntity):
            self._source = source
        else:
            raise ValueError("Source must be of type XmiBaseEntity")

    # Getter and setter for target
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target):
        if isinstance(target, XmiBaseEntity):
            self._target = target
        else:
            raise ValueError("Target must be of type XmiBaseEntity")

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
