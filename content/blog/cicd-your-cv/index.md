---
title: "CI/CD for your CV"
date: 2024-06-04
draft: false
description: Learn how to apply GitOps principals to your CV generation process
tags:
  - guide
---

In this guide I will show you how to setup [Github Actions](https://docs.github.com/en/actions) to generate your CV and upload it to your [project release](https://docs.github.com/en/repositories/releasing-projects-on-github).

## How does it Work?
When you push changes to `main` a workflow starts, that workflow uses [pandoc](https://pandoc.org/) to convert `markdown` to `pdf`.

A diagram of the workflow looks like this: 

```mermaid
flowchart TD
  user([User])
  repository([Repository])
  action([Github Action])
  dependencies["Install Dependencies"]
  pandoc([Pandoc])
  markdown([Markdown])
  css([CSS])
  pdf([PDF file])
  release([Github Release])

  subgraph push [" "]
    user-- git push -->repository
  end
 
  subgraph action [Github Actions]
    dependencies-->pandoc
    pandoc-- Converts -->pdf
    pdf-- Uploads -->release

    subgraph assets [Assets]
      markdown & css
    end
  end

push-- trigger -->action
assets-->pandoc
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
  {{< filetree/folder name="markdown" >}}
    {{< filetree/file name="Fname_Lname.md" >}}
  {{< /filetree/folder >}}
  {{< filetree/file name="Justfile" >}}
{{< /filetree/container >}}

Let's discuss each file and directory in more details:

### `markdown` Directory 
Let's you define multiple versions for your CV. 

Let's say you have a CV for a developer role and also a CV for a sysadmin role,
while you can technically have separate git branches, I found that it's not convenient to deal with branches when you want to edit shared assets like the CSS or workflow file.

#### `Fname_Lname.md` 
This is where your CV content goes. Simply write your CV in markdown format.

For example:

```markdown {filename="markdown/John_Doe.md"}
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
If we look at the [repository layout](#Repository-Layout) again you'll see two `.css` files: 

#### `normalize.css`
CSS file that ensures all components renders the same, no matter which browser it was opened in.

You can grab the latest version [here](https://necolas.github.io/normalize.css/) 

#### `default.css`
Where the actual styling goes. This is where you decide on things like:

- Background Color
- Font Family
- Font Size

And a lot more.

The first line of this CSS file is just importing `normalize.css`:

```css
@import "normalize.css";
```

{{< callout type="info" >}}
You can grab a base `default.css` file [here](assets/default.css).
{{< /callout >}}

### Justfile
Configuration file for [just](https://github.com/casey/just).

In short, it let's us save and run predefined commands easily.
