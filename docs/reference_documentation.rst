Reference Documentation
#######################

Service endpoint
================

A service endpoint is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- ``https://developers.smswithoutborders.com:14000``

API V1 Endpoints
================

.. list-table::
    :widths: auto

    * - Action
      - Endpoint
      - Parameters
      - Request body

    * - :ref:`Send SMS<Send single SMS message>`
      - POST /v1/sms
      - None
      - * auth_id = STRING
        * data = [{text = STRING, number = STRING, operator_name = STRING}]
    
    * - :ref:`Get Phone number operator name<Get Phone Number operator name>`
      - POST /v1/sms/operators
      - None
      - * [{text = STRING, number = STRING, operator_name = STRING}]

.. warning::

    We advise you to use this endpoint safely in the back-end to avoid exposing your developer's token to unauthorized persons.

Examples using `curl <https://curl.se/>`_

Send single SMS message
***********************

.. code-block:: bash

    curl --location --request POST 'https://developers.smswithoutborders.com:14000/v1/sms' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "auth_id":"",
    "data": [{
        "operator_name":"",
        "text":"",
        "number":""
        }]
    }'

Send bulk SMS messages
**********************

.. code-block:: bash

    curl --location --request POST 'https://developers.smswithoutborders.com:14000/v1/sms' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "auth_id":"",
    "data": [{
        "operator_name":"",
        "text":"",
        "number":""
        },
        {
        "operator_name":"",
        "text":"",
        "number":""
        },
        {
        "operator_name":"",
        "text":"",
        "number":""
        }]
    }'

Get Phone Number operator name
******************************

If the ```operator_name``` key is an empty string or not present in the request, It will be generated and populated in the response. But if the ```operator_name``` key is present it won't be modified in the response.

.. code-block:: bash

    curl --location --request POST 'https://developers.smswithoutborders.com:14000/v1/sms/operators' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "[{
        "operator_name":"",
        "text":"",
        "number":""
        },
        {
        "operator_name":"",
        "text":"",
        "number":""
        },
        {
        "operator_name":"",
        "text":"",
        "number":""
        }]
    }'
