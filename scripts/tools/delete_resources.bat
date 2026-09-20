az group delete --name aiagent-course-rg --yes

az cognitiveservices account list-deleted --output table

az cognitiveservices account purge --location australiaeast --resource-group aiagent-course-rg --name ai200stephen