@echo off

az group create ^
    --name aiagent-course-rg ^
    --location australiaeast 

az deployment group create ^
    --name deployment-template ^
    --resource-group aiagent-course-rg ^
    --template-file "%~dp0deployment-template.bicep" ^
    --parameters coursePrefix=ai200stephen

az deployment group show ^
    --resource-group aiagent-course-rg ^
    --name deployment-template ^
    --query properties.provisioningState ^
    --output tsv

az containerapp env create ^
    --name ai200stephen-env ^
    --resource-group aiagent-course-rg ^
    --location australiaeast

az acr build ^
    --registry ai200stephenacr ^
    --image refund-service:latest ^
    --file "%~dp0..\Dockerfile" ^
    "%~dp0.." ^
    --no-logs

az containerapp create ^
    --name refund-agent-service ^
    --resource-group aiagent-course-rg ^
    --environment ai200stephen-env ^
    --image ai200stephenacr.azurecr.io/refund-service:latest ^
    --registry-server ai200stephenacr.azurecr.io ^
    --system-assigned ^
    --registry-identity system ^
    --target-port 8080 ^
    --ingress external

    

echo Deployment Outputs:

az deployment group show ^
    --resource-group aiagent-course-rg ^
    --name deployment-template ^
    --query properties.outputs ^
    --output json

pause