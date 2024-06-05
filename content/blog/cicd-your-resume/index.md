---
title: "CI/CD for your Résumé"
date: 2024-06-04
draft: true
description: Learn how to apply GitOps principals to your résumé
tags:
  - guide
---

In this guide I will show you how to setup [Github Actions](https://docs.github.com/en/actions) to generate your résumé and upload it to your [project release](https://docs.github.com/en/repositories/releasing-projects-on-github).

## Repository File Tree
The basic file tree that we will create will look like: 

{{< filetree/container >}}
  {{< filetree/folder name=".github" >}}
    {{< filetree/folder name="workflows" >}}
      {{< filetree/file name="build.yaml" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
  {{< filetree/folder name="css" >}}
    {{< filetree/file name="default.css" >}}
    {{< filetree/file name="normalize.css" >}}
  {{< /filetree/folder >}}
  {{< filetree/file name="Justfile" >}}
  {{< filetree/file name="fname_lname.md" >}}
{{< /filetree/container >}}
