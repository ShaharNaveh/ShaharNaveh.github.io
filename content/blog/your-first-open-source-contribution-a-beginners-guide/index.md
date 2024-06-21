---
title: "Your First Open Source Contribution: A Beginner's Guide"
date: 2024-06-21
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

- Professional: You will get your code reviews from more experienced maintainers & developers.
  
- Responsive: When you make your first pull request your [impostor syndrome](https://en.m.wikipedia.org/wiki/Impostor_syndrome) will probably kick in, it's not so fun to wait an entire week (or more) for feedback.
  
- Organized: Usually the project will have a clear roadmap of what should be worked on, and the issue's description will be more descriptive.

### Labels are your Friend 
Some projects will put labels on  their issues, this can help you out with picking an issue that is more appropriate to you.
For example some projects have a label called `Good First Issue` (or similar), those issues are quick & easy to fix and the reason why the maintainers haven't done them themselves is to give new people something lightweight to get started.

## Local Development Perquisites 
### Making a Fork
After you choose your project you will need to fork it. Why? because you don't have write access to their repository.

after you mad the fork, you need to clone your fork, for example if I forked [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife), and my GitHub username is `ShaharNaveh` I will run the following command:

```bash
git clone https://github.com/octocat/Spoon-Knife
```

After that I will add the original repo as a [git remote](https://git-scm.com/docs/git-remote) and will call it `upstream` (you can choose a different name):

```bash
# cd into your project directory first
git remote add upstream https://github.com/octocat/Spoon-Knife
```

