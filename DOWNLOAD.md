Dataset **Disease Detection in Fruit Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/3/v/qn/r5eyLYVUm5J2XStCNrXbPP87ySHRcr6BzaClkFh3qxYHrdxwYgh1R6PKtOcOfIkFJL89hEErG8eu2QiKHNJnJJZOzLprQvEs4IXj2vEYJ8gdXl4YAhLdBHhAxNbH.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Disease Detection in Fruit Images', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://github.com/QuIIL/Dataset-Region-Aggregated-Attention-CNN-for-Disease-Detection-in-Fruit-Images/archive/refs/heads/main.zip).