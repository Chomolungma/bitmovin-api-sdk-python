# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.google_cloud_region import GoogleCloudRegion
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class GcsOutput(Output):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 acl=None,
                 access_key=None,
                 secret_key=None,
                 bucket_name=None,
                 cloud_region=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[AclEntry], string_types, string_types, string_types, GoogleCloudRegion) -> None
        super(GcsOutput, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, acl=acl)

        self._access_key = None
        self._secret_key = None
        self._bucket_name = None
        self._cloud_region = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if cloud_region is not None:
            self.cloud_region = cloud_region

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(GcsOutput, self), 'openapi_types'):
            types = getattr(super(GcsOutput, self), 'openapi_types')

        types.update({
            'access_key': 'string_types',
            'secret_key': 'string_types',
            'bucket_name': 'string_types',
            'cloud_region': 'GoogleCloudRegion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(GcsOutput, self), 'attribute_map'):
            attributes = getattr(super(GcsOutput, self), 'attribute_map')

        attributes.update({
            'access_key': 'accessKey',
            'secret_key': 'secretKey',
            'bucket_name': 'bucketName',
            'cloud_region': 'cloudRegion'
        })
        return attributes

    @property
    def access_key(self):
        # type: () -> string_types
        """Gets the access_key of this GcsOutput.

        GCS access key (required)

        :return: The access_key of this GcsOutput.
        :rtype: string_types
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        # type: (string_types) -> None
        """Sets the access_key of this GcsOutput.

        GCS access key (required)

        :param access_key: The access_key of this GcsOutput.
        :type: string_types
        """

        if access_key is not None:
            if not isinstance(access_key, string_types):
                raise TypeError("Invalid type for `access_key`, type has to be `string_types`")

        self._access_key = access_key

    @property
    def secret_key(self):
        # type: () -> string_types
        """Gets the secret_key of this GcsOutput.

        GCS secret key (required)

        :return: The secret_key of this GcsOutput.
        :rtype: string_types
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        # type: (string_types) -> None
        """Sets the secret_key of this GcsOutput.

        GCS secret key (required)

        :param secret_key: The secret_key of this GcsOutput.
        :type: string_types
        """

        if secret_key is not None:
            if not isinstance(secret_key, string_types):
                raise TypeError("Invalid type for `secret_key`, type has to be `string_types`")

        self._secret_key = secret_key

    @property
    def bucket_name(self):
        # type: () -> string_types
        """Gets the bucket_name of this GcsOutput.

        Name of the bucket (required)

        :return: The bucket_name of this GcsOutput.
        :rtype: string_types
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        # type: (string_types) -> None
        """Sets the bucket_name of this GcsOutput.

        Name of the bucket (required)

        :param bucket_name: The bucket_name of this GcsOutput.
        :type: string_types
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, string_types):
                raise TypeError("Invalid type for `bucket_name`, type has to be `string_types`")

        self._bucket_name = bucket_name

    @property
    def cloud_region(self):
        # type: () -> GoogleCloudRegion
        """Gets the cloud_region of this GcsOutput.


        :return: The cloud_region of this GcsOutput.
        :rtype: GoogleCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (GoogleCloudRegion) -> None
        """Sets the cloud_region of this GcsOutput.


        :param cloud_region: The cloud_region of this GcsOutput.
        :type: GoogleCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, GoogleCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `GoogleCloudRegion`")

        self._cloud_region = cloud_region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(GcsOutput, self), "to_dict"):
            result = super(GcsOutput, self).to_dict()
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
        if not isinstance(other, GcsOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other