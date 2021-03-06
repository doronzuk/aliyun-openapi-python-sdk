# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class ConfigureSynchronizationJobAlertRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2018-08-01', 'ConfigureSynchronizationJobAlert','dts')

	def get_DelayOverSeconds(self):
		return self.get_query_params().get('DelayOverSeconds')

	def set_DelayOverSeconds(self,DelayOverSeconds):
		self.add_query_param('DelayOverSeconds',DelayOverSeconds)

	def get_DelayAlertStatus(self):
		return self.get_query_params().get('DelayAlertStatus')

	def set_DelayAlertStatus(self,DelayAlertStatus):
		self.add_query_param('DelayAlertStatus',DelayAlertStatus)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SynchronizationJobId(self):
		return self.get_query_params().get('SynchronizationJobId')

	def set_SynchronizationJobId(self,SynchronizationJobId):
		self.add_query_param('SynchronizationJobId',SynchronizationJobId)

	def get_ErrorAlertPhone(self):
		return self.get_query_params().get('ErrorAlertPhone')

	def set_ErrorAlertPhone(self,ErrorAlertPhone):
		self.add_query_param('ErrorAlertPhone',ErrorAlertPhone)

	def get_DelayAlertPhone(self):
		return self.get_query_params().get('DelayAlertPhone')

	def set_DelayAlertPhone(self,DelayAlertPhone):
		self.add_query_param('DelayAlertPhone',DelayAlertPhone)

	def get_ErrorAlertStatus(self):
		return self.get_query_params().get('ErrorAlertStatus')

	def set_ErrorAlertStatus(self,ErrorAlertStatus):
		self.add_query_param('ErrorAlertStatus',ErrorAlertStatus)

	def get_SynchronizationDirection(self):
		return self.get_query_params().get('SynchronizationDirection')

	def set_SynchronizationDirection(self,SynchronizationDirection):
		self.add_query_param('SynchronizationDirection',SynchronizationDirection)