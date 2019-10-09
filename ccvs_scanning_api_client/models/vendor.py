class Vendor(object):

    def __init__(self, id=None, name=None, credentials=None):

        self._id = None
        self._name = None

        self._credentials = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.credentials = credentials

    @property
    def id(self):
        """
        Gets the id of this Vendor.

        :return: The id of this Vendor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vendor.

        :param id: The id of this Vendor.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Vendor.

        :return: The name of this Vendor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Vendor.

        :param name: The name of this Vendor.
        :type: str
        """
        if name is None:
            raise ValueError('Invalid value for `name`, must not be `None`')
        if name is not None and len(name) > 100:
            raise ValueError(
                'Invalid value for `name`, length must be less than or '
                'equal to `100`')
        if name is not None and len(name) < 1:
            raise ValueError(
                'Invalid value for `name`, length must be greater than or '
                'equal to `1`')

        self._name = name

    @property
    def credentials(self):
        """
        Gets the credentials of this Vendor.

        :return: The credentials of this Vendor.
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this Vendor.

        :param credentials: The credentials of this Vendor.
        :type: str
        """
        if credentials is None:
            raise ValueError(
                'Invalid value for `credentials`, must not be `None`')

        self._credentials = credentials

    def __eq__(self, other):
        """Returns true if both objects are equal."""
        if not isinstance(other, Vendor):
            return False

        return self.__dict__ == other.__dict__
