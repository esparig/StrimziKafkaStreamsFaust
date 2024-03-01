# Description
This is a simple example of how to create a Kafka consumer using [Faust](https://faust.readthedocs.io/en/latest/index.html), a python library for stream processing.

## Requirements
Basic requirement to run this example is a Kubernetes cluster with Strimzi managed Apache Kafka cluster deployed. Examples how to deploy Apache Kafka using Strimzi can be found on the [Strimzi website](https://strimzi.io).

Follow the [Strimzi Quickstart](https://strimzi.io/quickstarts/) to install Strimzi and Kafka on your local machine or on a cloud provider.

## Deploy example
Deploy the example provided in https://github.com/strimzi/client-examples/tree/main
This will create a topic called `my-topic` and produce some messages to it.

## Deploy the Faust consumer
To deploy the Faust consumer, you can use the provided `deployment.yaml` file like `kubectl -n kafka apply -f deployment.yaml`. This will create a new deployment in your Kubernetes cluster.

Output sample:

```
[2024-03-01 11:28:19,066] [1] [WARNING] Received message: Hello world - 65006 
[2024-03-01 11:28:19,067] [1] [WARNING] Extracted number: 65006 
[2024-03-01 11:28:20,065] [1] [WARNING] Received message: Hello world - 65007 
[2024-03-01 11:28:20,067] [1] [WARNING] Extracted number: 65007 
[2024-03-01 11:28:21,068] [1] [WARNING] Received message: Hello world - 65008 
[2024-03-01 11:28:21,069] [1] [WARNING] Extracted number: 65008 
```

