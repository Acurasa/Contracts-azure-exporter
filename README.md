# Contracts-azure-exporter


**Program wykonuje GET request z API giełdy handlowej binance, następnie loguje aktywne kontrakty dla wysłania na azure blob storage**



### Zainstalowane 
**Azure CLI**

## Deploy

**Azure CLI**

# Execute script locally*

	py -m venv env
	cd env
	Scripts\activate
	pip install requests
	cd .. 
	py binance_requests.py
	deactivate
	
1.Azure CLI logging:

    az login
    az login --use-device-code
    az config param-persist on
    az account list
    
2.Stworzyć resource group:
```bash
    export AZ_RESOURCE_GROUP=<resource group name>
    
    az group create --name ${AZ_RESOURCE_GROUP} --location eastus
```
3.Stworzyć zasob maszyny wirtualnej Azure:   

	az vm create \
	  --location <eastus> \
	  --resource-group ${AZ_RESOURCE_GROUP} \
	  --name <azure_vm_via_cli> \
	  --size <Standard_B1s> \
	  --image <UbuntuLTS> \
	  --public-ip-sku Standard \
	  --admin-username <azureuser> \
	  --admin-password <password>

**Powershell & Bash & cmd**
	
4.Zalogować się do maszyny przez ssh:

	ssh ubuntu@<vm_adress>
	
5.Zkopiować skrypt do maszyny w.:
	
	scp <localpath to script>/binance_futures.py  <Unix Path on vm>

6.Zainstalować Python3 & pip:

	sudo apt-get install azure-cli 
	sudo apt-get install python3
	sudo apt install python3-pip

7.Stworzyć  środowisko Python, zainstalować moduł **requests** oraz wykonać skrypt binance_requests.py:
	
	py -m venv env
	cd env
	Scripts\activate
	pip install requests
	cd .. 
	py binance_requests.py
	deactivate
	
**Azure CLI**
	
8.Stworzyć zasob Microsoft Azure Blob Storage oraz zalogować się na maszynie wirtualnej:
```bash
        az login --use-device-code
        az config param-persist on
	export AZ_RESOURCE_GROUP=<resource group name>	
	export AZ_STORAGE_ACCOUNT=<storage name>
	az storage account create \
    	--name ${AZ_STORAGE_ACCOUNT} \
    	--resource-group ${AZ_RESOURCE_GROUP} \
    	--location <eastus> \
    	--sku Standard_ZRS \
    	--encryption-services blob
```

9.Stworzyć Kontejner Azure Blob Storage:
```bash
	export AZ_CONTAINER_NAME=<container name>
	az storage container create \
		--account-name ${AZ_STORAGE_ACCOUNT} \
		--name ${AZ_CONTAINER_NAME}\
		--auth-mode login
```
10.Wysłać wygenerowany plik tekstowy contracts.txt do azure blob storage  

	az storage blob upload \
	 	--account-name ${AZ_STORAGE_ACCOUNT} \
	 	--container-name ${AZ_CONTAINER_NAME} \
	 	--name <contracts.txt> \
	 	--file <contracts.txt>
		
## Dokumentacje & Inne		

https://docs.microsoft.com/en-us/azure/storage/

https://docs.microsoft.com/pl-pl/cli/azure/
