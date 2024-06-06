---
title: "CI/CD for your Résumé"
date: 2024-06-04
draft: true
description: Learn how to apply GitOps principals to your résumé
tags:
  - guide
---

In this guide I will show you how to setup [Github Actions](https://docs.github.com/en/actions) to generate your résumé and upload it to your [project release](https://docs.github.com/en/repositories/releasing-projects-on-github).

## How does it Work?
When you push changes to `main` a workflow starts, that workflow uses [pandoc](https://pandoc.org/) to convert `markdown` to `pdf`.

A diagram of the workflow looks like this: 

```mermaid
flowchart LR
  user([User])
  repository([Repository])
  action([Github Action])
  pandoc([Pandoc])
  markdown([Markdown])
  css([CSS])
  pdf([PDF file])
  release([Github Release])
  user-- git push -->repository
  repository-- trigger -->action
  subgraph Github Action [action]
    markdown-->pandoc
    css-->pandoc
    pandoc-- Converts -->pdf
    pdf-- Uploads --> release
  end
```

```mermaid
flowchart TD
    A[Developer pushes code] -->|git push| B[GitHub Repository]
    B --> C[GitHub Actions Triggered]
    C --> D[Checkout Repository]
    D --> E[Install Dependencies]
    E --> F[Convert Markdown to PDF using Pandoc]
    F --> G[Create GitHub Release]
    G --> H[Upload PDF to Release]

    subgraph GitHub Actions
        C
        D
        E
        F
        G
        H
    end
```

## Repository Layout
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
  {{< filetree/file name="Fname_Lname.md" >}}
{{< /filetree/container >}}

Let's discuss each file in more details:


### `Fname_Lname.md` 
This is where your résumé content goes, simply write your résumé in markdown format.

For example:

```markdown {filename="John_Doe.md"}
# John Doe

#### Senior developer that puts a lot of attention to security
###### [ [ john_doe@example.com ](mailto:john_doe@example.com) ] . [ [ +111-22-333-4444 ](tel:+111-22-333-4444) ] . [ [ Github ](https://github.com/ShaharNaveh/) ]

## Experience

### **Software Devloper @ Example Company** (1970-Preset)

Screamed at screens to get things done.

## Skills

- Version Control & CI/CD: Git, Github Actions

- Networking: Advanced expertise in networking and internet protocols

## Additional Information
- Languages: English(native), Italian(fluent)
```

### CSS
