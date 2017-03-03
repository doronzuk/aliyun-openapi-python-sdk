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
class TextKeywordFilterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2016-12-16', 'TextKeywordFilter','green')
		self.set_method('POST')

	def get_CustomDict(self):
		return self.get_query_params().get('CustomDict')

	def set_CustomDict(self,CustomDict):
		self.add_query_param('CustomDict',CustomDict)

	def get_Text(self):
		return self.get_query_params().get('Text')

	def set_Text(self,Text):
		self.add_query_param('Text',Text)

	def get_UseSysDic(self):
		return self.get_query_params().get('UseSysDic')

	def set_UseSysDic(self,UseSysDic):
		self.add_query_param('UseSysDic',UseSysDic)