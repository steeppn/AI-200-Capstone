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

echo Deployment Outputs:

az deployment group show ^
    --resource-group aiagent-course-rg ^
    --name deployment-template ^
    --query properties.outputs ^
    --output json

pause