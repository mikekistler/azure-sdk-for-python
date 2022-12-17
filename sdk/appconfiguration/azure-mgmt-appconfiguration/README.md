# Azure App Configuration Management client library for Python

This is the Microsoft Azure App Configuration Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the [Azure SDK Python Releases](https://aka.ms/azsdk/python/all).

[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/appconfiguration/azure-appconfiguration-mgmt) | [Package (Pypi)][package] | [Product documentation][appconfig_docs]

## _Disclaimer_

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, see https://github.com/Azure/azure-sdk-for-python/issues/20691_

## Prerequisites

* Python 3.7 or later is required to use this package.
* You need an [Azure subscription][azure_sub] to use this package.

## Install the package

Install the Azure App Configuration Management client library for Python with pip:

```commandline
pip install azure-appconfiguration-mgmt
```

## Import the package

Import the App Configuration Management client library into your application with the following import statement:

```python
from azure.mgmt.appconfiguration import AppConfigurationManagementClient
```

## Get credentials

Here we demonstrate using [`DefaultAzureCredential`][default_cred_ref] to authenticate as a service principal.
`DefaultAzureCredential` is a "chained credential" that will obtain credentials from environment variables,
a managed identity, the signed-in user of the Azure CLI or a Microsoft application such as Visual Studio.
See the [Authentication][authentication] topic in the documentation for information about other credential types.

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```

## Create a client

Constructing the client requires your Azure subscription ID. Here we'll get that from an environment variable but
you could also retrieve this value from an Azure Keyvault.

```python
    subscription_id = os.environ.get("SUBSCRIPTION_ID", None)
    appconfig_client = AppConfigurationManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=subscription_id
    )
```

## Making client requests

Most App Configuration Management resources must be contained in a resource group. See [create a resource group][resource_groups] to learn
how to dynamically create a resource group in your Python application.

## More information

For more information on using the Azure Management client libraries for Python, see the [Overview of the Azure SDK for Python](https://aka.ms/azsdk/python/mgmt).

For docs and references, see [Python SDK References](https://learn.microsoft.com/python/api/overview/azure/?view=azure-python).
Documentation on latest packages--including beta releases--is available at [Python SDK References (latest)](https://learn.microsoft.com/python/api/overview/azure/?view=azure-python-preview).

Code samples for this package can be found at [App Configuration Management](https://learn.microsoft.com/samples/browse/?languages=python&term=Getting%20started%20-%20Managing&terms=Getting%20started%20-%20Managing) on learn.microsoft.com.
Code samples for other Azure services are available at [Samples Repo](https://github.com/Azure-Samples/azure-samples-python-management/tree/main/samples/appconfiguration).

## Provide Feedback

If you encounter any bugs or have suggestions, file an issue in the
[Issues](https://github.com/Azure/azure-sdk-for-python/issues)
section of the project.

![Impressions](https://azure-sdk-impressions.azurewebsites.net/api/impressions/azure-sdk-for-python%2Fazure-mgmt-appconfiguration%2FREADME.png)

<!-- LINKS -->

[appconfig_docs]: https://learn.microsoft.com/azure/azure-app-configuration/
[authentication]: https://learn.microsoft.com/azure/developer/python/sdk/authentication-overview
[azure_sub]: https://azure.microsoft.com/free/
[default_cred_ref]: https://aka.ms/azsdk-python-identity-default-cred-ref
[package]: https://pypi.org/project/azure-appconfiguration-mgmt/
[resource_groups]: https://learn.microsoft.com/azure/developer/python/sdk/examples/azure-sdk-example-resource-group
