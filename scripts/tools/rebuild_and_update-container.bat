az acr build ^
    --registry ai200stephenacr ^
    --image refund-service:latest ^
    --file "%~dp0..\Dockerfile" ^
    "%~dp0.." ^
    --no-logs

az containerapp update ^
  --name refund-agent-service ^
  --resource-group aiagent-course-rg ^
  --image ai200stephenacr.azurecr.io/refund-service:latest