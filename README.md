# py-geode-quickstart
=================

This library enables your python applications to use GemFire as a datastore. (GemFire is a distributed key-value store.). This library exposes Spring's CrudRepository like methods in an effort to simplify GemFire's APIs while still giving access to advanced GemFire features. 

Requirements(Tested env):
-Gemfire9.10.14
-Python3.9.10 or Python3.8.12

## Installation
---------------

Install from source:
```
    $ sudo python setup.py install
```
## Quick Start
--------------

1. Start the GemFire REST service by [following the instructions](http://gemfire.docs.pivotal.io/docs-gemfire/latest/rest_apps/setup_config.html)

2. Create a Region on the server (Region is a distributed ConcurrentMap in which GemFire stores the data). 
```
    gfsh>create region --name=Customer --type=PARTITION
```

3. Modify the quickstart.py's hostname and port(Rest API Service) and user/password along with your Gemfire Cluster's setting.

4. Run the quickstart.py from any python IDE or you can also run the below command :
```
/usr/local/bin/python3 /Users/jaxu/Downloads/TOI/py-geode-rest/py-geode-quickstart/quickstart.py
```

## API Reference
----------------
1.This library exercises [GemFire's REST APIs](http://gemfire.docs.pivotal.io/docs-gemfire/latest/rest_apps/book_intro.html) for enabling your python application to use GemFire as its datastore.

2.When developing your own python client, you can also refer the API reference from swagger-ui page:
http://[Host_Name]:[Rest_API_Port]/geode/swagger-ui.html