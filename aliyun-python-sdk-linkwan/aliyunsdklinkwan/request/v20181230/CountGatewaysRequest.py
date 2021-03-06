# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CountGatewaysRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'CountGateways','linkwan')
		self.set_protocol_type('https');

	def get_FuzzyName(self):
		return self.get_body_params().get('FuzzyName')

	def set_FuzzyName(self,FuzzyName):
		self.add_body_params('FuzzyName', FuzzyName)

	def get_FuzzyGwEui(self):
		return self.get_body_params().get('FuzzyGwEui')

	def set_FuzzyGwEui(self,FuzzyGwEui):
		self.add_body_params('FuzzyGwEui', FuzzyGwEui)

	def get_FreqBandPlanGroupId(self):
		return self.get_body_params().get('FreqBandPlanGroupId')

	def set_FreqBandPlanGroupId(self,FreqBandPlanGroupId):
		self.add_body_params('FreqBandPlanGroupId', FreqBandPlanGroupId)

	def get_FuzzyCity(self):
		return self.get_body_params().get('FuzzyCity')

	def set_FuzzyCity(self,FuzzyCity):
		self.add_body_params('FuzzyCity', FuzzyCity)

	def get_OnlineState(self):
		return self.get_body_params().get('OnlineState')

	def set_OnlineState(self,OnlineState):
		self.add_body_params('OnlineState', OnlineState)

	def get_IsEnabled(self):
		return self.get_body_params().get('IsEnabled')

	def set_IsEnabled(self,IsEnabled):
		self.add_body_params('IsEnabled', IsEnabled)