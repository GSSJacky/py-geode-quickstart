'''
Copyright (c) 2014 Pivotal Software, Inc.  All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
Unless required by applicable law or agreed to in writing, software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
'''

from distutils.core import setup

setup(
    name='py-geode-quickstart',
    version='1.0',
    description='Python client quickstart for Geode REST service ',
    long_description=open('README.md').read(),
    url='https://github.com/GSSJacky',
    packages=['org.apache.geode',],
    license='Apache 2.0',
    keywords=['Geode', 'In Memory Data Grid'],
    install_requires=['requests', 'jsonpickle'],
    author='Geode Community',
    maintainer='Jacky'
)
