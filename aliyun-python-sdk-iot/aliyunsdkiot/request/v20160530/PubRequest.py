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
class PubRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2016-05-30', 'Pub')

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_Qos(self):
		return self.get_query_params().get('Qos')

	def set_Qos(self,Qos):
		self.add_query_param('Qos',Qos)

	def get_TopicFullName(self):
		return self.get_query_params().get('TopicFullName')

	def set_TopicFullName(self,TopicFullName):
		self.add_query_param('TopicFullName',TopicFullName)

	def get_MessageContent(self):
		return self.get_query_params().get('MessageContent')

	def set_MessageContent(self,MessageContent):
		self.add_query_param('MessageContent',MessageContent)