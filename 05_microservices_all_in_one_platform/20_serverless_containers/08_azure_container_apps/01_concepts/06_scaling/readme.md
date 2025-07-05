# Set scaling rules in Azure Container Apps

https://learn.microsoft.com/en-us/azure/container-apps/scale-app?pivots=azure-cli

<<<<<<< HEAD
Azure Container Apps manages automatic horizontal scaling through a set of declarative scaling rules. As a container app revision scales out, new instances of the revision are created on-demand. These instances are known as replicas.

To support this scaling behavior, Azure Container Apps is powered by KEDA (Kubernetes Event-driven Autoscaling). KEDA supports scaling against a variety of metrics like HTTP requests, queue messages, CPU and memory load, and event sources like Azure Service Bus, Azure Event Hubs, Apache Kafka, and Redis. For more information, see Scalers in the KEDA documentation.

Adding or editing scaling rules creates a new revision of your container app. A revision is an immutable snapshot of your container app. To learn which types of changes trigger a new revision, see revision change types.
=======
>>>>>>> sashank/main
