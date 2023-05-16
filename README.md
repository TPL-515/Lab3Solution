# Lab 3

For this lab we will be manipulating upstream and downstream tasks. This should help you to be able to manipulate the order of assets within the pipeline.

## Getting Started

First clone the lab locally and install the dependencies like so:

```bash
git clone git@github.com:TPL-515/Lab3.git
cd Lab3/
pip install -e ".[dev]"
```

This should install all of the required dependencies for the lab.

## Running the Lab

In order to run the lab just run the following command:

```bash
dagster dev
```

From here you should be able to navigate to the UI hosted at: http://localhost:3000

## Lab Tasks

For this lab you will be asked to perform the following tasks

1) Verify that the assets run first within the U.I.

2) Change the order of the assets so that it goes run, walk, crawl.

3) Validate that the order is changed in the U.I.
