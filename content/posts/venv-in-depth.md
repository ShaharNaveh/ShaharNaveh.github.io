---
title: "Venv in Depth"
date: 2021-11-03T00:56:09+02:00
draft: false
---

# Venv in depth

In this post we are going to talk about:

* Why we need virtual environments

* What are virtual environments

* How to work with virtual environments

* How the virtual environment works under the hood

---

## Why virtual environmet

Python project will sometimes use packages that are not part of the python stdlib.
Also, projects will sometimes need a specific version of a package, because they are relying on a ~bug~ feature that only exists in that specific version of that package, maybe they use the specific version for stability reasons.

Because python does not support importing a specific version of a package, like for example in golang:

```golang
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
```

Also, because only one version of a package can exists in the evironment, it means that it **may** not be possible to satisfy the requirements of every project on the system, for example:

| Project/Dependency | pandas |
| :-: | :-: |
| Foo | > 1.0.0 |
| Bar | < 0.9.0 |

Here we have a table represents the dependecies for each project, and as we can see there is no way to satisfy the requirements of both projects having only one evironment.

The solution is to create a virtual environment.

> Every time a user installs a package on the global python environment, a puppy gets slapped until it's cooked. Abraham Lincoln

---

## What is a python virtual environment

Python virtual environmet is a self-contained directory, that include an installation of python of a specific version (defaults to the version of python that was used to create the virtual environment), and usually comes with pre-installed packages like: pip and setuptools
