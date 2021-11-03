#!/usr/bin/env python3
data = """
 01 
03/22 08:51:01 INFO   :.main: *************** RSVP Agent started ***************
 02 
03/22 08:51:01 INFO   :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf
03/22 08:51:01 INFO   :.main: Using log level 511
03/22 08:51:01 INFO   :..settcpimage: Get TCP images rc - EDC8112I Operation not supported on socket.
 03 
03/22 08:51:01 INFO   :..settcpimage: Associate with TCP/IP image name = TCPCS
03/22 08:51:02 INFO   :..reg_process: registering process with the system
03/22 08:51:02 INFO   :..reg_process: attempt OS/390 registration
03/22 08:51:02 INFO   :..reg_process: return from registration rc=0
 04 
03/22 08:51:06 TRACE  :...read_physical_netif: Home list entries returned = 7
03/22 08:51:06 INFO   :...read_physical_netif: index #0, interface VLINK1 has address 129.1.1.1, ifidx 0
03/22 08:51:06 INFO   :...read_physical_netif: index #1, interface TR1 has address 9.37.65.139, ifidx 1
03/22 08:51:06 INFO   :...read_physical_netif: index #2, interface LINK11 has address 9.67.100.1, ifidx 2
03/22 08:51:06 INFO   :...read_physical_netif: index #3, interface LINK12 has address 9.67.101.1, ifidx 3
03/22 08:51:06 INFO   :...read_physical_netif: index #4, interface CTCD0 has address 9.67.116.98, ifidx 4
03/22 08:51:06 INFO   :...read_physical_netif: index #5, interface CTCD2 has address 9.67.117.98, ifidx 5
03/22 08:51:06 INFO   :...read_physical_netif: index #6, interface LOOPBACK has address 127.0.0.1, ifidx 0
03/22 08:51:06 INFO   :....mailslot_create: creating mailslot for timer
03/22 08:51:06 INFO   :...mailbox_register: mailbox allocated for timer
 05 
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
 06 
03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE  :..entity_initialize: interface 129.1.1.1, entity for rsvp allocated and initialized
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE  :..entity_initialize: interface 9.37.65.139, entity for rsvp allocated and 
initialized
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.100.1, entity for rsvp allocated and initialized
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.101.1, entity for rsvp allocated and initialized
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.116.98, entity for rsvp allocated and 
initialized
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.117.98, entity for rsvp allocated and 
initialized
Kopieren


03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp
03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP
03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp
03/22 08:51:06 TRACE  :..entity_initialize: interface 127.0.0.1, entity for rsvp allocated and initialized
03/22 08:51:06 INFO   :......mailslot_create: creating socket for querying route
03/22 08:51:06 INFO   :.....mailbox_register: no mailbox necessary for forward
03/22 08:51:06 INFO   :......mailslot_create: creating mailslot for route engine - informational socket
03/22 08:51:06 TRACE  :......mailslot_create: ready to accept informational socket connection
03/22 08:51:11 INFO   :.....mailbox_register: mailbox allocated for route
03/22 08:51:11 INFO   :.....mailslot_create: creating socket for traffic control module
03/22 08:51:11 INFO   :....mailbox_register: no mailbox necessary for traffic-control
03/22 08:51:11 INFO   :....mailslot_create: creating mailslot for RSVP client API
03/22 08:51:11 INFO   :...mailbox_register: mailbox allocated for rsvp-api
03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for terminate
03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for terminate
03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for dump
03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for dump
03/22 08:51:11 INFO   :...mailslot_create: creating mailslot for (broken) pipe
03/22 08:51:11 INFO   :..mailbox_register: mailbox allocated for pipe
 07 
03/22 08:51:11 INFO   :.main: rsvpd initialization complete
 08 
03/22 08:52:50 INFO   :......rsvp_api_open: accepted a new connection for rapi
03/22 08:52:50 INFO   :.......mailbox_register: mailbox allocated for mailbox
03/22 08:52:50 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 does not exist
 09 
03/22 08:52:50 EVENT  :.....api_reader: api request SESSION
 10 
03/22 08:52:50 TRACE  :......rsvp_event_establishSession: local node will send
03/22 08:52:50 INFO   :........router_forward_getOI: Ioctl to get route entry successful
03/22 08:52:50 TRACE  :........router_forward_getOI:         source address:   9.67.116.98
03/22 08:52:50 TRACE  :........router_forward_getOI:         out inf:   9.67.116.98
03/22 08:52:50 TRACE  :........router_forward_getOI:         gateway:   0.0.0.0
03/22 08:52:50 TRACE  :........router_forward_getOI:         route handle:   7f5251c8
 11 
03/22 08:52:50 TRACE  :.......event_establishSessionSend: found outgoing if=9.67.116.98 through 
forward engine
03/22 08:52:50 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
 12 
03/22 08:52:50 EVENT  :.....api_reader: api request SENDER
 13 
03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  Entering
 
03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  papiLogFunc = 98681F0 papiUserValue = 0
 
03/22 08:52:50 INFO   :.......init_policyAPI: papi_debug:  Exiting
 
03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  Entering
 
03/22 08:52:50 INFO   :.......init_policyAPI: open_socket:  Entering
 
03/22 08:52:50 INFO   :.......init_policyAPI: open_socket:  Exiting
 
03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  ApiHandle = 98BDFB0,  connfd = 22
 
03/22 08:52:50 INFO   :.......init_policyAPI: APIInitialize:  Exiting
 
03/22 08:52:50 INFO   :.......init_policyAPI: RegisterWithPolicyAPI:  Entering
Kopieren


03/22 08:52:50 INFO   :.......init_policyAPI: RegisterWithPolicyAPI:  Writing to socket = 22
 
03/22 08:52:50 INFO   :.......init_policyAPI: ReadBuffer:  Entering
 
03/22 08:52:51 INFO   :.......init_policyAPI: ReadBuffer:  Exiting
 
03/22 08:52:51 INFO   :.......init_policyAPI: RegisterWithPolicyAPI:  Exiting
03/22 08:52:51 INFO   :.......init_policyAPI: Policy API initialized
03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindActionName:  Entering
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Entering
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Exiting
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindActionName:  Result = 0
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindActionName:  Exiting
 
 14 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: found action name CLCat2 for 
flow[sess=9.67.116.99:1047:6,source=9.67.116.98:8000]
03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindServiceDetailsOnActName:  Entering
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Entering
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: ReadBuffer:  Exiting
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindServiceDetailsOnActName:  Result = 0
 
03/22 08:52:51 INFO   :......rpapi_getPolicyData: RSVPFindServiceDetailsOnActName:  Exiting
 
03/22 08:52:51 INFO   :.....api_reader: appl chose service type 1
03/22 08:52:51 INFO   :......rpapi_getSpecData: RSVPGetTSpec:  Entering
 
03/22 08:52:51 INFO   :......rpapi_getSpecData: RSVPGetTSpec:  Result = 0
 
03/22 08:52:51 INFO   :......rpapi_getSpecData: RSVPGetTSpec:  Exiting
 
03/22 08:52:51 TRACE  :.....api_reader: new service=1, old service=0
03/22 08:52:51 INFO   :.......rsvp_flow_stateMachine: state SESSIONED, event PATHDELTA
 15 
03/22 08:52:51 TRACE  :........rsvp_action_nHop: constructing a PATH
03/22 08:52:51 TRACE  :........flow_timer_start: started T1
 16 
03/22 08:52:51 TRACE  :.......rsvp_flow_stateMachine: entering state PATHED
03/22 08:52:51 TRACE  :........mailslot_send: sending to (9.67.116.99:0)
03/22 08:52:51 TRACE  :........mailslot_send: sending to (9.67.116.99:1698)
 17 
03/22 08:52:51 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98
03/22 08:52:51 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84
03/22 08:52:51 TRACE  :.......rsvp_parse_objects: STYLE is WF
03/22 08:52:51 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0
03/22 08:52:51 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
03/22 08:52:51 INFO   :.......rsvp_flow_stateMachine: state PATHED, event RESVDELTA
 18 
03/22 08:52:51 TRACE  :........traffic_action_oif: is to install filter
03/22 08:52:51 INFO   :.........qosmgr_request: src-9.67.116.98:8000 dst-9.67.116.99:1047 proto-6 
rthdl-7f5251c8
 19 
03/22 08:52:51 INFO   :.........qosmgr_request: [CL r=90000 b=6000 p=110000 m=1024 M=2048]
03/22 08:52:51 INFO   :.........qosmgr_request: Ioctl to add reservation successful
03/22 08:52:51 INFO   :..........rpapi_Reg_UnregFlow: RSVPPutActionName:  Entering
Kopieren


03/22 08:52:51 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Entering
 
03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Exiting
 
03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: RSVPPutActionName:  Result = 0
 
03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: RSVPPutActionName:  Exiting
 
03/22 08:52:52 INFO   :..........rpapi_Reg_UnregFlow: flow[sess=9.67.116.99:1047:6, 
source=9.67.116.98:8000] registered with CLCat2
03/22 08:52:52 EVENT  :..........qosmgr_response: RESVRESP from qosmgr, reason=0, qoshandle=8b671d0
03/22 08:52:52 INFO   :..........qosmgr_response: src-9.67.116.98:8000 dst-9.67.116.99:1047 proto-6
03/22 08:52:52 TRACE  :...........traffic_reader: tc response msg=1, status=1
03/22 08:52:52 INFO   :...........traffic_reader: Reservation req successful[session=9.67.116.99:1047:6,
source=9.67.116.98:8000, qoshd=8b671d0]
 20 
03/22 08:52:52 TRACE  :........api_action_sender: constructing a RESV
03/22 08:52:52 TRACE  :........flow_timer_stop: stopped T1
03/22 08:52:52 TRACE  :........flow_timer_stop: Stop T4
03/22 08:52:52 TRACE  :........flow_timer_start: started T1
03/22 08:52:52 TRACE  :........flow_timer_start: Start T4
 21 
03/22 08:52:52 TRACE  :.......rsvp_flow_stateMachine: entering state RESVED
 22 
03/22 08:53:07 EVENT  :..mailslot_sitter: process received signal SIGALRM
03/22 08:53:07 TRACE  :.....event_timerT1_expire: T1 expired
03/22 08:53:07 INFO   :......router_forward_getOI: Ioctl to query route entry successful
03/22 08:53:07 TRACE  :......router_forward_getOI:         source address:   9.67.116.98
03/22 08:53:07 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98
03/22 08:53:07 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0
03/22 08:53:07 TRACE  :......router_forward_getOI:         route handle:   7f5251c8
03/22 08:53:07 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT
03/22 08:53:07 TRACE  :.......rsvp_action_nHop: constructing a PATH
03/22 08:53:07 TRACE  :.......flow_timer_start: started T1
03/22 08:53:07 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:53:07 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)
 23 
03/22 08:53:22 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98
03/22 08:53:22 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84
03/22 08:53:22 TRACE  :.......rsvp_parse_objects: STYLE is WF
03/22 08:53:22 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0
03/22 08:53:22 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
03/22 08:53:22 INFO   :.......rsvp_flow_stateMachine: state RESVED, event RESV
03/22 08:53:22 TRACE  :........flow_timer_stop: Stop T4
03/22 08:53:22 TRACE  :........flow_timer_start: Start T4
03/22 08:53:22 TRACE  :.......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:53:22 EVENT  :..mailslot_sitter: process received signal SIGALRM
03/22 08:53:22 TRACE  :.....event_timerT1_expire: T1 expired
03/22 08:53:22 INFO   :......router_forward_getOI: Ioctl to query route entry successful
03/22 08:53:22 TRACE  :......router_forward_getOI:         source address:   9.67.116.98
03/22 08:53:22 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98
03/22 08:53:22 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0
03/22 08:53:22 TRACE  :......router_forward_getOI:         route handle:   7f5251c8
03/22 08:53:22 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT
03/22 08:53:22 TRACE  :.......rsvp_action_nHop: constructing a PATH
03/22 08:53:22 TRACE  :.......flow_timer_start: started T1
03/22 08:53:22 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:53:22 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)
03/22 08:53:38 EVENT  :..mailslot_sitter: process received signal SIGALRM
03/22 08:53:38 TRACE  :.....event_timerT1_expire: T1 expired
03/22 08:53:38 INFO   :......router_forward_getOI: Ioctl to query route entry successful
Kopieren


03/22 08:53:38 TRACE  :......router_forward_getOI:         source address:   9.67.116.98
03/22 08:53:38 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98
03/22 08:53:38 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0
03/22 08:53:38 TRACE  :......router_forward_getOI:         route handle:   7f5251c8
03/22 08:53:38 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT
03/22 08:53:38 TRACE  :.......rsvp_action_nHop: constructing a PATH
03/22 08:53:38 TRACE  :.......flow_timer_start: started T1
03/22 08:53:38 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:53:38 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)
03/22 08:53:52 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98
03/22 08:53:52 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84
03/22 08:53:52 TRACE  :.......rsvp_parse_objects: STYLE is WF
03/22 08:53:52 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0
03/22 08:53:52 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
03/22 08:53:52 INFO   :.......rsvp_flow_stateMachine: state RESVED, event RESV
03/22 08:53:52 TRACE  :........flow_timer_stop: Stop T4
03/22 08:53:52 TRACE  :........flow_timer_start: Start T4
03/22 08:53:52 TRACE  :.......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:53:53 EVENT  :..mailslot_sitter: process received signal SIGALRM
03/22 08:53:53 TRACE  :.....event_timerT1_expire: T1 expired
03/22 08:53:53 INFO   :......router_forward_getOI: Ioctl to query route entry successful
03/22 08:53:53 TRACE  :......router_forward_getOI:         source address:   9.67.116.98
03/22 08:53:53 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98
03/22 08:53:53 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0
03/22 08:53:53 TRACE  :......router_forward_getOI:         route handle:   7f5251c8
03/22 08:53:53 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT
03/22 08:53:53 TRACE  :.......rsvp_action_nHop: constructing a PATH
03/22 08:53:53 TRACE  :.......flow_timer_start: started T1
03/22 08:53:53 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:53:53 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)
03/22 08:54:09 EVENT  :..mailslot_sitter: process received signal SIGALRM
03/22 08:54:09 TRACE  :.....event_timerT1_expire: T1 expired
03/22 08:54:09 INFO   :......router_forward_getOI: Ioctl to query route entry successful
03/22 08:54:09 TRACE  :......router_forward_getOI:         source address:   9.67.116.98
03/22 08:54:09 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98
03/22 08:54:09 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0
03/22 08:54:09 TRACE  :......router_forward_getOI:         route handle:   7f5251c8
03/22 08:54:09 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT
03/22 08:54:09 TRACE  :.......rsvp_action_nHop: constructing a PATH
03/22 08:54:09 TRACE  :.......flow_timer_start: started T1
03/22 08:54:09 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:54:09 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)
03/22 08:54:22 TRACE  :.....rsvp_event: received event from RAW-IP on interface 9.67.116.98
03/22 08:54:22 TRACE  :......rsvp_explode_packet: v=1,flg=0,type=2,cksm=54875,ttl=255,rsv=0,len=84
03/22 08:54:22 TRACE  :.......rsvp_parse_objects: STYLE is WF
03/22 08:54:22 INFO   :.......rsvp_parse_objects: obj RSVP_HOP hop=9.67.116.99, lih=0
03/22 08:54:22 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
03/22 08:54:22 INFO   :.......rsvp_flow_stateMachine: state RESVED, event RESV
03/22 08:54:22 TRACE  :........flow_timer_stop: Stop T4
03/22 08:54:22 TRACE  :........flow_timer_start: Start T4
03/22 08:54:22 TRACE  :.......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:54:24 EVENT  :..mailslot_sitter: process received signal SIGALRM
03/22 08:54:24 TRACE  :.....event_timerT1_expire: T1 expired
03/22 08:54:24 INFO   :......router_forward_getOI: Ioctl to query route entry successful
03/22 08:54:24 TRACE  :......router_forward_getOI:         source address:   9.67.116.98
03/22 08:54:24 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98
03/22 08:54:24 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0
03/22 08:54:24 TRACE  :......router_forward_getOI:         route handle:   7f5251c8
Kopieren


03/22 08:54:24 INFO   :......rsvp_flow_stateMachine: state RESVED, event T1OUT
03/22 08:54:24 TRACE  :.......rsvp_action_nHop: constructing a PATH
03/22 08:54:24 TRACE  :.......flow_timer_start: started T1
03/22 08:54:24 TRACE  :......rsvp_flow_stateMachine: reentering state RESVED
03/22 08:54:24 TRACE  :.......mailslot_send: sending to (9.67.116.99:0)
03/22 08:54:35 TRACE  :......rsvp_event_mapSession: Session=9.67.116.99:1047:6 exists
 24 
03/22 08:54:35 EVENT  :.....api_reader: api request SENDER_WITHDRAW
03/22 08:54:35 INFO   :.......rsvp_flow_stateMachine: state RESVED, event PATHTEAR
 25 
03/22 08:54:35 TRACE  :........traffic_action_oif: is to remove filter
03/22 08:54:35 INFO   :.........qosmgr_request: Ioctl to remove reservation successful
03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: RSVPRemActionName:  Entering
 
03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Entering
 
03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: ReadBuffer:  Exiting
 
03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: RSVPRemActionName:  Result = 0
 
03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: RSVPRemActionName:  Exiting
 
03/22 08:54:35 INFO   :..........rpapi_Reg_UnregFlow: flow[sess=9.67.116.99:1047:6, 
source=9.67.116.98:8000] unregistered from CLCat2
03/22 08:54:35 EVENT  :..........qosmgr_response: DELRESP from qosmgr, reason=0, qoshandle=0
03/22 08:54:35 INFO   :..........qosmgr_response: src-9.67.116.98:8000 dst-9.67.116.99:1047 proto-6
03/22 08:54:35 TRACE  :...........traffic_reader: tc response msg=3, status=1
 26 
03/22 08:54:35 TRACE  :........rsvp_action_nHop: constructing a PATHTEAR
03/22 08:54:35 TRACE  :........flow_timer_stop: stopped T1
03/22 08:54:35 TRACE  :........flow_timer_stop: Stop T4
 27 
03/22 08:54:35 TRACE  :.......rsvp_flow_stateMachine: entering state SESSIONED
03/22 08:54:35 TRACE  :........mailslot_send: sending to (9.67.116.99:0)
03/22 08:54:35 TRACE  :......rsvp_event_propagate: flow[session=9.67.116.99:1047:6, 
source=9.67.116.98:8000] ceased
 28 
03/22 08:54:35 EVENT  :.....api_reader: api request CLOSE
03/22 08:54:35 INFO   :.......rsvp_flow_stateMachine: state SESSIONED, event PATHTEAR
03/22 08:54:35 PROTERR:.......rsvp_flow_stateMachine: state SESSIONED does not expect event PATHTEAR
 29 
03/22 08:54:53 EVENT  :..mailslot_sitter: process received signal SIGTERM
03/22 08:54:53 INFO   :...check_signals: received TERM signal
03/22 08:54:53 INFO   :......term_policyAPI: UnRegisterFromPolicyAPI:  Entering
 
03/22 08:54:53 INFO   :......term_policyAPI: ReadBuffer:  Entering
 
03/22 08:54:53 INFO   :......term_policyAPI: ReadBuffer:  Exiting
 
03/22 08:54:53 INFO   :......term_policyAPI: UnRegisterFromPolicyAPI:  Result = 0
 
03/22 08:54:53 INFO   :......term_policyAPI: UnRegisterFromPolicyAPI:  Exiting
 
03/22 08:54:53 INFO   :......term_policyAPI: APITerminate:  Entering
 
03/22 08:54:53 INFO   :......term_policyAPI: APITerminate:  Exiting
 
03/22 08:54:53 INFO   :......term_policyAPI: Policy API terminated
03/22 08:54:53 INFO   :......dreg_process: deregistering process with the system
03/22 08:54:53 INFO   :......dreg_process: attempt to dereg (ifaeddrg_byaddr)
03/22 08:54:53 INFO   :......dreg_process: rc from ifaeddrg_byaddr  rc =0
03/22 08:54:53 INFO   :.....terminator: process terminated with exit code 0

"""

print(len(data))
zeilen = data.splitlines()
print(len(zeilen))

print("-" * 80)

for zeile in zeilen[:10]:
    print(zeile)

# Aufgabe: Bauen Sie eine Liste, inder nur die Zeilen drin sind, die mehr als 10 Zeichen haben
# Hinweis: Löschen von unnötigen Zeilen? Oder besser neue Liste und nur die Guten ins Töpfchen?

new_zeilen = []
for zeile in zeilen:

    # if len(zeile) > 60: - sehr unelegant, besser eguläre ausdfrücke oder vielleicht
    if zeile.startswith("03/22"):
        new_zeilen.append(zeile)

print(len(new_zeilen))

for zeile in new_zeilen[:30]:
    print(zeile)

# Aufgabe: Bauen Sie ein dict, bei dem jedes der Events ein Key ist und zu dem Event gezählt wird, wie oft es vorkommt
# for - Schleife
# Slice
# Strip
# ab ins dict damit, wenn neu - sonst für den KEy += 1
ereignisse = {}
for zeile in new_zeilen:
    event = zeile[15:22].strip()
    if event not in ereignisse:
        ereignisse[event] = 0
    ereignisse[event] += 1

    # oder kürzer: ereignisse[event] = ereignisse.get(event, 0) + 1
    #
    # oder mit KeyError try catch - effektiver als die "offizielle" Version
    # try:
    #    ereignisse[event] += 1
    # except KeyError:
    #    ereignisse[event] = 1

for k, v in ereignisse.items():
    print(f"{k:<10} {v:>10}")
