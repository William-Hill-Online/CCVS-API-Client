# Copyright 2019 WHG (International) Limited. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import six


class ImageVendor(object):
    """
    Attributes:
      attibute_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    attibute_types = {
        'id': 'str',
        'vendor': 'str',
        'image': 'str',
        'image_vendor_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vendor': 'vendor',
        'image': 'image',
        'image_vendor_id': 'image_vendor_id'
    }

    def __init__(self, id=None, vendor=None, image=None, image_vendor_id=None):

        self._id = None
        self._vendor = None
        self._image = None
        self._image_vendor_id = None

        if id is not None:
            self.id = id
        self.vendor = vendor
        self.image = image
        self.image_vendor_id = image_vendor_id

    @property
    def id(self):
        """
        Gets the id of this ImageVendor.

        :return: The id of this ImageVendor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ImageVendor.

        :param id: The id of this ImageVendor.
        :type: str
        """

        self._id = id

    @property
    def vendor(self):
        """
        Gets the vendor of this ImageVendor.

        :return: The vendor of this ImageVendor.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this ImageVendor.

        :param vendor: The vendor of this ImageVendor.
        :type: str
        """
        if vendor is None:
            raise ValueError('Invalid value for `vendor`, must not be `None`')

        self._vendor = vendor

    @property
    def image(self):
        """
        Gets the image of this ImageVendor.

        :return: The image of this ImageVendor.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this ImageVendor.

        :param image: The image of this ImageVendor.
        :type: str
        """
        if image is None:
            raise ValueError('Invalid value for `image`, must not be `None`')

        self._image = image

    @property
    def image_vendor_id(self):
        """
        Gets the image_vendor_id of this ImageVendor.

        :return: The image_vendor_id of this ImageVendor.
        :rtype: str
        """
        return self._image_vendor_id

    @image_vendor_id.setter
    def image_vendor_id(self, image_vendor_id):
        """
        Sets the image_vendor_id of this ImageVendor.

        :param image_vendor_id: The image_vendor_id of this ImageVendor.
        :type: str
        """
        if image_vendor_id is None:
            raise ValueError(
                'Invalid value for `image_vendor_id`, must not be `None`')
        if image_vendor_id is not None and len(image_vendor_id) > 200:
            raise ValueError(
                'Invalid value for `image_vendor_id`, length must be '
                'less than or equal to `200`')
        if image_vendor_id is not None and len(image_vendor_id) < 1:
            raise ValueError(
                'Invalid value for `image_vendor_id`, length must be '
                'greater than or equal to `1`')

        self._image_vendor_id = image_vendor_id

    def to_dict(self):
        """Returns the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.attibute_types):
            value = getattr(self, attr)
            if hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def __eq__(self, other):
        """Returns true if both objects are equal."""
        if not isinstance(other, ImageVendor):
            return False

        return self.__dict__ == other.__dict__
