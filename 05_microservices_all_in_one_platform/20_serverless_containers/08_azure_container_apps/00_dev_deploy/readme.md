# Develop and Deploy

[Select the right code-to-cloud path for Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/code-to-cloud-options)

[Quickstart: Deploy to Azure Container Apps using Visual Studio Code](https://learn.microsoft.com/en-us/azure/container-apps/deploy-visual-studio-code)

When you run:

Azure Container Apps: Deploy Project from Workspace

VS Code uses:

Your currently opened workspace or folder

The command deploys the project in your currently active workspace folder.

If you have multiple folders open in your workspace, it usually prompts you to choose the correct folder.

Where does it find the Dockerfile?
The extension looks for:
A Dockerfile in the root of the selected project folder.
If it finds multiple Dockerfiles, it may prompt you to choose which one to use.


***
The VS Code Azure Container extensions generate a docker build command to build the container image. The build context location, Dockerfile used, and resulting container image details are determined by your current workspace folder and the Azure extension configuration. 
Azure then manages the deployment of the built image to your selected container app or registry.

The extension does the sequence of the build. The actual command building of the image is done by Docker daemon reading the docker file.

To change the sequence, use the azure CLI directly (using bicep or terraform)
***