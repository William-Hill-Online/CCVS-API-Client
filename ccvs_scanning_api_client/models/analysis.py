"""
CCVS API.

Central Container Vulnerability Scanning  # noqa: E501

OpenAPI spec version: v1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
import re  # noqa: F401

import six


class Analysis(object):
    swagger_types = {
        'id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'image': 'str',
        'vendors': 'object',
        'errors': 'list',
        'result': 'str',
        'ccvs_results': 'object',
        'whitelist': 'object'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'image': 'image',
        'vendors': 'vendors',
        'errors': 'errors',
        'result': 'result',
        'ccvs_results': 'ccvs_results',
        'whitelist': 'whitelist'
    }

    def __init__(self, id=None, status=None, created_at=None, updated_at=None,
                 image=None, vendors=None, errors=None, result=None,
                 ccvs_results=None, whitelist=None):
        """Analysis - a model defined in Swagger"""

        self._id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._image = None
        self._vendors = None
        self._errors = None
        self._result = None
        self._ccvs_results = None
        self._whitelist = None

        if id is not None:
            self.id = id
        self.type = type
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.image = image
        if vendors is not None:
            self.vendors = vendors
        if errors is not None:
            self.errors = errors
        if result is not None:
            self.result = result
        if ccvs_results is not None:
            self.ccvs_results = ccvs_results
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def id(self):
        """
        Gets the id of this Analysis.

        :return: The id of this Analysis.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Analysis.

        :param id: The id of this Analysis.
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """
        Gets the status of this Analysis.

        :return: The status of this Analysis.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Gets the status of this Analysis.

        :return: The status of this Analysis.
        :rtype: str
        """
        allowed_values = ['pending', 'started', 'finished', 'failed']
        if status not in allowed_values:
            raise ValueError(
                'Invalid value for `status` ({0}), must be one of {1}'
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """
        Gets the created_at of this Analysis.

        :return: The created_at of this Analysis.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Gets the created_at of this Analysis.

        :return: The created_at of this Analysis.
        :rtype: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Analysis.

        :return: The updated_at of this Analysis.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Gets the updated_at of this Analysis.

        :return: The updated_at of this Analysis.
        :rtype: str
        """

        self._updated_at = updated_at

    @property
    def image(self):
        """
        Gets the image of this Analysis.

        :return: The image of this Analysis.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Gets the image of this Analysis.

        :return: The image of this Analysis.
        :rtype: str
        """
        if image is None:
            raise ValueError('Invalid value for `image`, must not be `None`')

        self._image = image

    @property
    def vendors(self):
        """
        Gets the vendors of this Analysis.

        :return: The vendors of this Analysis.
        :rtype: object
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """
        Gets the vendors of this Analysis.

        :return: The vendors of this Analysis.
        :rtype: object
        """

        self._vendors = vendors

    @property
    def errors(self):
        """
        Gets the errors of this Analysis.

        :return: The errors of this Analysis.
        :rtype: list
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Gets the errors of this Analysis.

        :return: The errors of this Analysis.
        :rtype: list
        """

        self._errors = errors

    @property
    def result(self):
        """
        Gets the result of this Analysis.

        :return: The result of this Analysis.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Gets the result of this Analysis.

        :return: The result of this Analysis.
        :rtype: str
        """

        self._result = result

    @property
    def ccvs_results(self):
        """
        Gets the ccvs_results of this Analysis.

        :return: The ccvs_results of this Analysis.
        :rtype: object
        """
        return self._ccvs_results

    @ccvs_results.setter
    def ccvs_results(self, ccvs_results):
        """
        Gets the ccvs_results of this Analysis.

        :return: The ccvs_results of this Analysis.
        :rtype: object
        """

        self._ccvs_results = ccvs_results

    @property
    def whitelist(self):
        """
        Gets the whitelist of this Analysis.

        :return: The whitelist of this Analysis.
        :rtype: object
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """
        Gets the whitelist of this Analysis.

        :return: The whitelist of this Analysis.
        :rtype: object
        """

        self._whitelist = whitelist

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
        if issubclass(Analysis, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        """Returns true if both objects are equal."""
        if not isinstance(other, Analysis):
            return False

        return self.__dict__ == other.__dict__

    @property
    def __dict__(self):
        """Returns a custom dict."""

        return self.to_dict()
