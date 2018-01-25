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


class SignedTxObject(object):
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
        'tx': 'GenericTxObject',
        'signatures': 'list[str]'
    }

    attribute_map = {
        'tx': 'tx',
        'signatures': 'signatures'
    }

    def __init__(self, tx=None, signatures=None):
        """
        SignedTxObject - a model defined in Swagger
        """

        self._tx = None
        self._signatures = None

        if tx is not None:
          self.tx = tx
        if signatures is not None:
          self.signatures = signatures

    @property
    def tx(self):
        """
        Gets the tx of this SignedTxObject.

        :return: The tx of this SignedTxObject.
        :rtype: GenericTxObject
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """
        Sets the tx of this SignedTxObject.

        :param tx: The tx of this SignedTxObject.
        :type: GenericTxObject
        """

        self._tx = tx

    @property
    def signatures(self):
        """
        Gets the signatures of this SignedTxObject.

        :return: The signatures of this SignedTxObject.
        :rtype: list[str]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """
        Sets the signatures of this SignedTxObject.

        :param signatures: The signatures of this SignedTxObject.
        :type: list[str]
        """

        self._signatures = signatures

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
        if not isinstance(other, SignedTxObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
