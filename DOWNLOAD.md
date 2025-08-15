Dataset **Disease Detection in Fruit Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTQ5N19EaXNlYXNlIERldGVjdGlvbiBpbiBGcnVpdCBJbWFnZXMvZGlzZWFzZS1kZXRlY3Rpb24taW4tZnJ1aXQtaW1hZ2VzLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIk96eUdLdjZZTlpNWUs3elV5U3dpckdQcDgyRm0xckdFeExabzZiZi9zMWM9In0=?response-content-disposition=attachment%3B%20filename%3D%22disease-detection-in-fruit-images-DatasetNinja.tar%22)

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