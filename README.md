# Experiments
This is a repository with some useful information. \
Let's describe it shortly:
 - [Full-Text search in SQLite](https://github.com/Extremesarova/experiments/blob/main/fts_sqlite.ipynb "fts_sqlite.ipynb") \
 It is a gentle demonstration of how [Full-Text search (FTS5) in SQLite](https://sqlite.org/fts5.html "SQLite documentation for FTS5") can be used to efficiently:
   - Search a large collection of documents for the subset that contain one or more instances of a search term.
   - Predict intents and classify text on mobile phones out of the box without using Tensorflow-lite and Pytorch for Mobile. Although it doesn't show great accuracy on large datasets, it can be used for small dataset with short phrases (commands, for example).
 - [NLP Stepik Course](https://github.com/Extremesarova/experiments/tree/main/NLP%20Course%20Stepik "Homework for NLP course from Stepik") \
Here I post my homework code and formulation of tasks [ENG] from [the course [RUS]](https://stepik.org/course/54098/info, "Stepik NLP Course"). 
 - use_tf_lite_conversation.ipynb
It is a demonstration of how to convert Universal Sentence Embedding Multilingual to tf-lite mode to use it for inference, for example, on mobile platforms like Android or iOS. 