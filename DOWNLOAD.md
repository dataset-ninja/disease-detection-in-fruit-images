Dataset **Disease Detection in Fruit Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/j/0/7n/QGz5WbKFT4cd7oDce2l5cPAdzAQ9guex1aw9WgSqOcwkoqFcfSxfVY40xvCm7XxLEjiNwViNQLt05vj5HrC2ixntB6rETu92EgLEq4Et1qPO6Kki77NNjaNLMJZK.tar)

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

The data in original format can be [downloaded here](https://github.com/QuIIL/Dataset-Region-Aggregated-Attention-CNN-for-Disease-Detection-in-Fruit-Images/archive/refs/heads/main.zip)