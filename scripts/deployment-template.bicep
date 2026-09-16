param coursePrefix string 
param aiFoundryName string = coursePrefix
param aiProjectName string = '${coursePrefix}-proj'
param llmDeploymentName string = '${coursePrefix}-llm-deployment'
param location string = resourceGroup().location
 
// LLM MODEL PARAMETERS
// ==============================
param modelCapacity int = 1
param modelSkuName string = 'GlobalStandard'

param modelName string = 'gpt-5-mini'
param modelFormat string = 'OpenAI'
param modelVersion string = '2025-08-07'
// ==============================

resource aiFoundry 'Microsoft.CognitiveServices/accounts@2025-06-01' = {
  name: aiFoundryName
  location: location
  identity:{
    type: 'SystemAssigned'
  }
  sku:{
    name: 'S0'
  }
  kind: 'AIServices'
  properties:{
    allowProjectManagement: true
    customSubDomainName: aiFoundryName
    disableLocalAuth: false
  }
}

resource aiProject 'Microsoft.CognitiveServices/accounts/projects@2025-06-01' = {
  name: aiProjectName
  parent: aiFoundry
  location: location
  identity:{
    type: 'SystemAssigned'
  }
  properties:{}
}

resource llmModelDeployment 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  name: llmDeploymentName
  parent: aiFoundry
  sku:{
    capacity: modelCapacity
    name: modelSkuName
  }
  properties:{
    model:{
      name: modelName
      format: modelFormat
      version: modelVersion
    }
  }
}

output azure_llm_endpoint string = 'https://${aiFoundry.properties.customSubDomainName}.services.ai.azure.com/openai/v1'
output llm_model_name string = llmModelDeployment.name
