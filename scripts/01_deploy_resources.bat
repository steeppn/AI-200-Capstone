@echo off

az group create ^
    --name aiagent-course-rg ^
    --location australiaeast 

az deployment group create ^
    --resource-group aiagent-course-rg ^
    --template-name deployment-template.bicep ^
    --parameters coursePrefix=courseunit1

az deployment group show ^
    --resource-group aiagent-course-rg ^
    --name deployment-template ^
    --query properties.output