```{post} 2023-07-29
:author: "@rioschala"
:tags: tarea
:category: blog
:language: English
:location: Colombia
:excerpt: 1
```
# Task 2 @rioschala
# What's a pipeline? CI/CD 🔄️

In order to talk about pipelines, it's important to understand elements related to [***CI/CD.***](https://en.wikipedia.org/wiki/CI/CD) First, in general terms CI/CD relates to a continuous process of collaboration towards the creation of software where many people need to participate in. In overall, we need to keep into account two elements.

1. Small changes to main **(using MR)**
2. Continuous and automatic deployment **(Live site goes after every MR)**


```{figure} task-2-pipelines-hw.md-data/ci-cd-info.svg
---
alt: Infographic about CD/CI
---
[Source](https://www.synopsys.com/glossary/what-is-cicd.html)
```

## Why is this important?
When it comes to software development, I consider this methodology aims to focus all progress into one main lane where all can access the information, preview changes, and continue working on other features and issues.

## What happened in my [<t><span style="color:green;">pipeline</span></t>](https://gitlab.com/rioschala/main/-/jobs/4718989183)?🚩

```{figure} task-2-pipelines-hw.md-data/pipeline-mr-rioschala.png
---
alt: Pipeline rioschala
---
[Source](https://gitlab.com/rioschala/main/-/jobs/4718989183)
```

**What do I see?**
* Actions to check the site structure
* Create a VENV
* Detect problems with elements such as fonts (**Roboto is missing**)
* Read and write on some files
* Finish the job

```{figure} task-2-pipelines-hw.md-data/stages-pipeline.png
---
alt: Pipeline stages
---
[Source](https://alexmarket.medium.com/introducci%C3%B3n-a-ci-cd-con-gitlab-23d4e9cc6482)
```
## gitlab-ci.yml

This document is the one in charge to set the policies that define the pipeline process. In this one, python version is defined ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pipenv). Then, a VENV is created in order to build the site. Pipfile is read and all packages get updated. 

Site is built and integrated after that into `main`.

## MR Comments 
As an active member, it's important to contribute to the active development of the project. That's why, as developer, I get to comment on multiple MR from users to suggest, edit and improve changes from their branches. 

```{figure} task-2-pipelines-hw.md-data/comments-mr.png
---
alt: Comments examples on MR from users
---
[Source](https://gitlab.com/guayahack/main/-/merge_requests/55)
```

