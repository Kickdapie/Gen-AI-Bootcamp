https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server

https://medium.com/@shubhambhama/connect-figma-to-cursor-ai-with-mcp-in-5-minutes-0c4794537fa3

https://github.com/gannonh/memento-mcp

This what we are going to use for mcp in the gen AI work (going to rework this for our project). We want to create an interface that allows the user to upload their design and have their design be built by the mcp protocol and cursor without needing either application. The return is a fully built and functional application.

Not going to just with Figma but also other tools. This app will work with corporate rules for UI's.

Use bolt://host.docker.internal:7687 instead of bolt://localhost:7687 in src/storage/neo4j/Neo4jConfig.ts for the uri
Why? Because inside the Docker container, localhost refers to itself, not your Windows host running Neo4j.

docker run -it --rm -v "C:\Users\danny\Documents\Code\Hundred Hands:/app" -w /app node:22-alpine sh