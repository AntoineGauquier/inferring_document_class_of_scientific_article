# Automatically Inferring the Document Class of a Scientific Article

This repository provides code, data, and models supplementing the
research article [*Automatically Inferring the Document Class of a
Scientific Article*](article.pdf) by Antoine Gauquier and [Pierre
Senellart](https://pierre.senellart.com/).

Some more content will be added within this repository over the coming
weeks.

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
(comma-separated) CSV file [dataset_information.csv]; after one header
row, the file contains one article per row with the following column
fields, in order:

1. `arxiv_identifier` is the unique arXiv identifier, of the form
   `YYMM.NNNNN` of the article. The metadata and PDF of such an
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

1. `nb_occurrences` is the number of times the PDF is seen/evaluated by the model after applying oversampling.

1. `split` is describing either the PDF belongs to training set (`train`) or to test set (`test`).

To obtain the exact same dataset, you should use one of the [Bulk
Access](https://info.arxiv.org/help/bulk_data.html) facilities of arXiv
(we used the AWS option, and all content was retrieved in June 2020) and,
as explained there, not directly crawl the main arXiv Web site. Use the
`last_modified` and `md5_hash` fields to verify that each article is the
correct version; if not, alternates version can be downloaded separately.

## Contact

<https://github.com/AntoineGauquier/inferring_document_class_of_scientific_article/>

* Antoine Gauquier <antoine.gauquier@ens.psl.eu>
* Pierre Senellart <pierre@senellart.com>
