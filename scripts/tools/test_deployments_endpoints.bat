az containerapp show ^
  --name refund-agent-service ^
  --resource-group aiagent-course-rg ^
  --query "properties.configuration.ingress.fqdn" ^
  --output tsv

curl https://refund-agent-service.delightfulplant-97cb683c.australiaeast.azurecontainerapps.io/

curl.exe -X POST "https://refund-agent-service.delightfulplant-97cb683c.australiaeast.azurecontainerapps.io/echo" -H "Content-Type: application/json" -d "{\"message\":\"test refund\"}"

az containerapp logs show ^
  --name refund-agent-service ^
  --resource-group aiagent-course-rg ^
  --tail 200
