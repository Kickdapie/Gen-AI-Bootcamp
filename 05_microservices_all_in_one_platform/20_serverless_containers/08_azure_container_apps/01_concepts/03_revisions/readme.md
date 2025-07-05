# Update and deploy changes in Azure Container Apps

https://learn.microsoft.com/en-us/azure/container-apps/revisions

<<<<<<< HEAD
Change management can be challenging as you develop containerized applications in the cloud. Ultimately, you need the support to track changes, ensure uptime, and have mechanisms to handle smooth rollbacks.

Change management in Azure Container Apps is powered by revisions, which are a snapshot of each version of your container app.

Key characteristics of revisions include:

Immutable:
Once established, a revision remains unchangeable.

Versioned: 
Revisions act as a record of the container app's versions, capturing its state at various stages.

Automatically provisioned: 
When you deploy a container app for the first time, an initial revision is automatically created.

Scoped changes: 
While revisions remain static, application-scope changes can affect all revisions, while revision-scope changes create a new revision.

Historical record: 
By default, you have access to 100 inactive revisions, but you can adjust this threshold manually.

Multiple revisions: 
You can run multiple revisions concurrently. This feature is especially beneficial when you need to manage different versions of your app simultaneously.



Lifecycle:

Provisioning status
When you create a new revision, the container app undergoes startup and readiness checks. During this phase, the provisioning status serves as a guide to track the container app's progress.


Running status
After a container app is successfully provisioned, a revision enters its operating phase. The running status helps monitor a container app's health and functionality.

Inactive status
Revisions can also enter an inactive state. These revisions don't possess provisioning or running states. However, Azure Container Apps maintains a list of these revisions, accommodating up to 100 inactive entries. You can activate a revision at any time
=======
>>>>>>> sashank/main
