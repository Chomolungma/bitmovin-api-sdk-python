# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Statistics(object):
    @poscheck_model
    def __init__(self,
                 bytes_encoded_total=None,
                 time_encoded_total=None):
        # type: (int, int) -> None

        self._bytes_encoded_total = None
        self._time_encoded_total = None
        self.discriminator = None

        if bytes_encoded_total is not None:
            self.bytes_encoded_total = bytes_encoded_total
        if time_encoded_total is not None:
            self.time_encoded_total = time_encoded_total

    @property
    def openapi_types(self):
        types = {
            'bytes_encoded_total': 'int',
            'time_encoded_total': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'bytes_encoded_total': 'bytesEncodedTotal',
            'time_encoded_total': 'timeEncodedTotal'
        }
        return attributes

    @property
    def bytes_encoded_total(self):
        # type: () -> int
        """Gets the bytes_encoded_total of this Statistics.

        Bytes encoded total. (required)

        :return: The bytes_encoded_total of this Statistics.
        :rtype: int
        """
        return self._bytes_encoded_total

    @bytes_encoded_total.setter
    def bytes_encoded_total(self, bytes_encoded_total):
        # type: (int) -> None
        """Sets the bytes_encoded_total of this Statistics.

        Bytes encoded total. (required)

        :param bytes_encoded_total: The bytes_encoded_total of this Statistics.
        :type: int
        """

        if bytes_encoded_total is not None:
            if not isinstance(bytes_encoded_total, int):
                raise TypeError("Invalid type for `bytes_encoded_total`, type has to be `int`")

        self._bytes_encoded_total = bytes_encoded_total

    @property
    def time_encoded_total(self):
        # type: () -> int
        """Gets the time_encoded_total of this Statistics.

        Time in seconds encoded for all contained daily statistics. (required)

        :return: The time_encoded_total of this Statistics.
        :rtype: int
        """
        return self._time_encoded_total

    @time_encoded_total.setter
    def time_encoded_total(self, time_encoded_total):
        # type: (int) -> None
        """Sets the time_encoded_total of this Statistics.

        Time in seconds encoded for all contained daily statistics. (required)

        :param time_encoded_total: The time_encoded_total of this Statistics.
        :type: int
        """

        if time_encoded_total is not None:
            if not isinstance(time_encoded_total, int):
                raise TypeError("Invalid type for `time_encoded_total`, type has to be `int`")

        self._time_encoded_total = time_encoded_total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Statistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other