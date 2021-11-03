---
title: "Venv in Depth"
date: 2021-11-03T00:56:09+02:00
draft: true
author: ["Shahar Naveh"]
---

## Agenda

In this post we are going to talk about what are python virtual environments (venv), why do we need them, how to use them and we will also understand how they work under the hood.

## Why venv

Python project will sometimes use packages that are not part of the python stdlib.
Also, projects will sometimes need a specific version of a package, because they are relying on a ~bug~ feature that only exists in that specific version of that package, maybe they use the specific version for stability reasons.

Because python does not support importing a specific version of a package, like for example in golang:

{{< highlight go "linenos=table" >}}
import (

    "fmt"

    errors081 "github.com/pkg/errors/081"

    errors091 "github.com/pkg/errors/091"

)

func main() {

    err := errors081.New("New error for v0.8.1")

    fmt.Println(err)

    err = errors091.New("New error for v0.9.1")

    fmt.Println(err)

}
{{< /highlight >}}

Also, because only one version of a package can exists in the evironment, it means that it **may** not be possible to satisfy the requirements of every project on the system, for example:

| Project/Dependency | pandas |
| :-: | :-: |
| Foo | > 1.0.0 |
| Bar | < 0.9.0 |

Here we have a table represents the dependecies for each project, and as we can see there is no way to satisfy the requirements of both projects having only one evironment (the system's python environment).

The solution is to create a virtual environment.

> Every time a user installs a package on the global python environment, a puppy gets slapped until it's cooked. Abraham Lincoln

## What is a python virtual environment

A python virtual environmet is a self-contained directory, that include an installation of python and some pre-installed packages like [pip](https://pip.pypa.io/en/stable/) and [setuptools](https://setuptools.pypa.io/en/latest/).

The python version of the venv will be the same version as the python that was used to create the venv, so if you have multiple versions of python installed on your system, make sure to pick the right one (`python3.9`, `python3.10`, etc).

## How to work with venv

In order to create a venv, run:

{{< highlight bash >}} python3 -m venv venv-in-depth {{< /highlight >}}

breakdown:

* `python3.9`: Using python 3.9 to create the venv

* `-m venv`: Using the venv module

* `venv-in-depth`: Name for the venv

Creating the venv is not enough, in order to use it (we will talk about why is that in a second) we need to activate the venv.



To activate the venv:
