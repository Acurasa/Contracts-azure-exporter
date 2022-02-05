# Contracts-azure-exporter

**Leonid Stasyuk L_III_NW_INF_PAC2 69224**

**Program wykonuje GET request z API giełdy handlowej binance, następnie loguje aktywne kontrakty dla wysłania na azure blob storage**



### Zainstalowane 
**Azure CLI**

## Deploy
**Azure CLI**

1.Azure CLI logging:

    az login
    az login --use-device-code
    az  account list
    
2.Stworzyć resource group:

    az group create --name name --location eastus

3.Stworzyć zasob maszyny wirtualnej Azure:   

	az vm create \
	  --location <eastus> \
	  --resource-group <name> \
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
	
8.Stworzyć zasob Microsoft Azure Blob Storage:
	
	az storage account create \
    	--name <storage-account> \
    	--resource-group <name> \
    	--location <eastus> \
    	--sku Standard_ZRS \
    	--encryption-services blob
	
9.Stworzyć Kontejner Azure Blob Storage:

	az storage container create \
		--account-name <storage-account> \
		--name <container> \
		--auth-mode login

10.Wysłać wygenerowany plik tekstowy contracts.txt do azure blob storage  

	az storage blob upload \
	 	--account-name <storage-account> \
	 	--container-name <container> \
	 	--name <contracts.txt> \
	 	--file <contracts.txt>
