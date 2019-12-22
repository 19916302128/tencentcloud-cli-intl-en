# -*- coding: utf-8 -*-
DESC = "clb-2018-03-17"
INFO = {
  "RegisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Targets",
        "desc": "List of real servers to be bound. Array length limit: 20"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target forwarding rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target forwarding rule URL. This parameter does not take effect if LocationId is specified"
      }
    ],
    "desc": "This API (RegisterTargets) is used to bind one or more real servers to a CLB listener or layer-7 forwarding rule. Before using this API, you need to create relevant layer-4 listeners or layer-7 forwarding rules. For the former (TCP/UDP), only the listener ID needs to be specified, while for the latter (HTTP/HTTPS), the forwarding rule also needs to be specified through LocationId or Domain+Url.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "SetLoadBalancerSecurityGroups": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SecurityGroups",
        "desc": "Array of security group IDs. One CLB instance can be bound to up to 50 security groups. If you want to unbind all security groups, you do not need to pass in this parameter, or you can pass in an empty array."
      }
    ],
    "desc": "This API (SetLoadBalancerSecurityGroups) is used to bind/unbind security groups for a public network CLB instance. You can use the DescribeLoadBalancers API to query the security groups bound to a CLB instance. This API uses `set` semantics.\nDuring a binding operation, the input parameters need to be all security groups to be bound to the CLB instance (including those already bound ones and new ones).\nDuring an unbinding operation, the input parameters need to be all the security groups still bound to the CLB instance after the unbinding operation. To unbind all security groups, you can leave this parameter empty or pass in an empty array. Note: Private network CLB do not support binding security groups."
  },
  "DescribeClassicalLBListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerIds",
        "desc": "List of CLB listener IDs"
      },
      {
        "name": "Protocol",
        "desc": "CLB listening protocol. Value range: TCP, UDP, HTTP, HTTPS"
      },
      {
        "name": "ListenerPort",
        "desc": "CLB listening port. Value range: [1-65535]"
      },
      {
        "name": "Status",
        "desc": "Listener status. Value range: 0 (creating), 1 (running)"
      }
    ],
    "desc": "This API (DescribeClassicalLBListeners) is used to get the listener information of a classic CLB."
  },
  "DeleteListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "ID of the listener to be deleted"
      }
    ],
    "desc": "This API is used to delete a listener from a CLB instance (layer-4 or layer-7).\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "SetSecurityGroupForLoadbalancers": {
    "params": [
      {
        "name": "SecurityGroup",
        "desc": "Security group ID, such as sg-12345678"
      },
      {
        "name": "OperationType",
        "desc": "ADD: bind a security group;\nDEL: unbind a security group"
      },
      {
        "name": "LoadBalancerIds",
        "desc": "Array of CLB instance IDs"
      }
    ],
    "desc": "This API is used to bind or unbind a security group for multiple public network CLB instances. Note: Private network CLB do not support binding security groups."
  },
  "BatchDeregisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Targets",
        "desc": "Unbound targets"
      }
    ],
    "desc": "This API is used to unbind layer-4/layer-7 real servers in batches."
  },
  "ReplaceCertForLoadBalancers": {
    "params": [
      {
        "name": "OldCertificateId",
        "desc": "ID of the certificate to be replaced, which can be a server certificate or a client certificate."
      },
      {
        "name": "Certificate",
        "desc": "Information such as the content of the new certificate"
      }
    ],
    "desc": "This API (ReplaceCertForLoadBalancers) is used to replace the certificate associated with a CLB instance. A new certificates can be associated with a CLB only after the original certificate is disassociated from it.\nThis API supports replacing server certificates and client certificates.\nThe new certificate to be used can be specified by passing in the certificate ID. If no certificate ID is specified, relevant information such as certificate content must be passed in to create a new certificate and bind it to the CLB.\nNote: This API can only be called in the Guangzhou region; for other regions, an error will occur due to domain name resolution problems."
  },
  "CreateRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "Listener ID"
      },
      {
        "name": "Rules",
        "desc": "Information of the new forwarding rule"
      }
    ],
    "desc": "This API (CreateRule) is used to create a forwarding rule under an existing layer-7 CLB listener, where real servers must be bound to the rule instead of the listener.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "AutoRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "HTTPS:443 listener ID"
      },
      {
        "name": "Domains",
        "desc": "Domain name to be redirected under an HTTPS:443 listener"
      }
    ],
    "desc": "An HTTPS:443 listener needs to be created first, along with a forwarding rule. When this API is called, an HTTP:80 listener will be created automatically if it did not exist and a forwarding rule corresponding to `Domains` (specified in the input parameter) under the HTTPS:443 listener will also be created. After successful creation, access requests to an HTTP:80 address will be redirected to an HTTPS:443 address automatically."
  },
  "ModifyDomain": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Domain",
        "desc": "Legacy domain name under a listener."
      },
      {
        "name": "NewDomain",
        "desc": "New domain name. \tLength limit: 1-120. There are three usage formats: non-regular expression, wildcard, and regular expression. A non-regular expression can only contain letters, digits, \"-\", and \".\". In a wildcard, \"*\" can only be at the beginning or the end. A regular expressions must begin with a \"~\"."
      }
    ],
    "desc": "This API (ModifyDomain) is used to modify a domain name under a layer-7 CLB listener.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DescribeClassicalLBTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      }
    ],
    "desc": "This API (DescribeClassicalLBTargets) is used to get the real servers bound to a classic CLB."
  },
  "DeregisterTargetsFromClassicalLB": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "InstanceIds",
        "desc": "List of real server instance IDs"
      }
    ],
    "desc": "This API (DeregisterTargetsFromClassicalLB) is used to unbind real servers from a classic load balancer.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "DescribeClassicalLBHealthStatus": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      }
    ],
    "desc": "This API (DescribeClassicalLBHealthStatus) is used to get the real server health status of a classic CLB"
  },
  "ModifyListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "ListenerName",
        "desc": "New listener name"
      },
      {
        "name": "SessionExpireTime",
        "desc": "Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners."
      },
      {
        "name": "HealthCheck",
        "desc": "Health check parameter, which is applicable only to TCP/UDP/TCP_SSL listeners."
      },
      {
        "name": "Certificate",
        "desc": "Certificate information. This parameter is applicable only to HTTPS/TCP_SSL listeners."
      },
      {
        "name": "Scheduler",
        "desc": "Forwarding method of a listener. Value range: WRR, LEAST_CONN.\nThey represent weighted round robin and least connections, respectively. Default value: WRR."
      },
      {
        "name": "SniSwitch",
        "desc": "Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners. Note: The SNI feature can be enabled but cannot be disabled once enabled."
      }
    ],
    "desc": "This API (ModifyListener) is used to modify the attributes of a CLB listener, such as listener name, health check parameter, certificate information, and forwarding policy.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DeleteLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "Array of IDs of the CLB instances to be deleted. Array length limit: 20"
      }
    ],
    "desc": "This API (DeleteLoadBalancer) is used to delete one or more specified CLB instances.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "ModifyDomainAttributes": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Domain",
        "desc": "Domain name, which must be under a created forwarding rule."
      },
      {
        "name": "NewDomain",
        "desc": "New domain name"
      },
      {
        "name": "Certificate",
        "desc": "Domain name certificate information. Note: This is only applicable to SNI-enabled listeners."
      },
      {
        "name": "Http2",
        "desc": "Whether to enable HTTP/2. Note: HTTP/2 can be enabled only for HTTPS domain names."
      },
      {
        "name": "DefaultServer",
        "desc": "Whether to set this domain name as the default domain name. Note: Only one default domain name can be set under one listener."
      }
    ],
    "desc": "This API is used to modify the domain name-level attributes of a layer-7 listener's forwarding rule, such as modifying the domain name, changing the DefaultServer, enabling/disabling HTTP/2, and modifying certificates.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "DeleteRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "LocationIds",
        "desc": "Array of IDs of the forwarding rules to be deleted"
      },
      {
        "name": "Domain",
        "desc": "Domain name of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified"
      },
      {
        "name": "Url",
        "desc": "Forwarding path of the forwarding rule to be deleted. This parameter does not take effect if LocationIds is specified"
      }
    ],
    "desc": "This API (DeleteRule) is used to delete a forwarding rule under a layer-7 CLB instance listener\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DescribeLoadBalancers": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "CLB instance ID."
      },
      {
        "name": "LoadBalancerType",
        "desc": "CLB instance network type:\nOPEN: public network; INTERNAL: private network."
      },
      {
        "name": "Forward",
        "desc": "CLB instance type. 1: generic CLB instance; 0: classic CLB instance"
      },
      {
        "name": "LoadBalancerName",
        "desc": "CLB instance name."
      },
      {
        "name": "Domain",
        "desc": "Domain name assigned to a CLB instance by Tencent Cloud. This parameter is meaningful only for the public network classic CLB."
      },
      {
        "name": "LoadBalancerVips",
        "desc": "VIP address of a CLB instance (there can be multiple addresses)"
      },
      {
        "name": "BackendPublicIps",
        "desc": "Public IP of the real server bound to a CLB."
      },
      {
        "name": "BackendPrivateIps",
        "desc": "Private IP of the real server bound to a CLB."
      },
      {
        "name": "Offset",
        "desc": "Data offset. Default value: 0."
      },
      {
        "name": "Limit",
        "desc": "Number of CLB instances to be returned. Default value: 20."
      },
      {
        "name": "OrderBy",
        "desc": "Sort by parameter. Value range: LoadBalancerName, CreateTime, Domain, LoadBalancerType."
      },
      {
        "name": "OrderType",
        "desc": "1: reverse; 0: sequential. Default value: reverse by creation time |"
      },
      {
        "name": "SearchKey",
        "desc": "Search field which fuzzy matches name, domain name, or VIP."
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API."
      },
      {
        "name": "WithRs",
        "desc": "Whether a CLB instance is bound to a real server. 0: no; 1: yes; -1: query all."
      },
      {
        "name": "VpcId",
        "desc": "VPC where a CLB instance resides, such as vpc-bhqkbhdx.\nBasic network does not support queries by VpcId."
      },
      {
        "name": "SecurityGroup",
        "desc": "Security group ID, such as sg-m1cc9123"
      },
      {
        "name": "MasterZone",
        "desc": "Master AZ, such as \"100001\" (Guangzhou Zone 1)"
      }
    ],
    "desc": "This API is used to query the list of CLB instances.\n"
  },
  "DescribeListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerIds",
        "desc": "Array of IDs of the CLB listeners to be queried"
      },
      {
        "name": "Protocol",
        "desc": "Type of the listener protocol to be queried. Value range: TCP, UDP, HTTP, HTTPS, TCP_SSL"
      },
      {
        "name": "Port",
        "desc": "Port of the listener to be queried"
      }
    ],
    "desc": "This API (DescribeListeners) is used to get the list of listeners by CLB IDs, listener protocol, or port. If no filter is specified, the default number (20) of listeners for the instance will be returned."
  },
  "CreateListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Ports",
        "desc": "Specifies for which ports to create listeners. Each port corresponds to a new listener"
      },
      {
        "name": "Protocol",
        "desc": "Listener protocol: TCP, UDP, HTTP, HTTPS, or TCP_SSL (which is currently in beta test. If you want to use it, please submit a ticket for application)"
      },
      {
        "name": "ListenerNames",
        "desc": "List of names of the listeners to be created. The array of names and array of ports are in one-to-one correspondence. If you do not want to name them now, you do not need to provide this parameter."
      },
      {
        "name": "HealthCheck",
        "desc": "Health check parameter, which is applicable only to TCP/UDP/TCP_SSL listeners"
      },
      {
        "name": "Certificate",
        "desc": "Certificate information. This parameter is applicable only to HTTPS/TCP_SSL listeners."
      },
      {
        "name": "SessionExpireTime",
        "desc": "Session persistence time in seconds. Value range: 30-3,600. The default value is 0, indicating that session persistence is not enabled. This parameter is applicable only to TCP/UDP listeners."
      },
      {
        "name": "Scheduler",
        "desc": "Forwarding method of a listener. Value range: WRR, LEAST_CONN.\nThey represent weighted round robin and least connections, respectively. Default value: WRR. This parameter is applicable only to TCP/UDP/TCP_SSL listeners."
      },
      {
        "name": "SniSwitch",
        "desc": "Whether to enable the SNI feature. This parameter is applicable only to HTTPS listeners"
      }
    ],
    "desc": "This API is used to create a listener for a CLB instance.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "BatchRegisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Targets",
        "desc": "Binding target"
      }
    ],
    "desc": "This API is used to bind CVM instances or ENIs in batches. It supports cross-region binding and only layer-4 (TCP/UDP) protocols."
  },
  "ModifyTargetWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target rule URL. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Targets",
        "desc": "List of real servers for which to modify the weight"
      },
      {
        "name": "Weight",
        "desc": "New forwarding weight of a real server. Value range: 0-100. Default value: 10. If the Targets.Weight parameter is set, this parameter will not take effect."
      }
    ],
    "desc": "This API (ModifyTargetWeight) is used to modify the forwarding weight of a real server bound to a CLB instance.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "TaskId",
        "desc": "Request ID, i.e., the RequestId parameter returned by the API"
      }
    ],
    "desc": "This API is used to query the execution status of an async task. After non-query APIs (used to create/delete CLB instances, listeners, or rules or to bind/unbind real servers) are called successfully, this API needs to be used to query whether the task is successful."
  },
  "ModifyRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "LocationId",
        "desc": "ID of the forwarding rule to be modified."
      },
      {
        "name": "Url",
        "desc": "New forwarding path of the forwarding rule. This parameter is not required if the URL does not need to be modified"
      },
      {
        "name": "HealthCheck",
        "desc": "Health check information"
      },
      {
        "name": "Scheduler",
        "desc": "Request forwarding method of the rule. Value range: WRR, LEAST_CONN, IP_HASH\nThey represent weighted round robin, least connections, and IP hash, respectively. Default value: WRR."
      },
      {
        "name": "SessionExpireTime",
        "desc": "Session persistence time"
      },
      {
        "name": "ForwardType",
        "desc": "Forwarding protocol between CLB instance and real server. Value range: HTTP, HTTPS. Default value: HTTP"
      }
    ],
    "desc": "This API (ModifyRule) is used to modify the attributes of a forwarding rule under a layer-7 CLB listener, such as forwarding path, health check attribute, and forwarding policy.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DescribeTargetHealth": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "List of IDs of CLB instances to be queried"
      }
    ],
    "desc": "This API (DescribeTargetHealth) is used to query the health check result of a real server of a CLB instance."
  },
  "DescribeTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerIds",
        "desc": "List of listener IDs"
      },
      {
        "name": "Protocol",
        "desc": "Listener protocol type"
      },
      {
        "name": "Port",
        "desc": "Listener port"
      }
    ],
    "desc": "This API (DescribeTargets) is used to query the list of real servers bound to some listeners of a CLB instance."
  },
  "DescribeRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SourceListenerIds",
        "desc": "Array of CLB listener IDs"
      },
      {
        "name": "SourceLocationIds",
        "desc": "Array of CLB forwarding rules"
      }
    ],
    "desc": "This API (DescribeRewrite) is used to query the redirection relationship between the forwarding rules of a CLB instance by instance ID. If no listener ID or forwarding rule ID is specified, all redirection relationships in the instance will be returned."
  },
  "RegisterTargetsWithClassicalLB": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "Targets",
        "desc": "Real server information"
      }
    ],
    "desc": "This API (RegisterTargetsWithClassicalLB) is used to bind real servers to a classic CLB.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful."
  },
  "ModifyTargetPort": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ListenerId",
        "desc": "CLB listener ID"
      },
      {
        "name": "Targets",
        "desc": "List of real servers for which to modify the ports"
      },
      {
        "name": "NewPort",
        "desc": "New port of the real server bound to a listener or forwarding rule"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID. When binding a real server to a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target rule URL. This parameter does not take effect if LocationId is specified"
      }
    ],
    "desc": "This API (ModifyTargetPort) is used to modify the port of a real server bound to a listener.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DeregisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID in the format of lb-12345678"
      },
      {
        "name": "ListenerId",
        "desc": "Listener ID in the format of lbl-12345678"
      },
      {
        "name": "Targets",
        "desc": "List of real servers to be unbound. Array length limit: 20"
      },
      {
        "name": "LocationId",
        "desc": "Forwarding rule ID in the format of loc-12345678. When unbinding a server from a layer-7 forwarding rule, you must provide either this parameter or Domain+Url"
      },
      {
        "name": "Domain",
        "desc": "Target rule domain name. This parameter does not take effect if LocationId is specified"
      },
      {
        "name": "Url",
        "desc": "Target rule URL. This parameter does not take effect if LocationId is specified"
      }
    ],
    "desc": "This API (DeregisterTargets) is used to unbind one or more real servers from a CLB listener or forwarding rule. For layer-4 listeners, only the listener ID needs to be specified. For layer-7 listeners, the forwarding rule also needs to be specified through LocationId or Domain+Url.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "ModifyLoadBalancerAttributes": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "Unique CLB ID"
      },
      {
        "name": "LoadBalancerName",
        "desc": "CLB instance name"
      },
      {
        "name": "TargetRegionInfo",
        "desc": "Region information of the real server bound to a CLB."
      },
      {
        "name": "InternetChargeInfo",
        "desc": "Network billing parameter. Note: The maximum outbound bandwidth can be modified, but the network billing method cannot be modified."
      }
    ],
    "desc": "This API is used to modify the attributes of a CLB instance such as name and cross-region attributes."
  },
  "DescribeClassicalLBByInstanceId": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "List of real server IDs."
      }
    ],
    "desc": "This API (DescribeClassicalLBByInstanceId) is used to get the list of classic CLB IDs through the real server instance ID."
  },
  "BatchModifyTargetWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "ModifyList",
        "desc": "List of weights to be modified in batches"
      }
    ],
    "desc": "This API (BatchModifyTargetWeight) is used to batch modify the forwarding weights of real servers bound to a listener. Currently, it only supports HTTP/HTTPS listeners.\nThis is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful."
  },
  "DeleteRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SourceListenerId",
        "desc": "Source listener ID"
      },
      {
        "name": "TargetListenerId",
        "desc": "Target listener ID"
      },
      {
        "name": "RewriteInfos",
        "desc": "Redirection relationship between forwarding rules"
      }
    ],
    "desc": "This API (DeleteRewrite) is used to delete the redirection relationship between the specified forwarding rules."
  },
  "CreateLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerType",
        "desc": "CLB instance network type:\nOPEN: public network; INTERNAL: private network."
      },
      {
        "name": "Forward",
        "desc": "CLB instance type. 1: generic CLB instance. Currently, only 1 can be passed in"
      },
      {
        "name": "LoadBalancerName",
        "desc": "CLB instance name, which takes effect only when an instance is created. Rule: 1-50 letters, digits, dashes (-), or underscores (_).\nNote: If this name is the same as the name of an existing CLB instance in the system, the system will automatically generate a name for this newly created instance."
      },
      {
        "name": "VpcId",
        "desc": "Network ID of the backend target server of CLB, which can be obtained through the DescribeVpcEx API. If this parameter is not passed in, it will default to a basic network (\"0\")."
      },
      {
        "name": "SubnetId",
        "desc": "A subnet ID must be specified when you purchase a private network CLB instance in a VPC, and the VIP of this instance will be generated in this subnet. This parameter is not supported in other cases."
      },
      {
        "name": "ProjectId",
        "desc": "ID of the project to which a CLB instance belongs, which can be obtained through the DescribeProject API. If this parameter is not passed in, the default project will be used."
      },
      {
        "name": "AddressIPVersion",
        "desc": "IP version. Value range: IPv4, IPv6. Default value: IPv4. This parameter is applicable only to public network CLB."
      },
      {
        "name": "Number",
        "desc": "Number of CLBs to be created. Default value: 1."
      },
      {
        "name": "MasterZoneId",
        "desc": "Sets the primary AZ ID for cross-AZ disaster recovery, such as 100001 or ap-guangzhou-1, which is applicable only to public network CLB.\nNote: A primary AZ carries traffic, while a secondary AZ does not carry traffic by default and will be used only if the primary AZ becomes unavailable. The platform will automatically select the optimal secondary AZ. The list of primary AZs in a specific region can be queried through the DescribeMasterZones API."
      },
      {
        "name": "ZoneId",
        "desc": "Specifies an AZ ID for creating a CLB instance, such as ap-guangzhou-1, which is applicable only to public network CLB."
      },
      {
        "name": "InternetAccessible",
        "desc": "CLB network billing method. This parameter is applicable only to public network CLB, and takes effect only for users whose bandwidth is managed in IP and CLB."
      },
      {
        "name": "Tags",
        "desc": "Tags a CLB instance when purchasing it"
      }
    ],
    "desc": "This API (CreateLoadBalancer) is used to create a CLB instance. To use the CLB service, you first need to purchase one or more instances. After this API is called successfully, a unique instance ID will be returned. There are two types of instances: public network and private network. For more information, see the product types in the product documentation.\nNote: (1) To apply for a CLB instance in the specified AZ and cross-AZ disaster recovery, please [submit a ticket](https://console.cloud.tencent.com/workorder/category); (2) Currently, IPv6 is supported only in Beijing, Shanghai, and Guangzhou regions.\nThis is an async API. After it is returned successfully, you can call the DescribeLoadBalancers API to query the status of the instance (such as creating and normal) to check whether it is successfully created."
  },
  "ManualRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "CLB instance ID"
      },
      {
        "name": "SourceListenerId",
        "desc": "Source listener ID"
      },
      {
        "name": "TargetListenerId",
        "desc": "Target listener ID"
      },
      {
        "name": "RewriteInfos",
        "desc": "Redirection relationship between forwarding rules"
      }
    ],
    "desc": "After the original access address and the address to be redirected are configured manually, the system will automatically redirect requests made to the original access address to the target address of the corresponding path. Multiple paths can be configured as a redirection policy under one domain name to achieve automatic redirection between HTTP and HTTPS. A redirection policy should meet the following rules: if A has already been redirected to B, then it cannot be redirected to C (unless the original redirection relationship is deleted and a new one is created), and B cannot be redirected to any other addresses."
  }
}