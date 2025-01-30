Dataset **Disease Detection in Fruit Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE0OTdfRGlzZWFzZSBEZXRlY3Rpb24gaW4gRnJ1aXQgSW1hZ2VzL2Rpc2Vhc2UtZGV0ZWN0aW9uLWluLWZydWl0LWltYWdlcy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJmeXV1VGZNd3pUQXJBNDZvVk04WkZYZlVkd1JXSDNyNlV2cXdqSEVFT2kwPSJ9)

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