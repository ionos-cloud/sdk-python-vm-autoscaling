# coding: utf-8

# flake8: noqa

"""
    VM Auto Scaling API

    The VM Auto Scaling Service enables IONOS clients to horizontally scale the number of VM replicas based on configured rules. You can use VM Auto Scaling to ensure that you have a sufficient number of replicas to handle your application loads at all times.  For this purpose, create a VM Auto Scaling Group that contains the server replicas. The VM Auto Scaling Service ensures that the number of replicas in the group is always within the defined limits.   When scaling policies are set, VM Auto Scaling creates or deletes replicas according to the requirements of your applications. For each policy, specified 'scale-in' and 'scale-out' actions are performed when the corresponding thresholds are reached.  # noqa: E501

    The version of the OpenAPI document: 1-SDK.1
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import apis into sdk package
from ionoscloud_vm_autoscaling.api.auto_scaling_groups_api import AutoScalingGroupsApi

# import ApiClient
from ionoscloud_vm_autoscaling.api_response import ApiResponse
from ionoscloud_vm_autoscaling.api_client import ApiClient
from ionoscloud_vm_autoscaling.configuration import Configuration
from ionoscloud_vm_autoscaling.exceptions import OpenApiException
from ionoscloud_vm_autoscaling.exceptions import ApiTypeError
from ionoscloud_vm_autoscaling.exceptions import ApiValueError
from ionoscloud_vm_autoscaling.exceptions import ApiKeyError
from ionoscloud_vm_autoscaling.exceptions import ApiAttributeError
from ionoscloud_vm_autoscaling.exceptions import ApiException

# import models into sdk package
from ionoscloud_vm_autoscaling.models.action import Action
from ionoscloud_vm_autoscaling.models.action_amount import ActionAmount
from ionoscloud_vm_autoscaling.models.action_collection import ActionCollection
from ionoscloud_vm_autoscaling.models.action_properties import ActionProperties
from ionoscloud_vm_autoscaling.models.action_resource import ActionResource
from ionoscloud_vm_autoscaling.models.action_status import ActionStatus
from ionoscloud_vm_autoscaling.models.action_type import ActionType
from ionoscloud_vm_autoscaling.models.actions_link_resource import ActionsLinkResource
from ionoscloud_vm_autoscaling.models.availability_zone import AvailabilityZone
from ionoscloud_vm_autoscaling.models.bus_type import BusType
from ionoscloud_vm_autoscaling.models.cpu_family import CpuFamily
from ionoscloud_vm_autoscaling.models.datacenter_server import DatacenterServer
from ionoscloud_vm_autoscaling.models.error401 import Error401
from ionoscloud_vm_autoscaling.models.error401_message import Error401Message
from ionoscloud_vm_autoscaling.models.error404 import Error404
from ionoscloud_vm_autoscaling.models.error404_message import Error404Message
from ionoscloud_vm_autoscaling.models.error_authorize import ErrorAuthorize
from ionoscloud_vm_autoscaling.models.error_authorize_message import ErrorAuthorizeMessage
from ionoscloud_vm_autoscaling.models.error_group_validate import ErrorGroupValidate
from ionoscloud_vm_autoscaling.models.error_group_validate_message import ErrorGroupValidateMessage
from ionoscloud_vm_autoscaling.models.error_message import ErrorMessage
from ionoscloud_vm_autoscaling.models.error_message_parse import ErrorMessageParse
from ionoscloud_vm_autoscaling.models.group import Group
from ionoscloud_vm_autoscaling.models.group_collection import GroupCollection
from ionoscloud_vm_autoscaling.models.group_policy import GroupPolicy
from ionoscloud_vm_autoscaling.models.group_policy_scale_in_action import GroupPolicyScaleInAction
from ionoscloud_vm_autoscaling.models.group_policy_scale_out_action import GroupPolicyScaleOutAction
from ionoscloud_vm_autoscaling.models.group_post import GroupPost
from ionoscloud_vm_autoscaling.models.group_post_entities import GroupPostEntities
from ionoscloud_vm_autoscaling.models.group_post_response import GroupPostResponse
from ionoscloud_vm_autoscaling.models.group_properties import GroupProperties
from ionoscloud_vm_autoscaling.models.group_properties_datacenter import GroupPropertiesDatacenter
from ionoscloud_vm_autoscaling.models.group_put import GroupPut
from ionoscloud_vm_autoscaling.models.group_put_properties import GroupPutProperties
from ionoscloud_vm_autoscaling.models.group_put_properties_datacenter import GroupPutPropertiesDatacenter
from ionoscloud_vm_autoscaling.models.group_resource import GroupResource
from ionoscloud_vm_autoscaling.models.metadata import Metadata
from ionoscloud_vm_autoscaling.models.metadata_basic import MetadataBasic
from ionoscloud_vm_autoscaling.models.metadata_state import MetadataState
from ionoscloud_vm_autoscaling.models.metric import Metric
from ionoscloud_vm_autoscaling.models.nic_firewall_rule import NicFirewallRule
from ionoscloud_vm_autoscaling.models.nic_flow_log import NicFlowLog
from ionoscloud_vm_autoscaling.models.parse_error import ParseError
from ionoscloud_vm_autoscaling.models.query_unit import QueryUnit
from ionoscloud_vm_autoscaling.models.replica_nic import ReplicaNic
from ionoscloud_vm_autoscaling.models.replica_properties_post import ReplicaPropertiesPost
from ionoscloud_vm_autoscaling.models.replica_volume_post import ReplicaVolumePost
from ionoscloud_vm_autoscaling.models.server import Server
from ionoscloud_vm_autoscaling.models.server_collection import ServerCollection
from ionoscloud_vm_autoscaling.models.server_properties import ServerProperties
from ionoscloud_vm_autoscaling.models.server_resource import ServerResource
from ionoscloud_vm_autoscaling.models.servers_link_resource import ServersLinkResource
from ionoscloud_vm_autoscaling.models.target_group import TargetGroup
from ionoscloud_vm_autoscaling.models.termination_policy_type import TerminationPolicyType
from ionoscloud_vm_autoscaling.models.volume_hw_type import VolumeHwType
