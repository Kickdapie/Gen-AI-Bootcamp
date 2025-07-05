# Application lifecycle management in Azure Container Apps

https://learn.microsoft.com/en-us/azure/container-apps/application-lifecycle-management

<<<<<<< HEAD
The Azure Container Apps application lifecycle revolves around revisions.

When you deploy a container app, the first revision is automatically created. More revisions are created as containers change, or any adjustments are made to the template section of the configuration.

A container app flows through four phases: deployment, update, deactivation, and shut down.



Deployment
As a container app is deployed, the first revision is automatically created.

Azure Container Apps: Deployment phase






Update
As a container app is updated with a revision scope-change, a new revision is created. You can choose whether to automatically deactivate old revisions (single revision mode), or allow them to remain available (multiple revision mode).

Azure Container Apps: Update phase

When in single revision mode, Container Apps handles the automatic switch between revisions to support zero downtime deployment.




Deactivate
Once a revision is no longer needed, you can deactivate a revision with the option to reactivate later. During deactivation, containers in the revision are shut down.

Azure Container Apps: Deactivation phase




Shutdown
The containers are shut down in the following situations:

As a container app scales in
As a container app is being deleted
As a revision is being deactivated
When a shutdown is initiated, the container host sends a SIGTERM message to your container. The code implemented in the container can respond to this operating system-level message to handle termination.

If your application doesn't respond within 30 seconds to the SIGTERM message, then SIGKILL terminates your container.

Additionally, make sure your application can gracefully handle shutdowns. Containers restart regularly, so don't expect state to persist inside a container. Instead, use external caches for expensive in-memory cache requirements.

=======
>>>>>>> sashank/main
