# Experiments

This is a repository with some useful information. \
Notebooks:

* Classification:
  * [Sarcasm prediction (binary, 1M rows)](https://nbviewer.org/github/Extremesarova/experiments/blob/80fae76cb94288155417735cae9b06aa171ec6b1/ods_mlcourse_ai/topic4_linear_models/a4-demo-sarcasm-detection-with-logit.ipynb) `jupyter notebook`

Investigational scripts:

* [Full-Text search in SQLite](https://github.com/Extremesarova/experiments/blob/main/fts_sqlite.ipynb "fts_sqlite.ipynb") \
 It is a gentle demonstration of how [Full-Text search (FTS5) in SQLite](https://sqlite.org/fts5.html "SQLite documentation for FTS5") can be used to efficiently:
  * Search a large collection of documents for the subset that contain one or more instances of a search term.
  * Predict intents and classify text on mobile phones out of the box without using Tensorflow-lite and Pytorch for Mobile. Although it doesn't show great accuracy on large datasets, it can be used for small dataset with short phrases (commands, for example).
* [Demonstration](https://nbviewer.org/github/Extremesarova/experiments/blob/main/use_tf_lite_convertation.ipynb) of how to convert Universal Sentence Embedding Multilingual to tf-lite mode to use it for inference, for example, on mobile platforms like Android or iOS.  

Learning:

* [Self-paced mlcourse.ai](https://github.com/Extremesarova/experiments/tree/main/ods_mlcourse_ai)
* [Python Stepik Course](https://github.com/Extremesarova/experiments/tree/main/stepik_python)
