@echo off

az cognitiveservices model list ^
    --location australiaeast ^
    --query "[?model.name=='gpt-5-mini' && kind=='OpenAI'].{Name:model.name, Version:model.version, Format:model.format, SKU:skuName}" ^
    --output table

pause