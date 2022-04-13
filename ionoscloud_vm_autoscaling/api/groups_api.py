from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_vm_autoscaling.api_client import ApiClient
from ionoscloud_vm_autoscaling.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GroupsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def autoscaling_groups_actions_find_by_id(self, action_id, group_id, **kwargs):  # noqa: E501
        """Retrieve action details  # noqa: E501

        Retrieve the details, such as metadata, properties, and the current status, for the specified action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_actions_find_by_id(action_id, group_id, async_req=True)
        >>> result = thread.get()

        :param action_id: (required)
        :type action_id: str
        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Action
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_actions_find_by_id_with_http_info(action_id, group_id, **kwargs)  # noqa: E501

    def autoscaling_groups_actions_find_by_id_with_http_info(self, action_id, group_id, **kwargs):  # noqa: E501
        """Retrieve action details  # noqa: E501

        Retrieve the details, such as metadata, properties, and the current status, for the specified action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_actions_find_by_id_with_http_info(action_id, group_id, async_req=True)
        >>> result = thread.get()

        :param action_id: (required)
        :type action_id: str
        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Action, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'action_id',
            'group_id',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_actions_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'action_id' is set
        if self.api_client.client_side_validation and ('action_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['action_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `action_id` when calling `autoscaling_groups_actions_find_by_id`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `autoscaling_groups_actions_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['actionId'] = local_var_params['action_id']  # noqa: E501
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Action'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups/{groupId}/actions/{actionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_actions_get(self, group_id, **kwargs):  # noqa: E501
        """Retrieve last ten actions  # noqa: E501

        Retrieve the scaling actions for the specified autoscaling group; presently, only the last ten actions are returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_actions_get(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param order_by: Define the property to be used for ordering the returned list; valid values are 'createdDate' and 'lastModifiedDate'.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ActionCollection
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_actions_get_with_http_info(group_id, **kwargs)  # noqa: E501

    def autoscaling_groups_actions_get_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Retrieve last ten actions  # noqa: E501

        Retrieve the scaling actions for the specified autoscaling group; presently, only the last ten actions are returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_actions_get_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param order_by: Define the property to be used for ordering the returned list; valid values are 'createdDate' and 'lastModifiedDate'.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ActionCollection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'depth',
            'order_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_actions_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `autoscaling_groups_actions_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ActionCollection'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups/{groupId}/actions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_delete(self, group_id, **kwargs):  # noqa: E501
        """Delete autoscaling groups.  # noqa: E501

        Delete the specified autoscaling group; deletion of the associated servers and volumes is presently not implemented.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_delete(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_delete_with_http_info(group_id, **kwargs)  # noqa: E501

    def autoscaling_groups_delete_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Delete autoscaling groups.  # noqa: E501

        Delete the specified autoscaling group; deletion of the associated servers and volumes is presently not implemented.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_delete_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `autoscaling_groups_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups/{groupId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_find_by_id(self, group_id, **kwargs):  # noqa: E501
        """Retrieve autoscaling groups by UUID  # noqa: E501

        Retrieve the details for the autoscaling group with the specified UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_find_by_id(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Group
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_find_by_id_with_http_info(group_id, **kwargs)  # noqa: E501

    def autoscaling_groups_find_by_id_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Retrieve autoscaling groups by UUID  # noqa: E501

        Retrieve the details for the autoscaling group with the specified UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_find_by_id_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Group, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `autoscaling_groups_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Group'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups/{groupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_get(self, **kwargs):  # noqa: E501
        """List autoscaling groups  # noqa: E501

        List all autoscaling groups for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_get(async_req=True)
        >>> result = thread.get()

        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param order_by: Define the property to be used for ordering the returned list; valid values are 'createdDate' and 'lastModifiedDate'.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupCollection
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_get_with_http_info(**kwargs)  # noqa: E501

    def autoscaling_groups_get_with_http_info(self, **kwargs):  # noqa: E501
        """List autoscaling groups  # noqa: E501

        List all autoscaling groups for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param order_by: Define the property to be used for ordering the returned list; valid values are 'createdDate' and 'lastModifiedDate'.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupCollection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'depth',
            'order_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'GroupCollection'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_post(self, group, **kwargs):  # noqa: E501
        """Create autoscaling groups  # noqa: E501

        Create autoscaling groups with this POST method. Creation of a group will trigger the creation of two monitoring alarms, for ‘Scale In’ and ‘Scale Out’ operations, according to \"policy\" settings.   \"properties.name\" must not be null or blank.   \"properties.targetReplicaCount\" is optional attribute which must be >= minReplicaCount and <= maxReplicaCount if provided in the request body.   \"properties.minReplicaCount\" must be >= 0 and <= 200.   \"properties.maxReplicaCount\" must be >= 0 and <= 200.   \"properties.datacenter.id\" must be a valid data center ID.   \"properties.policy.metric\" must be one of: INSTANCE_CPU_UTILIZATION_AVERAGE, INSTANCE_NETWORK_IN_BYTES, INSTANCE_NETWORK_OUT_BYTES, INSTANCE_NETWORK_IN_PACKETS, INSTANCE_NETWORK_OUT_PACKETS.   \"properties.policy.unit\" must be one of:  PER_SECOND, PER_MINUTE, PER_HOUR, TOTAL.  TOTAL can be combined only with INSTANCE_CPU_UTILIZATION_AVERAGE.   \"properties.policy.range\" must be >= 2 minutes.   If \"properties.policy.unit\" is \"TOTAL\", then \"properties.policy.scaleOutThreshold - properties.policy.scaleInThreshold\" must be >= 40.    \"properties.policy.scaleInAction.amount\" (the same is true for \"properties.policy.scaleOutAction.amount\") must be:   in case of properties.policy.scaleInAction.amountType = ABSOLUTE: 1 <= properties.policy.scaleInAction.amount <= 10  in case of properties.policy.scaleInAction.amountType = PERCENTAGE: 1 <= properties.policy.scaleInAction.amount <= 200   \"properties.policy.scaleInAction.cooldownPeriod\" (the same is true for \"properties.policy.scaleOutAction.cooldownPeriod\") must be: >= 2 minutes and <= 24 hours with a default value of 5 minutes if not provided in the request payload or given with null, empty string or spaces.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_post(group, async_req=True)
        >>> result = thread.get()

        :param group: (required)
        :type group: Group
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupPostResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_post_with_http_info(group, **kwargs)  # noqa: E501

    def autoscaling_groups_post_with_http_info(self, group, **kwargs):  # noqa: E501
        """Create autoscaling groups  # noqa: E501

        Create autoscaling groups with this POST method. Creation of a group will trigger the creation of two monitoring alarms, for ‘Scale In’ and ‘Scale Out’ operations, according to \"policy\" settings.   \"properties.name\" must not be null or blank.   \"properties.targetReplicaCount\" is optional attribute which must be >= minReplicaCount and <= maxReplicaCount if provided in the request body.   \"properties.minReplicaCount\" must be >= 0 and <= 200.   \"properties.maxReplicaCount\" must be >= 0 and <= 200.   \"properties.datacenter.id\" must be a valid data center ID.   \"properties.policy.metric\" must be one of: INSTANCE_CPU_UTILIZATION_AVERAGE, INSTANCE_NETWORK_IN_BYTES, INSTANCE_NETWORK_OUT_BYTES, INSTANCE_NETWORK_IN_PACKETS, INSTANCE_NETWORK_OUT_PACKETS.   \"properties.policy.unit\" must be one of:  PER_SECOND, PER_MINUTE, PER_HOUR, TOTAL.  TOTAL can be combined only with INSTANCE_CPU_UTILIZATION_AVERAGE.   \"properties.policy.range\" must be >= 2 minutes.   If \"properties.policy.unit\" is \"TOTAL\", then \"properties.policy.scaleOutThreshold - properties.policy.scaleInThreshold\" must be >= 40.    \"properties.policy.scaleInAction.amount\" (the same is true for \"properties.policy.scaleOutAction.amount\") must be:   in case of properties.policy.scaleInAction.amountType = ABSOLUTE: 1 <= properties.policy.scaleInAction.amount <= 10  in case of properties.policy.scaleInAction.amountType = PERCENTAGE: 1 <= properties.policy.scaleInAction.amount <= 200   \"properties.policy.scaleInAction.cooldownPeriod\" (the same is true for \"properties.policy.scaleOutAction.cooldownPeriod\") must be: >= 2 minutes and <= 24 hours with a default value of 5 minutes if not provided in the request payload or given with null, empty string or spaces.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_post_with_http_info(group, async_req=True)
        >>> result = thread.get()

        :param group: (required)
        :type group: Group
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupPostResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group' is set
        if self.api_client.client_side_validation and ('group' not in local_var_params or  # noqa: E501
                                                        local_var_params['group'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group` when calling `autoscaling_groups_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group' in local_var_params:
            body_params = local_var_params['group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'GroupPostResponse'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_put(self, group_id, group_update, **kwargs):  # noqa: E501
        """Update autoscaling groups  # noqa: E501

        Update the specified autoscaling group. \"properties.datacenter.id\" is immutable after creation and cannot be updated.  The other validations are the same as when creating a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_put(group_id, group_update, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param group_update: (required)
        :type group_update: GroupUpdate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Group
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_put_with_http_info(group_id, group_update, **kwargs)  # noqa: E501

    def autoscaling_groups_put_with_http_info(self, group_id, group_update, **kwargs):  # noqa: E501
        """Update autoscaling groups  # noqa: E501

        Update the specified autoscaling group. \"properties.datacenter.id\" is immutable after creation and cannot be updated.  The other validations are the same as when creating a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_put_with_http_info(group_id, group_update, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param group_update: (required)
        :type group_update: GroupUpdate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Group, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'group_update'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `autoscaling_groups_put`")  # noqa: E501
        # verify the required parameter 'group_update' is set
        if self.api_client.client_side_validation and ('group_update' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_update'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_update` when calling `autoscaling_groups_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_update' in local_var_params:
            body_params = local_var_params['group_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Group'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups/{groupId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_servers_find_by_id(self, group_id, server_id, **kwargs):  # noqa: E501
        """Retrieve group servers by UUID  # noqa: E501

        Retrieve the properties of the specificed server in autoscaling group.  Please note that the autoscaling group server IDs are distinct from, and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_servers_find_by_id(group_id, server_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param server_id: (required)
        :type server_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Server
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_servers_find_by_id_with_http_info(group_id, server_id, **kwargs)  # noqa: E501

    def autoscaling_groups_servers_find_by_id_with_http_info(self, group_id, server_id, **kwargs):  # noqa: E501
        """Retrieve group servers by UUID  # noqa: E501

        Retrieve the properties of the specificed server in autoscaling group.  Please note that the autoscaling group server IDs are distinct from, and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_servers_find_by_id_with_http_info(group_id, server_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param server_id: (required)
        :type server_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Server, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'server_id',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_servers_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `autoscaling_groups_servers_find_by_id`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `autoscaling_groups_servers_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Server'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups/{groupId}/servers/{serverId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def autoscaling_groups_servers_get(self, group_id, **kwargs):  # noqa: E501
        """Retrieve autoscaling group servers  # noqa: E501

        Retrieve all servers, associated with the specified autoscaling group.  Please note that the autoscaling group server IDs are distinct from, and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_servers_get(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param order_by: Define the property to be used for ordering the returned list; valid values are 'createdDate' and 'lastModifiedDate'.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ServerCollection
        """
        kwargs['_return_http_data_only'] = True
        return self.autoscaling_groups_servers_get_with_http_info(group_id, **kwargs)  # noqa: E501

    def autoscaling_groups_servers_get_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Retrieve autoscaling group servers  # noqa: E501

        Retrieve all servers, associated with the specified autoscaling group.  Please note that the autoscaling group server IDs are distinct from, and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.autoscaling_groups_servers_get_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: Controls the detail depth of the response objects.    - depth=0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth=1: Direct properties and children references are included.    - depth=2: Direct properties and children properties are included.    - depth=3: Direct properties and children properties and children's children are included.    - depth=... and so on  
        :type depth: float
        :param order_by: Define the property to be used for ordering the returned list; valid values are 'createdDate' and 'lastModifiedDate'.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ServerCollection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'depth',
            'order_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autoscaling_groups_servers_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `autoscaling_groups_servers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ServerCollection'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/cloudapi/autoscaling/groups/{groupId}/servers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
