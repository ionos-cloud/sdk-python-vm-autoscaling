# coding: utf-8

"""
    VM Auto Scaling API

    The VM Auto Scaling Service enables IONOS clients to horizontally scale the number of VM replicas based on configured rules. You can use Auto Scaling to ensure that you have a sufficient number of replicas to handle your application loads at all times.  For this purpose, create an Auto Scaling group that contains the server replicas. The VM Auto Scaling Service ensures that the number of replicas in the group is always within the defined limits. For example, if the number of target replicas is specified, Auto Scaling maintains the specified number of replicas.   When scaling policies are set, Auto Scaling creates or deletes replicas according to the requirements of your applications. For each policy, specified 'scale-in' and 'scale-out' actions are performed when the corresponding thresholds are reached.  # noqa: E501

    The version of the OpenAPI document: 1-SDK.1
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import six


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None):
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None):
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):

    def __init__(self, status=None, reason=None, http_resp=None, url=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
            self.url = url
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


class ApiTimeout(OpenApiException):
    def __init__(self, message, request_id=None):
        """
        Args:
            msg (str): the exception message
            request_id (str): the request id if any
        """
        self.message = message
        self.request_id = request_id

    def __str__(self):
        return self.message


class ApiFailedRequest(OpenApiException):
    def __init__(self, message, request_id=None):
        """
        Args:
            msg (str): the exception message
            request_id (str): the request id if any
        """
        self.message = message
        self.request_id = request_id

    def __str__(self):
        return self.message


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, six.integer_types):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
