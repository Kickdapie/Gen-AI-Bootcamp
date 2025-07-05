# Azure Container Apps environments

https://learn.microsoft.com/en-us/azure/container-apps/environment

<<<<<<< HEAD
*A Container Apps environment is a secure boundary around one or more container apps and jobs. The Container Apps runtime manages each environment by handling OS upgrades, scale operations, failover procedures, and resource balancing.

Environments include the following features:


Type	
There are two different types of Container Apps environments: Workload profiles environments and Consumption only environments. Workload profiles environments support both the Consumption and Dedicated plans whereas Consumption only environments support only the Consumption plan.

Virtual network	
A virtual network supports each environment, which enforces the environment's secure boundaries. As you create an environment, a virtual network with limited network capabilities is created for you, or you can provide your own. Adding an existing virtual network gives you fine-grained control over your network.

Multiple container apps	
When multiple container apps are in the same environment, they share the same virtual network and write logs to the same logging destination.

Multi-service integration	
You can add Azure Functions and Azure Spring Apps to your Azure Container Apps environment.


***
Basically a bigger container holding multiple containers that share resources
=======
>>>>>>> sashank/main
