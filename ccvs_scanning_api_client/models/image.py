# Copyright 2019 WHG (International) Limited. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import six


class Image(object):

    swagger_types = {
        'id': 'str',
        'name': 'str'
    }

    def __init__(self, id=None, name=None):
        self._id = None
        self._name = None

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

    @property
    def id(self):
        """
        Gets the id of this Image.

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.

        :param id: The id of this Image.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Image.

        :return: The name of this Image.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Image.

        :param name: The name of this Image.
        :type: str
        """
        if name is None:
            raise ValueError('Invalid value for `name`, must not be `None`')
        if name is not None and len(name) > 255:
            raise ValueError(
                'Invalid value for `name`, length must be less than or '
                'equal to `255`')
        if name is not None and len(name) < 1:
            raise ValueError(
                'Invalid value for `name`, length must be greater than or '
                'equal to `1`')

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, 'to_dict') else x,
                    value
                ))
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], 'to_dict') else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Image, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        """Returns true if both objects are equal."""
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    @property
    def __dict__(self):
        """Returns a custom dict."""

        return self.to_dict()
