# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.

    OpenAPI spec version: 1.0.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OracleQueryTxObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'vsn': 'int',
        'query_ttl': 'TTL',
        'response_ttl': 'TTL'
    }

    attribute_map = {
        'type': 'type',
        'vsn': 'vsn',
        'query_ttl': 'query_ttl',
        'response_ttl': 'response_ttl'
    }

    def __init__(self, type=None, vsn=None, query_ttl=None, response_ttl=None):
        """
        OracleQueryTxObject - a model defined in Swagger
        """

        self._type = None
        self._vsn = None
        self._query_ttl = None
        self._response_ttl = None

        self.type = type
        if vsn is not None:
          self.vsn = vsn
        self.query_ttl = query_ttl
        self.response_ttl = response_ttl

    @property
    def type(self):
        """
        Gets the type of this OracleQueryTxObject.

        :return: The type of this OracleQueryTxObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this OracleQueryTxObject.

        :param type: The type of this OracleQueryTxObject.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def vsn(self):
        """
        Gets the vsn of this OracleQueryTxObject.

        :return: The vsn of this OracleQueryTxObject.
        :rtype: int
        """
        return self._vsn

    @vsn.setter
    def vsn(self, vsn):
        """
        Sets the vsn of this OracleQueryTxObject.

        :param vsn: The vsn of this OracleQueryTxObject.
        :type: int
        """

        self._vsn = vsn

    @property
    def query_ttl(self):
        """
        Gets the query_ttl of this OracleQueryTxObject.

        :return: The query_ttl of this OracleQueryTxObject.
        :rtype: TTL
        """
        return self._query_ttl

    @query_ttl.setter
    def query_ttl(self, query_ttl):
        """
        Sets the query_ttl of this OracleQueryTxObject.

        :param query_ttl: The query_ttl of this OracleQueryTxObject.
        :type: TTL
        """
        if query_ttl is None:
            raise ValueError("Invalid value for `query_ttl`, must not be `None`")

        self._query_ttl = query_ttl

    @property
    def response_ttl(self):
        """
        Gets the response_ttl of this OracleQueryTxObject.

        :return: The response_ttl of this OracleQueryTxObject.
        :rtype: TTL
        """
        return self._response_ttl

    @response_ttl.setter
    def response_ttl(self, response_ttl):
        """
        Sets the response_ttl of this OracleQueryTxObject.

        :param response_ttl: The response_ttl of this OracleQueryTxObject.
        :type: TTL
        """
        if response_ttl is None:
            raise ValueError("Invalid value for `response_ttl`, must not be `None`")

        self._response_ttl = response_ttl

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, OracleQueryTxObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
