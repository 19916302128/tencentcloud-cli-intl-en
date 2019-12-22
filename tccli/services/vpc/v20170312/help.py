# -*- coding: utf-8 -*-
DESC = "vpc-2017-03-12"
INFO = {
  "ReplaceSecurityGroupPolicy": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "Security group policy set object."
      }
    ],
    "desc": "This API (ReplaceSecurityGroupPolicy) is used to replace a single security group policy (SecurityGroupPolicy).\nOnly one policy in a single direction can be replaced in each request, and the PolicyIndex parameter must be specified."
  },
  "ModifyNatGatewayAttribute": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "NatGatewayName",
        "desc": "The NAT gateway name, such as `test_nat`."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The maximum outbound bandwidth of the NAT gateway. Unit: Mbps."
      }
    ],
    "desc": "This API (ModifyNatGatewayAttribute) is used to modify the attributes of a NAT gateway."
  },
  "DescribeTaskResult": {
    "params": [
      {
        "name": "TaskId",
        "desc": "The async job ID"
      },
      {
        "name": "DealName",
        "desc": "The billing order ID"
      }
    ],
    "desc": "This API is used to query the EIP async job execution results."
  },
  "DescribeServiceTemplateGroups": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>service-template-group-name - String - (Filter condition) Protocol port template group name.</li>\n<li>service-template-group-id - String - (Filter condition) Protocol port template group instance ID, such as `ppmg-e6dy460g`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeServiceTemplateGroups) is used to query a protocol port template group."
  },
  "CreateRouteTable": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "RouteTableName",
        "desc": "The route table name. The maximum length is 60 characters."
      }
    ],
    "desc": "This API (CreateRouteTable) is used to create a route table.\n* After the VPC has been created, the system will create a default route table with which all newly created subnets will be associated. By default, you can use this route table to manage your routing policies. If you have multiple routing policies, you can call the API for creating route table to create more route tables to manage your routing policies."
  },
  "AssignIpv6CidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      }
    ],
    "desc": "This API is used to assign IPv6 ranges.\n* To use this API, you must already have a VPC instance. If you do not have a VPC instance yet, use the <a href=\"https://cloud.tencent.com/document/api/215/15774\" title=\"CreateVpc\" target=\"_blank\">CreateVpc</a> API to create one.\n* Each VPC can apply for only one IPv6 range."
  },
  "DescribeNatGatewayDestinationIpPortTranslationNatRules": {
    "params": [
      {
        "name": "NatGatewayIds",
        "desc": "NAT gateway ID."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions:\n`NatGatewayIds` and `Filters` cannot be specified at the same time.\n<li> nat-gateway-id, the NAT gateway ID, such as `nat-0yi4hekt`.</li>\n<li> vpc-id, the VPC ID, such as `vpc-0yi4hekt`.</li>\n<li> public-ip-address, the EIP, such as `139.199.232.238`.</li>\n<li>public-port, the public network port.</li>\n<li>private-ip-address, the private IP, such as `10.0.0.1`.</li>\n<li>private-port, the private network port.</li>\n<li>description, the rule description.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeNatGatewayDestinationIpPortTranslationNatRules) is used to query the array of objects of the port forwarding rules for a NAT gateway."
  },
  "ModifyServiceTemplateGroupAttribute": {
    "params": [
      {
        "name": "ServiceTemplateGroupId",
        "desc": "The protocol port template group instance ID, such as `ppmg-ei8hfd9a`."
      },
      {
        "name": "ServiceTemplateGroupName",
        "desc": "Protocol port template group name."
      },
      {
        "name": "ServiceTemplateIds",
        "desc": "Instance ID of the protocol port template, such as `ppm-4dw6agho`."
      }
    ],
    "desc": "This API (ModifyServiceTemplateGroupAttribute) is used to modify a protocol port template group."
  },
  "DescribeCcnAttachedInstances": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      },
      {
        "name": "Filters",
        "desc": "Filter conditions:\n<li>ccn-id - String - (Filter condition) The CCN instance ID.</li>\n<li>instance-type - String - (Filter condition) The associated instance type.</li>\n<li>instance-region - String - (Filter condition) The associated instance region.</li>\n<li>instance-type - String - (Filter condition) The instance ID of the associated instance.</li>"
      },
      {
        "name": "CcnId",
        "desc": "The ID of the CCN instance"
      },
      {
        "name": "OrderField",
        "desc": "The order field supports `CcnId`, `InstanceType`, `InstanceId`, `InstanceName`, `InstanceRegion`, `AttachedTime`, and `State`."
      },
      {
        "name": "OrderDirection",
        "desc": "Order methods. Ascending: `ASC`, Descending: `DESC`."
      }
    ],
    "desc": "This API (DescribeCcnAttachedInstances) is used to query the network instances associated with the CCN instance."
  },
  "ResetRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      },
      {
        "name": "RouteTableName",
        "desc": "The route table name. The maximum length is 60 characters."
      },
      {
        "name": "Routes",
        "desc": "Routing policy."
      }
    ],
    "desc": "This API (ResetRoutes) is used to reset the name of a route table and all its routing policies.<br />\nNote: When this API is called, all routing policies in the current route table are deleted before new routing policies are saved, which may incur network interruption."
  },
  "DescribeNetworkInterfaceLimit": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "The ID of the CVM instance to be queried."
      }
    ],
    "desc": "This API (DescribeNetworkInterfaceLimit) is used to query the ENI quota based on the CVM instance ID. It returns the ENI quota to which the CVM instance can be bound and the IP address quota that can be allocated to each ENI."
  },
  "DescribeNetDetects": {
    "params": [
      {
        "name": "NetDetectIds",
        "desc": "The array of network detection instance `IDs`, such as [`netd-12345678`]."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) The VPC instance ID, such as vpc-12345678.</li>\n<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>\n<li>subnet-id - String - (Filter condition) The subnet instance ID, such as subnet-12345678.</li>\n<li>net-detect-name - String - (Filter condition) The network detection name.</li>"
      },
      {
        "name": "Offset",
        "desc": "The offset. Default: 0."
      },
      {
        "name": "Limit",
        "desc": "The number of returned values. Default: 20. Maximum: 100."
      }
    ],
    "desc": "This API (DescribeNetDetects) is used to query the list of network detection instances."
  },
  "DescribeSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups."
      }
    ],
    "desc": "This API (DescribeSecurityGroupPolicies) is used to query security group policies."
  },
  "DescribeGatewayFlowMonitorDetail": {
    "params": [
      {
        "name": "TimePoint",
        "desc": "The point in time. This indicates details of this minute will be queried. For example, in `2019-02-28 18:15:20`, details at `18:15` will be queried."
      },
      {
        "name": "VpnId",
        "desc": "The instance ID of the VPN gateway, such as `vpn-ltjahce6`."
      },
      {
        "name": "DirectConnectGatewayId",
        "desc": "The instance ID of the Direct Connect gateway, such as `dcg-ltjahce6`."
      },
      {
        "name": "PeeringConnectionId",
        "desc": "The instance ID of the peering connection, such as `pcx-ltjahce6`."
      },
      {
        "name": "NatId",
        "desc": "The instance ID of the NAT gateway, such as `nat-ltjahce6`."
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      },
      {
        "name": "OrderField",
        "desc": "The order field supports `InPkg`, `OutPkg`, `InTraffic`, and `OutTraffic`."
      },
      {
        "name": "OrderDirection",
        "desc": "Order methods. Ascending: `ASC`, Descending: `DESC`."
      }
    ],
    "desc": "This API (DescribeGatewayFlowMonitorDetail) is used to query the monitoring details of the gateway traffic.\n* Only querying of a single gateway instance is supported. That is, only one of the `VpnId`, `DirectConnectGatewayId`, `PeeringConnectionId`, or `NatId` input parameters is supported, and one must be used.\n* If the gateway has traffic, but no data is returned when this API is called, please check whether gateway traffic monitoring has been enabled in the corresponding gateway details page in the console."
  },
  "UnassignIpv6Addresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The `ID` of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "The list of specified `IPv6` addresses. A maximum of 10 can be specified each time."
      }
    ],
    "desc": "This API (UnassignIpv6Addresses) is used to release ENI `IPv6` addresses.<br />\nThis API is completed asynchronously. If you need to query the async execution results, use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "DeleteVpnConnection": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      }
    ],
    "desc": "This API (DeleteVpnConnection) is used to delete VPN tunnels."
  },
  "ModifyAddressTemplateGroupAttribute": {
    "params": [
      {
        "name": "AddressTemplateGroupId",
        "desc": "IP address template group instance ID, such as `ipmg-2uw6ujo6`."
      },
      {
        "name": "AddressTemplateGroupName",
        "desc": "IP address template group name."
      },
      {
        "name": "AddressTemplateIds",
        "desc": "IP address template instance ID, such as `ipm-mdunqeb6`."
      }
    ],
    "desc": "This API (ModifyAddressTemplateGroupAttribute) is used to modify an IP address template group."
  },
  "DescribeAddresses": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "The list of unique IDs of EIPs, such as `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "The upper limit for `Filters` in each request is 10 and 5 for `Filter.Values`. `AddressIds` and `Filters` cannot be specified at the same time. Detailed filter conditions are as follows:\n<li> address-id - String - Required: no - (Filter condition) The unique EIP ID, such as `eip-11112222`.</li>\n<li> address-name - String - Required: no - (Filter condition) The EIP name. Fuzzy filtering is not supported.</li>\n<li> address-ip - String - Required: no - (Filter condition) Filters by EIP.</li>\n<li> address-status - String - Required: no - (Filter condition) The EIP state. Possible EIP states are: 'CREATING', 'BINDING', 'BIND', 'UNBINDING', 'UNBIND', 'OFFLINING', and 'BIND_ENI'.</li>\n<li> instance-id - String - Required: no - (Filter condition) The ID of the instance bound to the EIP, such as `ins-11112222`.</li>\n<li> private-ip-address - String - Required: no - (Filter condition) The private IP address bound to the EIP.</li>\n<li> network-interface-id - String - Required: no - (Filter condition) The ID of the ENI bound to the EIP, such as `eni-11112222`.</li>\n<li> is-arrears - String - Required: no - (Filter condition) Whether the EIP is in arrears. (TRUE: the EIP is in arrears | FALSE: the billing status of the EIP is normal)</li>"
      },
      {
        "name": "Offset",
        "desc": "The Offset. The default value is 0. For more information on `Offset`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646)."
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. The default value is 20. The maximum is 100. For more information on `Limit`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/product/11646)."
      }
    ],
    "desc": "This API (DescribeAddresses) is used to query the information of one or multiple [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* If the parameter is empty, a number (as specified by the `Limit`, the default value is 20) of EIPs will be returned."
  },
  "ModifyServiceTemplateAttribute": {
    "params": [
      {
        "name": "ServiceTemplateId",
        "desc": "Protocol port template instance ID, such as `ppm-529nwwj8`."
      },
      {
        "name": "ServiceTemplateName",
        "desc": "Protocol port template name."
      },
      {
        "name": "Services",
        "desc": "It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE."
      }
    ],
    "desc": "This API (ModifyServiceTemplateAttribute) is used to modify a protocol port template."
  },
  "DetachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "The list of network instances to be unbound"
      }
    ],
    "desc": "This API (DetachCcnInstances) is used to unbind a specified network instance from a CCN instance.<br />\nAfter unbinding the network instance, the corresponding routing policy will also be deleted."
  },
  "CreateVpnConnection": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "CustomerGatewayId",
        "desc": "The ID of the customer gateway, such as `cgw-2wqq41m9`. You can query the customer gateway by using the `DescribeCustomerGateways` API."
      },
      {
        "name": "VpnConnectionName",
        "desc": "Gateway can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "PreShareKey",
        "desc": "The pre-shared key."
      },
      {
        "name": "SecurityPolicyDatabases",
        "desc": "The SPD policy group, for example: {\"10.0.0.5/24\":[\"172.123.10.5/16\"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC."
      },
      {
        "name": "IKEOptionsSpecification",
        "desc": "Internet Key Exchange (IKE) configuration. IKE has a self-protection mechanism. The network security protocol is configured by the user."
      },
      {
        "name": "IPSECOptionsSpecification",
        "desc": "IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud."
      }
    ],
    "desc": "This API (CreateVpnConnection) is used to create VPN tunnel."
  },
  "CreateDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`"
      },
      {
        "name": "Routes",
        "desc": "The list of IDC IP range that must be connected"
      }
    ],
    "desc": "This API (CreateDirectConnectGatewayCcnRoutes) is used to create the CCN route (IDC IP range) of a Direct Connect gateway."
  },
  "DescribeNatGateways": {
    "params": [
      {
        "name": "NatGatewayIds",
        "desc": "The unified ID of the NAT gateways, such as `nat-123xx454`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `NatGatewayIds` and `Filters` cannot be specified at the same time.\n<li>nat-gateway-id - String - (Filter condition) The ID of the protocol port template instance, such as `nat-123xx454`.</li>\n<li>vpc-id - String - (Filter condition) The unique ID of the VPC, such as `vpc-123xx454`.</li>\n<li>nat-gateway-name - String - (Filter condition) The ID of the protocol port template instance, such as `test_nat`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeNatGateways) is used to query NAT gateways."
  },
  "CreateSubnets": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC` instance, such as `vpc-6v2ht8q5`."
      },
      {
        "name": "Subnets",
        "desc": "The subnet object list."
      }
    ],
    "desc": "This API (CreateSubnets) is used to create subnets in batches.\n* You must create a VPC before creating a subnet.\n* After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.\n* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).\n* IP address ranges of different subnets cannot overlap with each other within the same VPC.\n* A subnet is automatically associated with the default route table once created."
  },
  "ReplaceRouteTableAssociation": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "Subnet instance ID, such as `subnet-3x5lf5q0`. This can be queried using the DescribeSubnets API."
      },
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      }
    ],
    "desc": "This API (ReplaceRouteTableAssociation) is used to modify the route table associated with a subnet.\n* A subnet can only be associated with one route table."
  },
  "CheckNetDetectState": {
    "params": [
      {
        "name": "DetectDestinationIp",
        "desc": "The array of detection destination IPv4 addresses, which contains at most two IP addresses."
      },
      {
        "name": "NextHopType",
        "desc": "The type of the next hop. Currently supported types are:\nVPN: VPN gateway;\nDIRECTCONNECT: direct connect gateway;\nPEERCONNECTION: peering connection;\nNAT: NAT gateway;\nNORMAL_CVM: normal CVM."
      },
      {
        "name": "NextHopDestination",
        "desc": "The next-hop destination gateway. The value is related to NextHopType.\nIf NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.\nIf NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.\nIf NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.\nIf NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.\nIf NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12."
      },
      {
        "name": "NetDetectId",
        "desc": "The ID of a network detection instance, such as netd-12345678."
      },
      {
        "name": "VpcId",
        "desc": "The `ID` of a `VPC` instance, such as `vpc-12345678`."
      },
      {
        "name": "SubnetId",
        "desc": "The ID of a subnet instance, such as subnet-12345678."
      },
      {
        "name": "NetDetectName",
        "desc": "The name of a network detection instance. The maximum length is 60 characters."
      }
    ],
    "desc": "This API is used to verify the network detection status."
  },
  "DescribeVpcs": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "The VPC instance ID, such as `vpc-f49l6u0z`. Each request supports a maximum of 100 instances. `VpcIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `VpcIds` and `Filters` cannot be specified at the same time.\n<li>vpc-name - String - (Filter condition) VPC instance name.</li>\n<li>is-default - String - (Filter condition) Indicates whether it is the default VPC.</li>\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>cidr-block - String - (Filter condition) VPC CIDR.</li>\n<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>\n<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeVpcs) is used to query the VPC list."
  },
  "DeleteDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`"
      },
      {
        "name": "RouteIds",
        "desc": "The route ID, such as `ccnr-f49l6u0z`."
      }
    ],
    "desc": "This API (DeleteDirectConnectGatewayCcnRoutes) is used to delete the CCN routes (IDC IP range) of a Direct Connect gateway."
  },
  "RejectAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "The list of instances whose association is rejected."
      }
    ],
    "desc": "This API (RejectAttachCcnInstances) is used to reject association operations when instances are associated across accounts for the CCN owner.\n"
  },
  "DeleteSecurityGroup": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      }
    ],
    "desc": "This API (DeleteSecurityGroup) is used to delete security groups (SecurityGroup).\n* Only security groups under the current account can be deleted.\n* A security group cannot be deleted directly if its instance ID is used in the policy of another security group. You need to modify the policy first and then delete the security group.\n* A security group cannot be recovered after deletion, please proceed with caution."
  },
  "ModifyAddressesBandwidth": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "The unique ID of the EIP, such as 'eip-xxxx'."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "Target bandwidth value adjustment"
      },
      {
        "name": "StartTime",
        "desc": "The monthly bandwidth start time"
      },
      {
        "name": "EndTime",
        "desc": "The monthly bandwidth end time"
      }
    ],
    "desc": "This API (ModifyAddressesBandwidth) is used to adjust [Elastic IP](https://cloud.tencent.com/document/product/213/1941) bandwidth, including the postpaid EIP, prepaid EIP and bandwidth package EIP."
  },
  "CreateNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "DestinationIpPortTranslationNatRules",
        "desc": "The port forwarding rules of the NAT gateway."
      }
    ],
    "desc": "This API (CreateNatGatewayDestinationIpPortTranslationNatRule) is used to create a port forwarding rule for a NAT gateway."
  },
  "CreateSubnet": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance to be operated on. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "SubnetName",
        "desc": "The subnet name. The maximum length is 60 bytes."
      },
      {
        "name": "CidrBlock",
        "desc": "The subnet IP address range. It must be within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC."
      },
      {
        "name": "Zone",
        "desc": "The ID of the availability zone in which the subnet resides. You can set up disaster recovery across availability zones by choosing different availability zones for different subnets."
      }
    ],
    "desc": "This API (CreateSubnet) is used to create subnets.\n* You must create a VPC before creating a subnet.\n* After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.\n* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).\n* IP address ranges of different subnets cannot overlap with each other within the same VPC.\n* A subnet is automatically associated with the default route table once created."
  },
  "ModifyAddressTemplateAttribute": {
    "params": [
      {
        "name": "AddressTemplateId",
        "desc": "IP address template instance ID, such as `ipm-mdunqeb6`."
      },
      {
        "name": "AddressTemplateName",
        "desc": "IP address template name."
      },
      {
        "name": "Addresses",
        "desc": "Address information, including IP, CIDR and IP address range."
      }
    ],
    "desc": "This API (ModifyAddressTemplateAttribute) is used to modify an IP address template."
  },
  "AcceptAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "List of associated instances."
      }
    ],
    "desc": "This API (AcceptAttachCcnInstances) is used to associate instances across accounts. Cloud Connect Network (CCN) owners accept and agree to the operations."
  },
  "DeleteServiceTemplateGroup": {
    "params": [
      {
        "name": "ServiceTemplateGroupId",
        "desc": "The protocol port template group instance ID, such as `ppmg-n17uxvve`."
      }
    ],
    "desc": "This API (DeleteServiceTemplateGroup) is used to delete a protocol port template group."
  },
  "DisassociateAddress": {
    "params": [
      {
        "name": "AddressId",
        "desc": "The unique ID of the EIP, such as `eip-11112222`."
      },
      {
        "name": "ReallocateNormalPublicIp",
        "desc": "Whether a common public IP is assigned after the EIP is unbound. Value range:<br><li>TRUE: Indicates that after the EIP is unbound, a common public IP is assigned.<br><li>FALSE: Indicates that after the EIP is unbound, a common public IP is not assigned.<br>Default value: FALSE.<br><br>The parameter can be specified only under the following conditions:<br><li>It can only be specified when you unbind an EIP from the primary private IP of the primary ENI.<br><li>After an EIP is unbound, you can assign public IPs to an account up to 10 times per day. For more information, use the [DescribeAddressQuota] (https://cloud.tencent.com/document/api/213/1378) API."
      }
    ],
    "desc": "This API (DisassociateAddress) is used to unbind [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* The unbinding of EIPs from CVM instances and ENIs is supported.\n* The unbinding of EIPs from NATs is not supported. For information about how to unbind an EIP from a NAT, see [EipUnBindNatGateway](https://cloud.tencent.com/document/product/215/4092).\n* You can only unbind EIPs in BIND or BIND_ENI status.\n* Blocked EIPs cannot be unbound."
  },
  "DeleteSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "The policy set of the security group. One request can only delete one or more policies in one direction. Both PolicyIndex-matching deletion and security group policy-matching deletion methods are supported. Each request can use only one matching method."
      }
    ],
    "desc": "This API (DeleteSecurityGroupPolicies) is used to delete security group policies (SecurityGroupPolicy).\n* SecurityGroupPolicySet.Version is used to specify the version of the security group you are operating. If the specified Version number differs from the latest version of the current security group, a failure will be returned. If Version is not specified, the policy of the specified PolicyIndex will be deleted directly."
  },
  "CreateVpc": {
    "params": [
      {
        "name": "VpcName",
        "desc": "The VPC name. The maximum length is 60 bytes."
      },
      {
        "name": "CidrBlock",
        "desc": "VPC CIDR, which must fall within the following private network IP ranges: 10.0.0.0/16, 172.16.0.0/16, and 192.168.0.0/16."
      },
      {
        "name": "EnableMulticast",
        "desc": "Whether multicast is enabled. `true`: Enabled. `false`: Not enabled."
      },
      {
        "name": "DnsServers",
        "desc": "The DNS address. A maximum of 4 addresses is supported."
      },
      {
        "name": "DomainName",
        "desc": "Domain name"
      }
    ],
    "desc": "This API (CreateVpc) is used to create a VPC.\n* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses). For more information, please see corresponding documents about VPC IP address ranges.\n* The number of VPCs that can be created in a region is limited. For more information, please see <a href=\"https://intl.cloud.tencent.com/doc/product/215/537\" title=\"VPC use limits\">VPC use limits</a>. To request more resources, please contact the online customer service."
  },
  "AssignIpv6SubnetCidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6SubnetCidrBlocks",
        "desc": "The assigned `IPv6` subnet IP range list."
      }
    ],
    "desc": "This API (AssignIpv6SubnetCidrBlock) is used to assign IPv6 subnet IP ranges.\n* To assign an `IPv6` IP range to a subnet, the `VPC` that the subnet belongs to should have obtained the `IPv6` IP range. If this has not been assigned, use the `AssignIpv6CidrBlock` API to assign an `IPv6` IP range to the `VPC` to which the subnet belongs. Otherwise, the `IPv6` subnet IP range cannot be assigned.\n* Each subnet can only be assigned one IPv6 IP range."
  },
  "AllocateAddresses": {
    "params": [
      {
        "name": "AddressCount",
        "desc": "The number of EIPs. Default: 1."
      },
      {
        "name": "InternetServiceProvider",
        "desc": "The EIP line type. Default: BGP.\n<ul style=\"margin:0\"><li>For a user who has activated the static single-line IP whitelist, possible values are:<ul><li>CMCC: China Mobile</li>\n<li>CTCC: China Telecom</li>\n<li>CUCC: China Unicom</li></ul>Note: Only certain regions support static single-line IP addresses.</li></ul>"
      },
      {
        "name": "InternetChargeType",
        "desc": "The EIP billing method.\n<ul style=\"margin:0\"><li>For a user who has activated bandwidth billing by IP whitelist, possible values are:<ul><li>BANDWIDTH_PACKAGE: paid by the [bandwidth package](https://cloud.tencent.com/document/product/684/15255) (The bandwidth sharing whitelist must be activated additionally.)</li>\n<li>BANDWIDTH_POSTPAID_BY_HOUR: bandwidth postpaid by hour</li>\n<li>TRAFFIC_POSTPAID_BY_HOUR: traffic postpaid by hour</li></ul>Default: TRAFFIC_POSTPAID_BY_HOUR</li>.\n<li>For users who do not use bill-by-bandwidth billing mode, InternetChargeType is consistent with that of the instance bound to the EIP. Therefore, it is unnecessary to pass in this parameter.</li></ul>"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The maximum EIP outbound bandwidth. Unit: Mbps.\n<ul style=\"margin:0\"><li>For a user who has activated bandwidth billing by IP whitelist, the value range is determined by the EIP billing method:<ul><li>BANDWIDTH_PACKAGE: 1 Mbps to 1,000 Mbps</li>\n<li>BANDWIDTH_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li>\n<li>TRAFFIC_POSTPAID_BY_HOUR: 1 Mbps to 100 Mbps</li></ul>Default: 1 Mbps</li>.\n<li>For a user who has not activated bandwidth billing by IP whitelist, InternetMaxBandwidthOut is consistent with that of the instance bound to the EIP. Therefore, it is unnecessary to pass in this parameter.</li></ul>"
      },
      {
        "name": "AddressType",
        "desc": "The EIP type. Default: EIP.\n<ul style=\"margin:0\"><li>For a user who has activated the AIA whitelist, possible values are:<ul><li>AnycastEIP: an Anycast EIP address. For more information, see [Anycast Internet Acceleration](https://cloud.tencent.com/document/product/644).</li></ul>Note: Only certain regions support Anycast EIPs.</li></ul>"
      },
      {
        "name": "AnycastZone",
        "desc": "The Anycast publishing region.\n<ul style=\"margin:0\"><li>For a user who has activated the AIA whitelist, possible values are:<ul><li>ANYCAST_ZONE_GLOBAL: the global publishing region (the global AIA whitelist must be activated additionally.) </li><li>ANYCAST_ZONE_OVERSEAS: the publishing regions outside Mainland China </li></ul>Default: ANYCAST_ZONE_OVERSEAS.</li></ul>"
      },
      {
        "name": "ApplicableForCLB",
        "desc": "Whether the Anycast EIP can be bound to Cloud Load Balancer (CLB) instances.\n<ul style=\"margin:0\"><li>For a user who has activated the AIA whitelist, possible values are:<ul><li>TRUE: the Anycast EIP can be bound to CLB instances.</li>\n<li>FALSE: the Anycast EIP can be bound to CVMs, NAT gateways, and HA virtual IP addresses.</li></ul>Default: FALSE.</li></ul>"
      }
    ],
    "desc": "This API is used to apply for one or more [Elastic IP Addresses](https://cloud.tencent.com/document/product/213/1941) (EIPs for short).\n* An EIP is a static IP address that is dedicated for dynamic cloud computing. You can quickly re-map an EIP to another instance under your account to protect against instance failures.\n* Your EIP is associated with your Tencent Cloud account rather than an instance. It remains associated with your Tencent Cloud account until you choose to explicitly release it or your account is in arrears for more than 24 hours.\n* The maximum number of EIPs that can be applied for a Tencent Cloud account in each region is restricted. For more information, see [EIP Product Introduction](https://cloud.tencent.com/document/product/213/5733). You can get the quota information through the DescribeAddressQuota API."
  },
  "DescribeVpcIpv6Addresses": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "The `IP` address list. Each request supports a maximum of `10` batch querying."
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      }
    ],
    "desc": "This API (DescribeVpcIpv6Addresses) is used to query `VPC` `IPv6` information.\nThis API is used to query only the information of `IPv6` addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results."
  },
  "AttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "Instances",
        "desc": "List of associated network instances"
      },
      {
        "name": "CcnUin",
        "desc": "The UIN (root account) of the CCN. By default, the current account belongs to the UIN"
      }
    ],
    "desc": "This API (AttachCcnInstances) is used to load a network instance to a CCN instance. Network instances include VPCs and Direct Connect gateways.<br />\nThe number of network instances that each CCN can be associated with is limited. For more information, see the product documentation. If you need to associate more instances, please contact online customer service."
  },
  "AssociateAddress": {
    "params": [
      {
        "name": "AddressId",
        "desc": "The unique ID of the EIP, such as `eip-11112222`."
      },
      {
        "name": "InstanceId",
        "desc": "The ID of the instance to be bound, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API."
      },
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI to be bonud, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. You can query the ENI ID by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `networkInterfaceId` field in the returned result of [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817) API."
      },
      {
        "name": "PrivateIpAddress",
        "desc": "The private IP to be bound. If you specify `NetworkInterfaceId`, then you must also specify `PrivateIpAddress`, indicating the EIP is bound to the specified private IP of the specified ENI. At the same time, you must ensure the specified `PrivateIpAddress` is a private IP on the `NetworkInterfaceId`. You can query the private IP of the specified ENI by logging into the [Console](https://console.cloud.tencent.com/vpc/eni). You can also obtain the parameter value from the `privateIpAddress` field in the returned result of [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817) API."
      }
    ],
    "desc": "This API (AssociateAddress) is used to bind an [Elastic IP](https://cloud.tencent.com/document/product/213/1941) (EIP for short) to the specified private IP of an instance or ENI.\n* Essentially, binding an EIP to an instance (CVM) means binding an EIP to the primary private IP of the primary ENI on an instance.\n* When you bind an EIP to the primary private IP of the primary ENI, the previously bound public IP is automatically unbound and released.\n* To bind the EIP to the private IP of the specified ENI (not the primary private IP of the primary ENI), you must unbind the EIP before you can bind a new one.\n* To bind the EIP to a NAT gateway, use the API [EipBindNatGateway](https://cloud.tencent.com/document/product/215/4093)\n* EIP that is in arrears or blocked cannot be bound.\n* Only EIP in the UNBIND status can be bound."
  },
  "DeleteSubnet": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "The ID of the subnet instance. You can obtain the parameter value from the SubnetId field in the returned result of DescribeSubnets API."
      }
    ],
    "desc": "This API (DeleteSubnet) is used to delete subnets.\nBefore deleting a subnet, you need to remove all resources in the subnet, including CVMs, load balancers, cloud data, NoSQL databases, and ENIs."
  },
  "AttachClassicLinkVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC instance ID"
      },
      {
        "name": "InstanceIds",
        "desc": "CVM Instance ID"
      }
    ],
    "desc": "This API (AttachClassicLinkVpc) is used to create a Classiclink between a VPC and a basic network device.\n* The VPC and the basic network device must be in the same region.\n* For the difference between VPCs and basic networks, see VPC product documentation-<a href=\"https://cloud.tencent.com/document/product/215/535#2.-.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.8E.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C\">VPCs and basic networks</a>."
  },
  "DisassociateNatGatewayAddress": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "PublicIpAddresses",
        "desc": "The array of EIPs bound to the NAT gateway."
      }
    ],
    "desc": "This API (DisassociateNatGatewayAddress) is used to unbind an EIP from a NAT gateway."
  },
  "DescribeDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`."
      },
      {
        "name": "CcnRouteType",
        "desc": "The route learning type of the CCN. Available values:\n<li>`BGP` - Automatic learning.</li>\n<li>`STATIC` - Static means user-configured. This is the default value.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      }
    ],
    "desc": "This API (DescribeDirectConnectGatewayCcnRoutes) is used to query the CCN routes (IDC IP range) of the Direct Connect gateway."
  },
  "CreateNetworkInterface": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "The name of the ENI. The maximum length is 60 characters."
      },
      {
        "name": "SubnetId",
        "desc": "The subnet instance ID of the ENI, such as `subnet-0ap8nwca`."
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "ENI description can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "The number of private IP addresses that is newly applied for. The total number of private IP addresses cannot exceed the quota."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "Specifies the security group to be bound with, such as ['sg-1dd51d']."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The information of the specified private IPs. You can specify a maximum of 10 each time."
      },
      {
        "name": "Tags",
        "desc": "Bound tags, such as [{\"Key\": \"city\", \"Value\": \"shanghai\"}]."
      }
    ],
    "desc": "This API is used to create one or more ENIs.\n* You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be in the same subnet as the ENI and is not occupied.\n* When creating an ENI, you can specify the number of private IP addresses that you want to apply for. The system will randomly generate private IP addresses.\n* An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href=\"/document/product/576/18527\">ENI Use Limits</a>.\n* You can bind an existing security group when creating an ENI.\n* You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added."
  },
  "DescribeNetDetectStates": {
    "params": [
      {
        "name": "NetDetectIds",
        "desc": "The array of network detection instance `IDs`, such as [`netd-12345678`]."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `NetDetectIds` and `Filters` cannot be specified at the same time.\n<li>net-detect-id - String - (Filter condition) The network detection instance ID, such as netd-12345678.</li>"
      },
      {
        "name": "Offset",
        "desc": "The offset. Default: 0."
      },
      {
        "name": "Limit",
        "desc": "The number of returned values. Default: 20. Maximum: 100."
      }
    ],
    "desc": "This API (DescribeNetDetectStates) is used to query the list of network detection verification results."
  },
  "DescribeCcns": {
    "params": [
      {
        "name": "CcnIds",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`. Each request can have a maximum of 100 instances. `CcnIds` and `Filters` cannot be specified at the same time"
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `CcnIds` and `Filters` cannot be specified at the same time.\n<li>ccn-id - String - (Filter condition) The unique ID of the CCN, such as `vpc-f49l6u0z`.</li>\n<li>ccn-name - String - (Filter condition) The CCN name.</li>\n<li>ccn-description - String - (Filter condition) CCN description.</li>\n<li>state - String - (Filter condition) The instance status. 'ISOLATED': Isolated (the account is in arrears and the service is suspended.) 'AVAILABLE': Running.</li>\n<li>tag-key - String - Required: no - (Filter condition) Filters by tag key.</li>\n<li>`tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see this example: **Querying the list of CCNs bound to tags**.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      },
      {
        "name": "OrderField",
        "desc": "Order fields support `CcnId`, `CcnName`, `CreateTime`, `State`, and `QosLevel`"
      },
      {
        "name": "OrderDirection",
        "desc": "Order methods. Ascending: `ASC`, Descending: `DESC`."
      }
    ],
    "desc": "This API (DescribeCcns) is used to query the CCN list."
  },
  "DeleteCcn": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      }
    ],
    "desc": "This API (DeleteCcn) is used to delete CCNs.\n* After deletion, the routes between all instances associated with the CCN will be deleted, and the network will be interrupted. Please confirm this operation in advance.\n* CCN deletion is an irreversible operation. Please proceed with caution.\n"
  },
  "HaVipDisassociateAddressIp": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be an `HAVIP` that has been bound to an `EIP`."
      }
    ],
    "desc": "This API (HaVipDisassociateAddressIp) is used to unbind an EIP which has been bound to an HAVIP.<br />\nThis API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "DetachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "InstanceId",
        "desc": "The ID of the CVM instance, such as `ins-r8hr2upy`."
      }
    ],
    "desc": "This API (DetachNetworkInterface) is used to unbind an ENI from a CVM."
  },
  "DeleteNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      }
    ],
    "desc": "This API (DeleteNetworkInterface) is used to delete ENIs.\n* An ENI that has been bound to a CVM cannot be deleted.\n* An ENI can be deleted only after being unbound from the server. After the deletion, all private IP addresses associated with the ENI will be released."
  },
  "DescribeVpnConnections": {
    "params": [
      {
        "name": "VpnConnectionIds",
        "desc": "The instance ID of the VPN tunnel, such as `vpnx-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnConnectionIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "The filter condition. For details, see the Instance Filter Conditions Table. The upper limit for `Filters` in each request is 10 and 5 for `Filter.Values`. `VpnConnectionIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - The VPC instance ID, such as `vpc-0a36uwkr`.</li>\n<li>vpn-gateway-id - String - The VPN gateway instance ID, such as `vpngw-p4lmqawn`.</li>\n<li>customer-gateway-id - String - The customer gateway instance ID, such as `cgw-l4rblw63`.</li>\n<li>vpn-connection-name - String - The connection name, such as `test-vpn`.</li>\n<li>vpn-connection-id - String - The connection instance ID, such as `vpnx-5p7vkch8\"`.</li>"
      },
      {
        "name": "Offset",
        "desc": "The Offset. The default value is 0. For more information about Offset, see the relevant section in the API Introduction."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": " This API (DescribeVpnConnections) is used to query the VPN tunnel list."
  },
  "ReplaceRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      },
      {
        "name": "Routes",
        "desc": "Routing policy object. The routing policy ID (RouteId) must be specified."
      }
    ],
    "desc": "This API (ReplaceRoutes) is used to modify a specified routing policy by its ID (RouteId). Batch modification is supported."
  },
  "DeleteNatGateway": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      }
    ],
    "desc": "This API (DeleteNatGateway) is used to delete a NAT gateway.\nAfter the deletion of a NAT gateway, the system will automatically delete the routing entry that contains the NAT gateway from the route table. It will also unbind the Elastic IP."
  },
  "DownloadCustomerGatewayConfiguration": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      },
      {
        "name": "CustomerGatewayVendor",
        "desc": "Customer gateway vendor information object, which can be obtained through DescribeCustomerGatewayVendors."
      },
      {
        "name": "InterfaceName",
        "desc": "Name of the physical API for tunnel access device."
      }
    ],
    "desc": "This API (DownloadCustomerGatewayConfiguration) is used to download a VPN tunnel configuration."
  },
  "DeleteServiceTemplate": {
    "params": [
      {
        "name": "ServiceTemplateId",
        "desc": "Protocol port template instance ID, such as `ppm-e6dy460g`."
      }
    ],
    "desc": "This API (DeleteServiceTemplate) is used to delete a protocol port template."
  },
  "UnassignPrivateIpAddresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The information of the specified private IPs. You can specify a maximum of 10 each time."
      }
    ],
    "desc": "This API (UnassignPrivateIpAddresses) is used to return the private IPs of ENI.\n* To return the secondary private IPs of an ENI, the API will automatically unbind the IPs of an ENI. The primary private IP of the ENI cannot be returned."
  },
  "DeleteAddressTemplateGroup": {
    "params": [
      {
        "name": "AddressTemplateGroupId",
        "desc": "The IP address template group instance ID, such as `ipmg-90cex8mq`."
      }
    ],
    "desc": "This API (DeleteAddressTemplateGroup) is used to delete an IP address template group."
  },
  "DescribeCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-gree226l`."
      },
      {
        "name": "RouteIds",
        "desc": "The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `RouteIds` and `Filters` cannot be specified at the same time.\n<li>route-id - String - (Filter condition) Routing policy ID.</li>\n<li>cidr-block - String - (Filter condition) Destination port.</li>\n<li>instance-type - String - (Filter condition) The next hop type.</li>\n<li>instance-region - String - (Filter condition) The next hop region.</li>\n<li>instance-type - String - (Filter condition) The instance ID of the next hop.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeCcnRoutes) is used to query routes that have been added to a CCN."
  },
  "CreateDefaultVpc": {
    "params": [
      {
        "name": "Zone",
        "desc": "The ID of the availability zone in which the subnet resides. The availability zone will be randomly selected if not specified."
      },
      {
        "name": "Force",
        "desc": "Whether to forcibly return a default VPC"
      }
    ],
    "desc": "This API is used to create a default VPC.\n\nThe default VPC is suitable for getting started with and launching public instances, and it can be used like any other VPCs. To create a standard VPC, for which you need to specify a VPC name, VPC IP range, subnet IP range, and subnet availability zone, use the regular CreateVpc API.\n\nUnder normal circumstances, this API may not create a default VPC. It depends on the network attributes (DescribeAccountAttributes) of your account.\n* If both basic network and VPC are supported, the returned VpcId is 0.\n* If only VPC is supported, the default VPC information is returned.\n\nYou can also use the Force parameter to forcibly return a default VPC."
  },
  "AttachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "InstanceId",
        "desc": "The ID of the CVM instance, such as `ins-r8hr2upy`."
      }
    ],
    "desc": "This API (AttachNetworkInterface) is used to bind an ENI to a CVM.\n* One CVM can be bound to multiple ENIs, but only one primary ENI. For more information on the limits, see <a href=\"https://cloud.tencent.com/document/product/215/6513\">ENI use limits</a>.\n* An ENI can only be bound to one CVM at a time.\n* Only CVMs in running or shutdown status can be bound to an ENI. For more information about CVM status, see <a href=\"https://cloud.tencent.com/document/api/213/9452#instance_state\">Tencent CVM information</a>.\n* An ENI can only be bound to a CVM in VPC, and the CVM must reside in the same availability zone as the subnet of the ENI."
  },
  "ReplaceDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "The ID of the Direct Connect gateway, such as `dcg-prpqlmg1`"
      },
      {
        "name": "Routes",
        "desc": "The list of IDC IP range that must be connected"
      }
    ],
    "desc": "This API (ReplaceDirectConnectGatewayCcnRoutes) is used to modify the specified route according to the route ID. Batch modification is supported."
  },
  "CreateNatGateway": {
    "params": [
      {
        "name": "NatGatewayName",
        "desc": "NAT gateway name"
      },
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The maximum outbound bandwidth of the NAT gateway (unit: Mbps). Supported parameter values: `20, 50, 100, 200, 500, 1000, 2000, 5000`. Default: `100Mbps`."
      },
      {
        "name": "MaxConcurrentConnection",
        "desc": "The concurrent connection cap of the NAT gateway. Supported parameter values: `1000000, 3000000, 10000000`. The default value is `100000`."
      },
      {
        "name": "AddressCount",
        "desc": "The number of EIPs that needs to be applied for. The system will create N number of EIPs according to your requirements. Either AddressCount or PublicAddresses must be passed in."
      },
      {
        "name": "PublicIpAddresses",
        "desc": "The EIP array bound to the NAT gateway. Either AddressCount or PublicAddresses must be passed in."
      },
      {
        "name": "Zone",
        "desc": "The availability zone, such as `ap-guangzhou-1`."
      }
    ],
    "desc": "This API (CreateNatGateway) is used to create a NAT gateway."
  },
  "DeleteNetDetect": {
    "params": [
      {
        "name": "NetDetectId",
        "desc": "The `ID` of a network detection instance, such as `netd-12345678`."
      }
    ],
    "desc": "This API (DeleteNetDetect) is used to delete a network detection instance."
  },
  "ModifySecurityGroupAttribute": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "GroupName",
        "desc": "Security group can be named freely, but cannot exceed 60 characters."
      },
      {
        "name": "GroupDescription",
        "desc": "The remarks for the security group. The maximum length is 100 characters."
      }
    ],
    "desc": "This API (ModifySecurityGroupAttribute) is used to modify the attributes of a security group (SecurityGroupPolicy)."
  },
  "DeleteAddressTemplate": {
    "params": [
      {
        "name": "AddressTemplateId",
        "desc": "The IP address template instance ID, such as `ipm-09o5m8kc`."
      }
    ],
    "desc": "This API (DeleteAddressTemplate) is used to delete an IP address template."
  },
  "DeleteVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      }
    ],
    "desc": "This API (DeleteVpnGateway) is used to delete a VPN gateway. Currently, only deletion of pay-as-you-go IPSEC gateway instances in running status is supported."
  },
  "CreateServiceTemplate": {
    "params": [
      {
        "name": "ServiceTemplateName",
        "desc": "Template name of the protocol port"
      },
      {
        "name": "Services",
        "desc": "It supports single port, multiple ports, consecutive ports and all ports. Supported protocols include TCP, UDP, ICMP, and GRE."
      }
    ],
    "desc": "This API (CreateServiceTemplate) is used to create a protocol port template."
  },
  "DeleteRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "Route table instance ID."
      },
      {
        "name": "Routes",
        "desc": "Routing policy object."
      }
    ],
    "desc": "This API (DeleteRoutes) is used to delete routing policies in batches from a route table."
  },
  "ModifySecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "The security group policy set. SecurityGroupPolicySet object must specify new egress and ingress policies at the same time. SecurityGroupPolicy object does not support custom index (PolicyIndex)."
      },
      {
        "name": "SortPolicys",
        "desc": "Whether security group sorting is supported. True indicates that security group sorting is supported. If SortPolicys does not exist or is set to False, the security group policy can be modified."
      }
    ],
    "desc": "This API (ModifySecurityGroupPolicies) is used to reset the egress and ingress policies (SecurityGroupPolicy) of a security group.\n\n* This API deletes all the current egress and ingress policies, and then adds new Egress and Ingress policies. It does not support custom PolicyIndex indexes.\n* If SecurityGroupPolicySet.Version is set to 0, all policies will be cleared, and Egress and Ingress will be ignored.\n* The value of the Protocol field can be TCP, UDP, ICMP, ICMPV6, GRE, or ALL.\n* The CidrBlock field allows you to enter any string that conforms to the CIDR format. (More details) In a basic network, if a CidrBlock contains private IP addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.\n* The Ipv6CidrBlock field allows you to enter any string that conforms to the IPv6 CIDR format. (More details) In a basic network, if an Ipv6CidrBlock contains private IPv6 addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.\n* The SecurityGroupId field allows you to enter the IDs of security groups that are in the same project as the security group to be modified, including the ID of the security group itself, to represent private IP addresses of all CVMs under the security group. If this field is used, this policy will change without manual modification according to the CVM associated with the policy ID while being used to match network messages.\n* The Port field allows you to enter a single port number, or two port numbers separated by a minus sign to represent a port range, such as 80 or 8000-8010. The Port field can be used only when the value of the Protocol field is TCP or UDP.\n* The Action field only allows you to enter ACCEPT or DROP.\n* CidrBlock, Ipv6CidrBlock, SecurityGroupId, and AddressTemplate are exclusive and cannot be entered at the same time. Protocol + Port and ServiceTemplate are mutually exclusive and cannot be entered at the same time."
  },
  "ModifySubnetAttribute": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "Subnet instance ID, such as `subnet-pxir56ns`."
      },
      {
        "name": "SubnetName",
        "desc": "The subnet name. The maximum length is 60 bytes."
      },
      {
        "name": "EnableBroadcast",
        "desc": "Whether the subnet has broadcast enabled."
      }
    ],
    "desc": "This API (ModifySubnetAttribute) is used to modify subnet attributes."
  },
  "DisableCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "RouteIds",
        "desc": "The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`."
      }
    ],
    "desc": "This API (DisableCcnRoutes) is used to disable CCN routes that are already enabled."
  },
  "InquiryPriceCreateVpnGateway": {
    "params": [
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps."
      },
      {
        "name": "InstanceChargeType",
        "desc": "The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances."
      }
    ],
    "desc": "This API (InquiryPriceCreateVpnGateway) is used to query the price for VPN gateway creation."
  },
  "ResetVpnConnection": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      }
    ],
    "desc": "The API (ResetVpnConnection) is used to reset VPN tunnels."
  },
  "CreateAddressTemplateGroup": {
    "params": [
      {
        "name": "AddressTemplateGroupName",
        "desc": "The name of the IP address template group."
      },
      {
        "name": "AddressTemplateIds",
        "desc": "The instance ID of the IP address template, such as `ipm-mdunqeb6`."
      }
    ],
    "desc": "This API (CreateAddressTemplateGroup) is used to create an IP address template group."
  },
  "CreateSecurityGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "Security group can be named freely, but cannot exceed 60 characters."
      },
      {
        "name": "GroupDescription",
        "desc": "The remarks for the security group. The maximum length is 100 characters."
      },
      {
        "name": "ProjectId",
        "desc": "The project id is 0 by default. You can query this in the project management page of the Qcloud console."
      }
    ],
    "desc": "This API (CreateSecurityGroup) is used to create security groups (SecurityGroup).\n* <a href=\"https://cloud.tencent.com/document/product/213/500#2.-.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84.E9.99.90.E5.88.B6\">Security group limits</a> for each project in each region under each account.\n* Both the inbound and outbound rules for a newly created security group are Deny All by default. You need to call CreateSecurityGroupPolicies to set the security group rules according to your needs."
  },
  "ModifyNetworkInterfaceAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-pxir56ns`."
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "The name of the ENI. The maximum length is 60 characters."
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "ENI description can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "SecurityGroupIds",
        "desc": "The specified security groups to be bound with, such as ['sg-1dd51d']."
      }
    ],
    "desc": "This API (ModifyNetworkInterfaceAttribute) is used to modify ENI attributes."
  },
  "DescribeVpnGateways": {
    "params": [
      {
        "name": "VpnGatewayIds",
        "desc": "The VPN gateway instance ID, such as `vpngw-f49l6u0z`. Each request can have a maximum of 100 instances. `VpnGatewayIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `VpnGatewayIds` and `Filters` cannot be specified at the same time.\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>vpn-gateway-id - String - (Filter condition) VPN instance ID, such as `vpngw-5aluhh9t`.</li>\n<li>vpn-gateway-name - String - (Filter condition) VPN instance name.</li>\n<li>type - String - (Filter condition) VPN gateway type: 'IPSEC', 'SSL'.</li>\n<li>public-ip-address- String - (Filter condition) Public IP.</li>\n<li>renew-flag - String - (Filter condition) Gateway renewal type. Manual renewal: `NOTIFY_AND_MANUAL_RENEW`, Automatic renewal: `NOTIFY_AND_AUTO_RENEW`.</li>\n<li>zone - String - (Filter condition) The availability zone where the VPN is located, such as `ap-guangzhou-2`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The number of request objects."
      }
    ],
    "desc": "This API (DescribeVpnGateways) is used to query the VPN gateway list."
  },
  "DeleteRouteTable": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      }
    ],
    "desc": "This API is used to delete a route table."
  },
  "ModifyIpv6AddressesAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The `ID` of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "The information of the specified private `IPv6` addresses."
      }
    ],
    "desc": "This API (ModifyIpv6AddressesAttribute) is used to modify the private IPv6 address attributes of an ENI."
  },
  "DescribeAccountAttributes": {
    "params": [],
    "desc": "This API (DescribeAccountAttributes) is used to query your account attributes."
  },
  "AssignIpv6Addresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The `ID` of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "Ipv6Addresses",
        "desc": "The specified `IPv6` address list. You can specify a maximum of 10 at one time. The quota is calculated together with the `Ipv6AddressCount` input parameter."
      },
      {
        "name": "Ipv6AddressCount",
        "desc": "The number of automatically assigned `IPv6` addresses. The total number of private IP addresses cannot exceed the quota. The quota is calculated together with the `Ipv6Addresses` input parameter."
      }
    ],
    "desc": "This API (AssignIpv6Addresses) is used to apply for an IPv6 address for the ENI.<br />\nThis API is completed asynchronously. If you need to query the async execution results, use the `RequestId` returned by this API to query the `QueryTask` API.\n* An ENI can only be bound with a limited number of IPs. For more information about resource limits, see<a href=\"/document/product/576/18527\">ENI use limits</a>.\n* You can specify the `IPv6` address when applying. The address type cannot be the primary `IP`. Currently, `IPv6` can only be supported as the secondary `IP`.\n* The address must be unoccupied and is in the subnet to which the ENI belongs.\n* When applying for one to multiple secondary `IPv6` addresses on ENI, the API will return the specified number of secondary `IPv6` addresses in the subnet range where the ENI is located."
  },
  "MigratePrivateIpAddress": {
    "params": [
      {
        "name": "SourceNetworkInterfaceId",
        "desc": "ID of the ENI instance bound with the private IP, such as `eni-m6dyj72l`."
      },
      {
        "name": "DestinationNetworkInterfaceId",
        "desc": "ID of the destination ENI instance to be migrated."
      },
      {
        "name": "PrivateIpAddress",
        "desc": "The private IP to be migrated, such as 10.0.0.6."
      }
    ],
    "desc": " This API (MigratePrivateIpAddress) is used to migrate the private IPs of ENIs.\n\n* This API is used to migrate a private IP from one ENI to another. Primary IPs cannot be migrated.\n* The ENIs before and after migration must belong to the same subnet."
  },
  "DescribeServiceTemplates": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>service-template-name - String - (Filter condition) Protocol port template name.</li>\n<li>service-template-id - String - (Filter condition) Protocol port template instance ID, such as `ppm-e6dy460g`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeServiceTemplates) is used to query protocol port templates."
  },
  "UnassignIpv6CidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6CidrBlock",
        "desc": "The `IPv6` IP range, such as `3402:4e00:20:1000::/56`"
      }
    ],
    "desc": "This API (UnassignIpv6CidrBlock) is used to release IPv6 IP ranges.\nIf the IP range still has occupied IPs that are not yet repossessed, the IP range cannot be released."
  },
  "ModifyNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "SourceNatRule",
        "desc": "The port forwarding rule of the source NAT gateway."
      },
      {
        "name": "DestinationNatRule",
        "desc": "The port forwarding rule of the destination NAT gateway."
      }
    ],
    "desc": "This API (ModifyNatGatewayDestinationIpPortTranslationNatRule) is used to modify a port forwarding rule for a NAT gateway."
  },
  "HaVipAssociateAddressIp": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`. This must be a `HAVIP` that has not been bound to an `EIP`"
      },
      {
        "name": "AddressIp",
        "desc": "The Elastic `IP`. This must be an `EIP` that has not been bound to a `HAVIP`"
      }
    ],
    "desc": "This API (HaVipAssociateAddressIp) is used to bind an EIP to an HAVIP.<br />\nThis API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "DescribeHaVips": {
    "params": [
      {
        "name": "HaVipIds",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `HaVipIds` and `Filters` cannot be specified at the same time.\n<li>havip-id - String - The unique `ID` of the `HAVIP`, such as `havip-9o233uri`.</li>\n<li>havip-name - String - `HAVIP` name.</li>\n<li>vpc-id - String - The `ID` of the VPC where `HAVIP` is located.</li>\n<li>subnet-id - String - The `ID` of the subnet where `HAVIP` is located.</li>\n<li>address-ip - String - The `EIP` to which `HAVIP` is bound.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeHaVips) is used to query the list of highly available virtual IPs (HAVIP)."
  },
  "DeleteHaVip": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`."
      }
    ],
    "desc": "This API (DeleteHaVip) is used to delete Highly Available Virtual IP (HAVIP)<br />\nThis API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to query the `QueryTask` API."
  },
  "DescribeAddressQuota": {
    "params": [],
    "desc": "This API (DescribeAddressQuota) is used to query the quota information of your [Elastic IP](https://cloud.tencent.com/document/product/213/1941) (EIP) in the current region. For more information, see [EIP product introduction](https://cloud.tencent.com/document/product/213/5733)."
  },
  "ModifyVpnGatewayAttribute": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "VpnGatewayName",
        "desc": "The VPN gateway name. The maximum length is 60 bytes."
      },
      {
        "name": "InstanceChargeType",
        "desc": "VPN gateway billing mode. Currently, only the conversion of prepaid (monthly subscription) to postpaid (that is, pay-as-you-go) is supported. That is, the parameters only supports POSTPAID_BY_HOUR."
      }
    ],
    "desc": "This API (ModifyVpnGatewayAttribute) is used to modify the attributes of VPN gateways."
  },
  "ResetVpnGatewayInternetMaxBandwidth": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "The ID of the VPN gateway instance."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps."
      }
    ],
    "desc": "This API (ResetVpnGatewayInternetMaxBandwidth) is used to adjust the bandwidth cap of VPN gateways. Currently, only configuration upgrade is supported. VPN gateways with monthly subscription must be within the validity period."
  },
  "DeleteVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      }
    ],
    "desc": "This API (DeleteVpc) is used to delete VPCs.\n* Before deleting a VPC, ensure that the VPC contains no resources, including CVMs, cloud databases, NoSQL databases, VPN gateways, direct connect gateways, load balancers, peering connections, and basic network devices that are linked to the VPC.\n* The deletion of VPCs is irreversible. Proceed with caution."
  },
  "DescribeSubnets": {
    "params": [
      {
        "name": "SubnetIds",
        "desc": "Queries the ID of the subnet instance, such as `subnet-pxir56ns`. Each request can have a maximum of 100 instances. `SubnetIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter condition. `SubnetIds` and `Filters` cannot be specified at the same time.\n<li>subnet-id - String - (Filter condition) Subnet instance name.</li>\n<li>vpc-id - String - (Filter condition) VPC instance ID, such as `vpc-f49l6u0z`.</li>\n<li>cidr-block - String - (Filter condition) The subnet IP range, such as 192.168.1.0.</li>\n<li>is-default - Boolean - (Filter condition) Whether it is the default subnet.</li>\n<li>is-remote-vpc-snat - Boolean - (Filter condition) Whether it is a VPC SNAT address pool subnet.</li>\n<li>subnet-name - String - (Filter condition) Subnet name.</li>\n<li>zone - String - (Filter condition) Availability zone.</li>\n<li>tag-key - String - Required: No - (Filter condition) Filter by tag key.</li>\n<li>tag:tag-key - String - Required: No - (Filter condition) Filter by tag key-value pair. The tag-key is replaced with the specific tag key. For usage, refer to case 2.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeSubnets) is used to query the list of subnets."
  },
  "CreateCcn": {
    "params": [
      {
        "name": "CcnName",
        "desc": "The name of the CCN. The maximum length is 60 characters."
      },
      {
        "name": "CcnDescription",
        "desc": "The description of the CCN. The maximum length is 100 characters."
      },
      {
        "name": "QosLevel",
        "desc": "CCN service quality, 'PT': Platinum, 'AU': Gold, 'AG': Silver. The default is ‘AU’."
      },
      {
        "name": "InstanceChargeType",
        "desc": "The billing method. POSTPAID: postpaid by traffic. Default: POSTPAID."
      },
      {
        "name": "BandwidthLimitType",
        "desc": "The bandwidth limit type. OUTER_REGION_LIMIT: regional outbound limit. INTER_REGION_LIMIT: inter-regional limit. Default: OUTER_REGION_LIMIT."
      }
    ],
    "desc": "This API (CreateCcn) is used to create a Cloud Connect Network (CCN).<br />\nEach account can only create a limited number of CCN instances. For more information, see the product documentation. If you need to create more instances, please contact the online customer service."
  },
  "ModifyVpnConnectionAttribute": {
    "params": [
      {
        "name": "VpnConnectionId",
        "desc": "The ID of the VPN tunnel instance, such as `vpnx-f49l6u0z`."
      },
      {
        "name": "VpnConnectionName",
        "desc": "VPN tunnel can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "PreShareKey",
        "desc": "The pre-shared key."
      },
      {
        "name": "SecurityPolicyDatabases",
        "desc": "The SPD policy group, for example: {\"10.0.0.5/24\":[\"172.123.10.5/16\"]}. 10.0.0.5/24 is the VPC internal IP range, and 172.123.10.5/16 is the IDC IP range. The user specifies the IP range in the VPC that can communicate with the IP range in the IDC."
      },
      {
        "name": "IKEOptionsSpecification",
        "desc": "IKE (Internet Key Exchange) configuration. IKE comes with a self-protection mechanism. The network security protocol is configured by the user."
      },
      {
        "name": "IPSECOptionsSpecification",
        "desc": "IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud."
      }
    ],
    "desc": "This API (ModifyVpnConnectionAttribute) is used to modify VPN tunnels."
  },
  "DescribeSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. It can be obtained through `DescribeSecurityGroups`. Each request can have a maximum of 100 instances. `SecurityGroupIds` and `Filters` cannot be specified at the same time."
      },
      {
        "name": "Filters",
        "desc": "Filter conditions. `SecurityGroupIds` and `Filters` cannot be specified at the same time.\n<li>security-group-id - String - (Filter condition) The security group ID.</li>\n<li>project-id - Integer - (Filter condition) The project ID.</li>\n<li>security-group-name - String - (Filter condition) The security group name.</li>\n<li>tag-key - String - Required: no - (Filter condition) Filters by tag key. For more information, see Example 2.</li>\n<li> `tag:tag-key` - String - Required: no - (Filter condition) Filters by tag key pair. For this parameter, `tag-key` will be replaced with a specific tag key. For more information, see Example 3.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset."
      },
      {
        "name": "Limit",
        "desc": "The returned quantity."
      }
    ],
    "desc": "This API (DescribeSecurityGroups) is used to query security groups."
  },
  "CreateVpnGateway": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "VpnGatewayName",
        "desc": "The VPN gateway name. The maximum length is 60 bytes."
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "The public network bandwidth configuration. Available bandwidth specifications: 5, 10, 20, 50, and 100. Unit: Mbps"
      },
      {
        "name": "InstanceChargeType",
        "desc": "The VPN gateway billing mode. PREPAID: prepaid means monthly subscription. POSTPAID_BY_HOUR: postpaid means pay-as-you-go. Default: POSTPAID_BY_HOUR. If prepaid mode is specified, the `InstanceChargePrepaid` parameter must be entered."
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "Parameter settings for prepaid billing mode, also known as monthly subscription. This parameter can specify the purchase period and other attributes such as auto-renewal. This parameter is mandatory for prepaid instances."
      },
      {
        "name": "Zone",
        "desc": "The availability zone, such as `ap-guangzhou-2`."
      }
    ],
    "desc": "This API (CreateVpnGateway) is used to create a VPN gateway."
  },
  "ModifyPrivateIpAddressesAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The specified private IP information."
      }
    ],
    "desc": "This API (ModifyPrivateIpAddressesAttribute) is used to modify the private IP attributes of an ENI."
  },
  "DescribeClassicLinkInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>vpc-id - String - (Filter condition) The VPC instance ID.</li>\n<li>vm-ip - String - (Filter condition) The IP address of the CVM on the basic network.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "The returned quantity"
      }
    ],
    "desc": "This API (DescribeClassicLinkInstances) is used to query the Classiclink instances list."
  },
  "DetachClassicLinkVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The ID of the VPC instance. You can obtain the parameter value from the VpcId field in the returned result of DescribeVpcs API."
      },
      {
        "name": "InstanceIds",
        "desc": "Queries the ID of the CVM instance, such as `ins-r8hr2upy`."
      }
    ],
    "desc": "This API (DetachClassicLinkVpc) is used to delete a Classiclink."
  },
  "SetCcnRegionBandwidthLimits": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "CcnRegionBandwidthLimits",
        "desc": "The outbound bandwidth cap of each CCN region."
      }
    ],
    "desc": "This API (SetCcnRegionBandwidthLimits) is used to set the outbound bandwidth cap for CCNs in each region. This API can only set the outbound bandwidth cap for regions in the network instances that have already been associated."
  },
  "CreateHaVip": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the VPC to which the `HAVIP` belongs."
      },
      {
        "name": "SubnetId",
        "desc": "The `ID` of the subnet to which the `HAVIP` belongs."
      },
      {
        "name": "HaVipName",
        "desc": "The name of the `HAVIP`."
      },
      {
        "name": "Vip",
        "desc": "The specified virtual IP address, which must be within the IP range of the `VPC` and not in use. It will be automatically assigned if not specified."
      }
    ],
    "desc": "This API (CreateHaVip) is used to create a highly available virtual IP (HAVIP)"
  },
  "MigrateNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "The ID of the ENI instance, such as `eni-m6dyj72l`."
      },
      {
        "name": "SourceInstanceId",
        "desc": "The ID of the CVM bound to the ENI, such as `ins-r8hr2upy`."
      },
      {
        "name": "DestinationInstanceId",
        "desc": "ID of the destination CVM instance to be migrated."
      }
    ],
    "desc": "This API (MigrateNetworkInterface) is used to migrate ENIs."
  },
  "ReleaseAddresses": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "The unique ID list of the EIP. The unique ID of an EIP is as follows: `eip-11112222`."
      }
    ],
    "desc": "This API (ReleaseAddresses) is used to release one or multiple [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* This operation is irreversible. Once you release an EIP, the IP address associated with the EIP no longer belongs to you.\n* Only EIPs in UNBIND status can be released."
  },
  "EnableCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "RouteIds",
        "desc": "The unique ID of the CCN routing policy, such as `ccnr-f49l6u0z`."
      }
    ],
    "desc": "This API (EnableCcnRoutes) is used to enable CCN routes that are already added.<br />\nThis API is used to verify whether there will be conflict with an existing route after a CCN route is enabled. If there is a conflict, the route will not be enabled, and the process will fail. When a conflict occurs, you must disable the conflicting route before you can enable the desired route."
  },
  "ModifyRouteTableAttribute": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "The route table instance ID, such as `rtb-azd4dt1c`."
      },
      {
        "name": "RouteTableName",
        "desc": "Route table name."
      }
    ],
    "desc": "This API (ModifyRouteTableAttribute) is used to modify the attributes of a route table."
  },
  "ModifyNetDetect": {
    "params": [
      {
        "name": "NetDetectId",
        "desc": "The ID of a network detection instance, such as `netd-12345678`."
      },
      {
        "name": "NetDetectName",
        "desc": "The name of a network detection instance. The maximum length is 60 characters."
      },
      {
        "name": "DetectDestinationIp",
        "desc": "The array of detection destination IPv4 addresses, which contains at most two IP addresses."
      },
      {
        "name": "NextHopType",
        "desc": "The type of the next hop. Currently supported types are:\nVPN: VPN gateway;\nDIRECTCONNECT: direct connect gateway;\nPEERCONNECTION: peering connection;\nNAT: NAT gateway;\nNORMAL_CVM: normal CVM."
      },
      {
        "name": "NextHopDestination",
        "desc": "The next-hop destination gateway. The value is related to NextHopType.\nIf NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.\nIf NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.\nIf NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.\nIf NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.\nIf NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12."
      },
      {
        "name": "NetDetectDescription",
        "desc": "Network detection description."
      }
    ],
    "desc": "This API (ModifyNetDetect) is used to modify network detection parameters."
  },
  "DeleteNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "The ID of the NAT gateway, such as `nat-df45454`."
      },
      {
        "name": "DestinationIpPortTranslationNatRules",
        "desc": "The port forwarding rules of the NAT gateway."
      }
    ],
    "desc": "This API (DeleteNatGatewayDestinationIpPortTranslationNatRule) is used to delete a port forwarding rule for a NAT gateway."
  },
  "CreateRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "Route table instance ID."
      },
      {
        "name": "Routes",
        "desc": "Routing policy object."
      }
    ],
    "desc": "This API (CreateRoutes) is used to create a routing policy.\n* You can create routing policies in batch for a specified route table."
  },
  "CreateNetDetect": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of a `VPC` instance, such as `vpc-12345678`."
      },
      {
        "name": "SubnetId",
        "desc": "The ID of a subnet instance, such as subnet-12345678."
      },
      {
        "name": "NetDetectName",
        "desc": "The name of a network detection instance. The maximum length is 60 characters."
      },
      {
        "name": "DetectDestinationIp",
        "desc": "The array of detection destination IPv4 addresses, which contains at most two IP addresses."
      },
      {
        "name": "NextHopType",
        "desc": "The type of the next hop. Currently supported types are:\nVPN: VPN gateway;\nDIRECTCONNECT: direct connect gateway;\nPEERCONNECTION: peering connection;\nNAT: NAT gateway;\nNORMAL_CVM: normal CVM."
      },
      {
        "name": "NextHopDestination",
        "desc": "The next-hop destination gateway. The value is related to NextHopType.\nIf NextHopType is set to VPN, the value of this parameter is the VPN gateway ID, such as vpngw-12345678.\nIf NextHopType is set to DIRECTCONNECT, the value of this parameter is the direct connect gateway ID, such as dcg-12345678.\nIf NextHopType is set to PEERCONNECTION, the value of this parameter is the peering connection ID, such as pcx-12345678.\nIf NextHopType is set to NAT, the value of this parameter is the NAT gateway ID, such as nat-12345678.\nIf NextHopType is set to NORMAL_CVM, the value of this parameter is the IPv4 address of the CVM, such as 10.0.0.12."
      },
      {
        "name": "NetDetectDescription",
        "desc": "Network detection description."
      }
    ],
    "desc": "This API is used to create a network detection instance."
  },
  "ModifyHaVipAttribute": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "The unique `ID` of the `HAVIP`, such as `havip-9o233uri`."
      },
      {
        "name": "HaVipName",
        "desc": "`HAVIP` can be named freely, but the maximum length is 60 characters."
      }
    ],
    "desc": "This API (ModifyHaVipAttribute) is used to modify HAVIP attributes."
  },
  "ResetAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "CcnUin",
        "desc": "The UIN (root account) to which the CCN belongs."
      },
      {
        "name": "Instances",
        "desc": "The list of network instances that re-apply for association."
      }
    ],
    "desc": "This API (ResetAttachCcnInstances) is used to re-apply for the association operation when the application for cross-account instance association expires."
  },
  "CreateServiceTemplateGroup": {
    "params": [
      {
        "name": "ServiceTemplateGroupName",
        "desc": "Group name of the protocol port template."
      },
      {
        "name": "ServiceTemplateIds",
        "desc": "Instance ID of the protocol port template, such as `ppm-4dw6agho`."
      }
    ],
    "desc": "This API (CreateServiceTemplateGroup) is used to create a protocol port template group."
  },
  "ModifyCcnAttribute": {
    "params": [
      {
        "name": "CcnId",
        "desc": "The CCN instance ID, such as `ccn-f49l6u0z`."
      },
      {
        "name": "CcnName",
        "desc": "The name of the CCN. The maximum length is 60 characters."
      },
      {
        "name": "CcnDescription",
        "desc": "The description of the CCN. The maximum length is 100 characters."
      }
    ],
    "desc": "This API (ModifyCcnAttribute) is used to modify CCN attributes."
  },
  "DescribeVpcPrivateIpAddresses": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the `VPC`, such as `vpc-f49l6u0z`."
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "The private `IP` address list. Each request supports a maximum of `10` batch querying."
      }
    ],
    "desc": "This API (DescribeVpcPrivateIpAddresses) is used to query the private IP information of a VPC.<br />\nThis API is used to query only the information of IP addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results."
  },
  "DescribeSecurityGroupAssociationStatistics": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "The Security instance ID, such as `sg-33ocnj9n`. It can be obtained through DescribeSecurityGroups."
      }
    ],
    "desc": "This API (DescribeSecurityGroupAssociationStatistics) is used to query statistics on the instances associated with a security group."
  },
  "UnassignIpv6SubnetCidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "The `ID` of the VPC where the subnet is located, such as `vpc-f49l6u0z`."
      },
      {
        "name": "Ipv6SubnetCidrBlocks",
        "desc": "The `IPv6` subnet IP range list."
      }
    ],
    "desc": "This API (UnassignIpv6SubnetCidrBlock) is used to release IPv6 subnet IP ranges.\nIf the subnet IP range still has occupied IPs that are not yet repossessed, the subnet IP range cannot be released."
  },
  "DescribeAddressTemplates": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>address-template-name - String - (Filter condition) IP address template name.</li>\n<li>address-template-id - String - (Filter condition) IP address template instance ID, such as `ipm-mdunqeb6`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeAddressTemplates) is used to query an IP address template."
  },
  "CreateAddressTemplate": {
    "params": [
      {
        "name": "AddressTemplateName",
        "desc": "The name of the IP address template"
      },
      {
        "name": "Addresses",
        "desc": "Address information, including IP, CIDR and IP address range."
      }
    ],
    "desc": "This API (CreateAddressTemplate) is used to create an IP address template."
  },
  "ModifyAddressAttribute": {
    "params": [
      {
        "name": "AddressId",
        "desc": "The unique ID of the EIP, such as `eip-11112222`."
      },
      {
        "name": "AddressName",
        "desc": "The EIP name after modification. The maximum length is 20 characters."
      },
      {
        "name": "EipDirectConnection",
        "desc": "Whether the set EIP is a direct connection EIP. TRUE: yes. FALSE: no. Note that this parameter is available only to users who have activated the EIP direct connection function."
      }
    ],
    "desc": "This API (ModifyAddressAttribute) is used to modify the name of an [Elastic IP](https://cloud.tencent.com/document/product/213/1941)."
  },
  "DescribeAddressTemplateGroups": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter conditions.\n<li>address-template-group-name - String - (Filter condition) IP address template group name.</li>\n<li>address-template-group-id - String - (Filter condition) IP address template group instance ID, such as `ipmg-mdunqeb6`.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset. The default value is 0."
      },
      {
        "name": "Limit",
        "desc": "Number of values to be returned. The default value is 20. Maximum is 100."
      }
    ],
    "desc": "This API (DescribeAddressTemplateGroups) is used to query an IP address template group."
  },
  "TransformAddress": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "The ID of the instance with a common public IP to be operated on, such as `ins-11112222`. You can query the instance ID by logging into the [Console](https://console.cloud.tencent.com/cvm). You can also obtain the parameter value from the `InstanceId` field in the returned result of [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) API."
      }
    ],
    "desc": "This API (TransformAddress) is used to switch common public IPs into [Elastic IPs](https://cloud.tencent.com/document/product/213/1941).\n* The platform limits the number of times that a user can unbind an EIP and reassign public IPs in each region per day. For more information, see [EIP product introduction](/document/product/213/1941)). The preceding quota can be obtained through the [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) API."
  },
  "CreateSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "The security group instance ID, such as `sg-33ocnj9n`. This can be obtained through DescribeSecurityGroups."
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "Security group policy set."
      }
    ],
    "desc": "This API is used to create security group policies (SecurityGroupPolicy).\n\n* The `Version` field indicates the version number of a security group policy, which will automatically increment by 1 every time you update the security policy, to prevent the expiration of the updated routing policies. If this field is left empty, any conflicts will be ignored.\n* The value of the `Protocol` field can be TCP, UDP, ICMP, ICMPV6, GRE, or ALL.\n* The `CidrBlock` field allows you to enter any string that conforms to the CIDR format. (More details) In a basic network, if a CidrBlock contains private IP addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.\n* The `Ipv6CidrBlock` field allows you to enter any string that conforms to the IPv6 CIDR format. (More details) In a basic network, if an Ipv6CidrBlock contains private IPv6 addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.\n* The SecurityGroupId field allows you to enter the IDs of security groups that are in the same project as the security group to be modified, including the ID of the security group itself, to represent private IP addresses of all CVMs under the security group. If this field is used, the policy will change without manual modification according to the CVM associated with the policy ID while being used to match network messages.\n* The Port field allows you to enter a single port number, or two port numbers separated by a minus sign to represent a port range, such as 80 or 8000-8010. The Port field is accepted only if the value of the Protocol field is TCP or UDP. In other words, if the value of the Protocol field is not TCP or UDP, Protocol and Port are exclusive and cannot be entered at the same time, otherwise an error will occur with the API.\n* The Action field only allows you to enter ACCEPT or DROP.\n* CidrBlock, Ipv6CidrBlock, SecurityGroupId, and AddressTemplate are exclusive and cannot be entered at the same time. Protocol + Port and ServiceTemplate are mutually exclusive and cannot be entered at the same time.\n* Only policies in one direction can be created in each request. If you need to specify the PolicyIndex parameter, the indexes of policies must be consistent."
  },
  "ResetNatGatewayConnection": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT gateway ID."
      },
      {
        "name": "MaxConcurrentConnection",
        "desc": "Concurrent connections cap of the NAT gateway, such as 1000000, 3000000, 10000000."
      }
    ],
    "desc": "This API (ResetNatGatewayConnection) is used to adjust concurrent connection cap for the NAT gateway."
  },
  "ModifyVpcAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "Security group can be named freely, but cannot exceed 60 characters."
      },
      {
        "name": "VpcName",
        "desc": "VPC can be named freely, but the maximum length is 60 characters."
      },
      {
        "name": "EnableMulticast",
        "desc": "Whether multicast is enabled. `true`: Enabled. `false`: Off."
      },
      {
        "name": "DnsServers",
        "desc": "DNS address. A maximum of 4 addresses is supported. The first one is master server by default, and the rest are slave servers."
      },
      {
        "name": "DomainName",
        "desc": "Domain name"
      }
    ],
    "desc": "This API (ModifyVpcAttribute) is used to modify VPC attributes."
  }
}