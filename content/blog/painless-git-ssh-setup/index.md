---
title: Painless Git+Ssh Setup
date: 2024-05-20T00:00:00-12:00
draft: false
---

In this guide, we'll walk you through the steps to generate an SSH key pair, add it to your Git account, and configure your local Git setup for seamless integration. 

By the end, you'll have a more efficient and secure Git environment that enhances your productivity and protects your code.

## Why?

Setting up Git to use SSH can significantly enhance your workflow by providing a secure and convenient method for authenticating your repositories. Whether you're a seasoned developer or new to version control, configuring Git with SSH keys streamlines the process of pushing and pulling code, eliminating the need to repeatedly enter your username and password.

## How?

### Create the `.ssh` directory 

{{< tabs items="Linux/MacOS,Windows" >}}

  {{< tab >}}
  ```bash
  mkdir -p ~/.ssh/keys/
  ```
  {{< /tab >}}

  {{< tab >}}
  ```powershell
  New-Item -Type Directory -Path "$env:USERPROFILE\.ssh\keys" 
  ```
  {{< /tab >}}

{{< /tabs >}}

{{< callout type="info" >}}

  We created `.ssh/keys` as well. this will help to manage multiple ssh keys when needed.
  
{{< /callout >}}


### Generate an ssh key
{{< tabs items="Linux/MacOS,Windows" >}}

  {{< tab >}}
  ```bash
  ssh-keygen -t ed25519 -C private-pc -f ~/.ssh/keys/github
  ```
  {{< /tab >}}

  {{< tab >}}
  ```powershell
  ssh-keygen.exe -t ed25519 -C private-pc -f "$env:USERPROFILE\.ssh\keys\github" 
  ```
  {{< /tab >}}

{{< /tabs >}}

#### Explanation
- `-t`: Type, here we choose `ed25519`.
- `-C`: Comment, defaults to `<username>@<computer name>`, you can omit this.
- `-f`: File location, here I've chosen "github", but you can give it whatever name you desire.
