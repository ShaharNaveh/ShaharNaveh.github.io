---
title: Painless Git+Ssh Setup
date: 2024-05-20T00:00:00-12:00
draft: false
---

# Test

{{< tabs tabTotal="3">}}
{{< tab tabName="Tab 1" >}}

**Tab 1 Content**

{{< /tab >}}
{{< tab tabName="Tab 2" >}}

**Tab 2 Content**

{{< /tab >}}
{{< tab tabName="Tab 3">}}

**Tab 3 Content**

{{< /tab >}}
{{< /tabs >}}


# Why?
Setting up Git to use SSH can significantly enhance your workflow by providing a secure and convenient method for authenticating your repositories. Whether you're a seasoned developer or new to version control, configuring Git with SSH keys streamlines the process of pushing and pulling code, eliminating the need to repeatedly enter your username and password. In this guide, we'll walk you through the steps to generate an SSH key pair, add it to your Git account, and configure your local Git setup for seamless integration. By the end, you'll have a more efficient and secure Git environment that enhances your productivity and protects your code.

# How?

```ssh-config
Host github.com
    Hostname github.com
    Foo Bar
```
