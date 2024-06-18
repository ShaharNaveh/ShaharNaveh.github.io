---
title: "Your First Open Source Contribution: A Beginner's Guide"
date: 2024-06-18
draft: true
description: This article provides a beginner's guide to making your first open source contribution, covering project selection and the submission process
tags:
  - guide
---

Contributing to open source projects can be transformative for both novice and seasoned developers. It enhances your skills, provides real-world experience, expands your professional network, and allows you to give back to the community. However, making that first contribution can be daunting. This guide will help you navigate the initial steps, from selecting a project that aligns with your interests to successfully submitting your first pull request, ensuring you can confidently engage with the open source ecosystem.

## Creating an Account on a Git Hosting Platform

While there are many git hosting platforms such as [Bitbucket](https://bitbucket.org/), [Gitlab](https://gitlab.com/), and [Github](https://github.com/), **Github** is the leading platform for hosting most open-source projects.

[Create a Github account](https://github.com/signup) and proceed to the next step.

## Configuring Git
While there are many GUI based programs that makes working with git easier, I would recommend using the CLI as it will help to better understand what goes on behind the scenes.

Here's a quick guide on how to configure the git CLI:

{{< cards >}}
{{< card link="/blog/painless-git-ssh-setup/" title="Configuring Git Guide" >}}
{{< /cards >}} 

## Discovering Projects

{{< callout >}}
If you already have a project in mind, you can skip this step.
{{< /callout >}}

Github has a few neat features that allows anyone at any skill level to discover new projects that might interest you:

{{< hextra/feature-grid >}}

{{< hextra/feature-card
    title="Explore"
    icon="github"
    link="https://github.com/explore"
    subtitle="Discover what's popular on GitHub today"
>}}

{{< hextra/feature-card
    title="Topics"
    icon="github"
    link="https://github.com/topics"
    subtitle="Find and explore topics on GitHub"
>}}


{{< hextra/feature-card
    title="Trending"
    icon="github"
    link="https://github.com/trending"
    subtitle="Explore the most popular and exciting projects on GitHub"
>}}

{{< /hextra/feature-grid >}}

## Tips for Choosing a Project 
### Go for the Bigger Projects
Beginners often think things like:

> I'll pick a small project so I won't affect a lot of people with my bad code.

> I'll go for a smaller project where it's easier to navigate the codebase.

> I want more small "family" like community rather than cold & industrial atmosphere.

But those arguments are very naive and often not true.

As a matter of fact you want to contribute to the large projects because:

- Professional: you will get your code reviews from more experienced maintainers & developers.
- Activity: when you make your first pull request your [impostor syndrome](https://en.m.wikipedia.org/wiki/Impostor_syndrome) will probably kick in, it's not fun to wait an entire week (or more) for feedback.
- Organized: Usually they will have a clear roadmap of what should be worked on, and the issue's description will be more descriptive.
