@echo off

REM get the latest revision number to restart
for /f "delims=" %%R in ('
  az containerapp show ^
    --name refund-agent-service ^
    --resource-group aiagent-course-rg ^
    --query properties.latestRevisionName ^
    --output tsv
') do set "LATEST_REVISION=%%R"

az containerapp revision restart ^
  --name refund-agent-service ^
  --resource-group aiagent-course-rg ^
  --revision "%LATEST_REVISION%"
