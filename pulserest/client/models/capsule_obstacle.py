# coding: utf-8

"""
    Robot API

    Robot REST API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint

import six

from pulserest.client.models.point import Point  # noqa: F401,E501


class CapsuleObstacle(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'obstacle_type': 'str',
        'name': 'str',
        'radius': 'float',
        'start_point': 'Point',
        'end_point': 'Point'
    }

    attribute_map = {
        'obstacle_type': 'obstacleType',
        'name': 'name',
        'radius': 'radius',
        'start_point': 'startPoint',
        'end_point': 'endPoint'
    }

    def __init__(self, obstacle_type=None, name=None, radius=None, start_point=None, end_point=None):  # noqa: E501
        """CapsuleObstacle - a model defined in Swagger"""  # noqa: E501

        self._obstacle_type = None
        self._name = None
        self._radius = None
        self._start_point = None
        self._end_point = None
        self.discriminator = None

        self.obstacle_type = obstacle_type
        self.name = name
        self.radius = radius
        self.start_point = start_point
        self.end_point = end_point

    @property
    def obstacle_type(self):
        """Gets the obstacle_type of this CapsuleObstacle.  # noqa: E501


        :return: The obstacle_type of this CapsuleObstacle.  # noqa: E501
        :rtype: str
        """
        return self._obstacle_type

    @obstacle_type.setter
    def obstacle_type(self, obstacle_type):
        """Sets the obstacle_type of this CapsuleObstacle.


        :param obstacle_type: The obstacle_type of this CapsuleObstacle.  # noqa: E501
        :type: str
        """
        if obstacle_type is None:
            raise ValueError("Invalid value for `obstacle_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CAPSULE"]  # noqa: E501
        if obstacle_type not in allowed_values:
            raise ValueError(
                "Invalid value for `obstacle_type` ({0}), must be one of {1}"  # noqa: E501
                .format(obstacle_type, allowed_values)
            )

        self._obstacle_type = obstacle_type

    @property
    def name(self):
        """Gets the name of this CapsuleObstacle.  # noqa: E501


        :return: The name of this CapsuleObstacle.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CapsuleObstacle.


        :param name: The name of this CapsuleObstacle.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def radius(self):
        """Gets the radius of this CapsuleObstacle.  # noqa: E501

        (in meters)  # noqa: E501

        :return: The radius of this CapsuleObstacle.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this CapsuleObstacle.

        (in meters)  # noqa: E501

        :param radius: The radius of this CapsuleObstacle.  # noqa: E501
        :type: float
        """
        if radius is None:
            raise ValueError("Invalid value for `radius`, must not be `None`")  # noqa: E501

        self._radius = radius

    @property
    def start_point(self):
        """Gets the start_point of this CapsuleObstacle.  # noqa: E501


        :return: The start_point of this CapsuleObstacle.  # noqa: E501
        :rtype: Point
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point):
        """Sets the start_point of this CapsuleObstacle.


        :param start_point: The start_point of this CapsuleObstacle.  # noqa: E501
        :type: Point
        """
        if start_point is None:
            raise ValueError("Invalid value for `start_point`, must not be `None`")  # noqa: E501

        self._start_point = start_point

    @property
    def end_point(self):
        """Gets the end_point of this CapsuleObstacle.  # noqa: E501


        :return: The end_point of this CapsuleObstacle.  # noqa: E501
        :rtype: Point
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this CapsuleObstacle.


        :param end_point: The end_point of this CapsuleObstacle.  # noqa: E501
        :type: Point
        """
        if end_point is None:
            raise ValueError("Invalid value for `end_point`, must not be `None`")  # noqa: E501

        self._end_point = end_point

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CapsuleObstacle, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CapsuleObstacle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
