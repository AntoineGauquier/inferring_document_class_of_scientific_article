# Automatically Inferring the Document Class of a Scientific Article

This repository provides additional content, code, data, and models supplementing the
research article [*Automatically Inferring the Document Class of a
Scientific Article*](short.pdf) by Antoine Gauquier and [Pierre
Senellart](https://pierre.senellart.com/).

## Additional content

[Appendix to the original paper](appendix.pdf), with complete list of
labels and detailed experimental results.

## Dataset

We used 98713 articles in PDF format (completed by their sources to
obtain the ground truth document class) published in 2018 on
[arXiv](https://arXiv.org/). The [default
license](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html)
used within arXiv only grants the rights to distribute the article to
arXiv, but does not grant redistribution or other derivative rights. For
this reason, we cannot provide the entire dataset in full, but we do
provide here explanations on how to build the same dataset.

The list of all articles used for this dataset is available in the
(comma-separated) CSV file [dataset_information.csv](dataset_information.csv); after one header
row, the file contains one article per row with the following column
fields, in order:

1. `arxiv_identifier` is the unique arXiv identifier, of the form
   `arXiv:YYMM.NNNNN` of the article. The metadata and PDF of such an
   article, respectively, are at the following official URLs:
   `https://arxiv.org/abs/YYMM.NNNNN` and
   `https://arxiv.org/pdf/YYMM.NNNNN.pdf`
1. `document_class` is the ground-truth document class of each article,
   as inferred by a simple extraction from the LaTeX source of the
   article; similar classes have been regrouped, as explained in the
   article.
1. `last_modified` is the last modification date and time of the PDF file, in
   [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, as stored within arXiv.
   This helps disambiguate different versions of the same article stored
   on arXiv.
1. `md5_hash` is a MD5 hash of the content of the PDF file. This helps
   disambiguate different versions of the same article stored on arXiv.

1. `nb_occurrences` is the number of occurrences of the PDF article in
   the oversampled dataset.

1. `split` is describing whether the PDF belongs to the training set (`train`)
   or to the test set (`test`).

To obtain the exact same dataset, you should use one of the [Bulk
Access](https://info.arxiv.org/help/bulk_data.html) facilities of arXiv
(we used the AWS option, and all content was retrieved in June 2020) and,
as explained there, not directly crawl the main arXiv Web site. Use the
`last_modified` and `md5_hash` fields to verify that each article is the
correct version; if not, alternates version can be downloaded separately.

## Code

You will find in the [code](code/) directory the Keras code of the three
main models proposed:

- [code/cnn_model_multiclass_merged_classes.py](code/cnn_model_multiclass_merged_classes.py) for the simple CNN
    architecture on 33 classes
- [code/cnn_model_binary_rejection.py](code/cnn_model_binary_rejection.py) for the binary rejector model
    to determine whether an article belongs to a homogeneous class
- [code/cnn_model_multiclass_merged_classes_non_heterogeneous.py](code/cnn_model_multiclass_merged_classes_non_heterogeneous.py) for the
    simple CNN artchitecture on 31 homogeneous classes, to be used after
    the rejector

## Models

You will find in the [models/](models) directory all trained CNN models used;
note that you need Git Large File Storage (git-lfs) installed and
initialized to retrieve these models:

- [models/model_multiclass_33classes_256_256.h5](models/model_multiclass_33classes_256_256.h5) for the simple CNN
    architecture on 33 classes
- [models/model_resnet50v2_256_256.h5](models/model_resnet50v2_256_256.h5) for the ResNet50V2 architecture on
    33 classes
- [models/model_nasnetmobile_256_256.h5](models/model_nasnetmobile_256_256.h5) for the NASNetMobile
    architecture on 33 classes
- [models/model_efficientnetv2b0_256_256.h5](models/model_efficientnetv2b0_256_256.h5) for the EfficientNetV2B0
    architecture on 33 classes
- [models/model_binary_rejector_256_256.h5](models/model_binary_rejector_256_256.h5) for the binary rejector to
    detect homogenerous classes
- [models/model_multiclass_31classes_256_256.h5](models/model_multiclass_31classes_256_256.h5) for the simple CNN
    architecture on 31 homogeneous classes

## Contact

<https://github.com/AntoineGauquier/inferring_document_class_of_scientific_article/>

* Antoine Gauquier <antoine.gauquier@ens.psl.eu>
* Pierre Senellart <pierre@senellart.com>
