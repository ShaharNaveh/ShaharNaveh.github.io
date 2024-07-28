---
title: Painless Git+SSH Setup
date: 2024-05-25
draft: false
type: docs
tags: 
  - git
  - ssh
---

{{< hextra/hero-subtitle >}}
How to configure SSH for git in an easy, painless way.
{{< /hextra/hero-subtitle >}}

<!---
In this guide, we'll walk you through the steps to generate an SSH key pair, add it to your Git account, and configure your local Git setup for seamless integration. 

By the end, you'll have a more efficient and secure Git environment that enhances your productivity and protects your code.
--->

## Why?
Setting up Git to use SSH can significantly enhance your workflow by providing a secure and convenient method for authenticating your repositories.
Whether you're a seasoned developer or new to version control, configuring Git with SSH keys streamlines the process of pushing and pulling code, eliminating the need to repeatedly enter your username and password.

## How?
{{< callout type="info" >}}
Although I will use GitHub as my Git hosting provider in this guide, this setup works for any other Git hosting provider. Just replace "github" with "gitlab," "bitbucket," etc.
{{< /callout >}}

### Create the `.ssh` Directory and SSH config
{{< tabs items="Linux/MacOS,Windows" >}}
  {{< tab >}}
  ```shell
  mkdir -p ~/.ssh/keys/
  touch ~/.ssh/config
  ```
  {{< /tab >}}

  {{< tab >}}
  ```powershell
  New-Item -ItemType Directory -Path "$env:UserProfile\.ssh\keys"
  New-Item -ItemType File -Path "$env:UserProfile\.ssh\config"
  ```
  {{< /tab >}}
{{< /tabs >}}

If everything went successfully, the `.ssh` directory tree will look like:

{{< filetree/container >}}
  {{< filetree/folder name=".ssh" >}}
    {{< filetree/file name="config" >}}
    {{< filetree/folder name="keys" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

{{< callout type="info" >}}
Creating the `.ssh/keys` directory helps manage multiple SSH keys if needed.
{{< /callout >}}

## Generate an SSH Key Pair
{{< tabs items="Linux/MacOS,Windows" >}}
  {{< tab >}}
  ```shell
  ssh-keygen -t ed25519 -b 4096 -a 100 -C private-pc -f ~/.ssh/keys/githb
  ```
  {{< /tab >}}

  {{< tab >}}
  ```powershell
  ssh-keygen.exe -t ed25519 -b 4096 -a 100 -C private-pc -f "$env:UserProfile\.ssh\keys\github" 
  ```
  {{< /tab >}}
{{< /tabs >}}

{{< callout type="info" >}}
You can set a password (recommended) or skip it by pressing `<Enter>` twice.
{{< /callout >}}

Now your `.ssh` tree will look like:
{{< filetree/container >}}
  {{< filetree/folder name=".ssh" >}}
    {{< filetree/file name="config" >}}
    {{< filetree/folder name="keys" >}}
      {{< filetree/file name="github" >}}
      {{< filetree/file name="github.pub" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

#### Explanation
- `-t`: Type of key, here `ed25519`.
- `-b`: Number of bits, here 4096.
- `-a`: Number of [KDF](https://en.m.wikipedia.org/wiki/Key_derivation_function) rounds, here 100.
- `-C`: Comment, defaults to `<username>@<computer name>`.
- `-f`: File location and name, here "github". This creates two files:
  * `.ssh/keys/github`: Private key.
  * `.ssh/keys/github.pub`: Public key.

{{< callout type="info" >}}
Read more about available configuration options for `ssh-keygen` [here](https://www.man7.org/linux/man-pages/man1/ssh-keygen.1.html).
{{< /callout >}}

### Create the SSH Config File
```xorg {filename=".ssh/config",linenos=table}
Host github.com
  Hostname github.com
  User git
  IdentityFile %d/.ssh/keys/github
  AddKeysToAgent yes
  RequestTTY no
  SessionType none
```

{{< callout type="info" >}}
Read more about available configuration options for `ssh_config` [here](https://man.openbsd.org/ssh_config).
{{< /callout >}}

#### Explanation
The key to the configuration is the first line: `Host github.com`. This tells SSH to use the defined settings whenever you connect to `github.com`:

```shell
ssh github.com
```

SSH will use the settings provided:
- `Hostname`: The address to connect to.
- `User`: The user to authenticate as, usually "git".
- `IdentityFile`: Path to the private key, `%d` is the user home directory.
- `AddKeysToAgent`: Adds the key to the ssh-agent, usful if the SSH key is password protected.
- `RequestTTY`: Set to `no` as no shell is needed.
- `SessionType`: Set to `none` since no commands are executed on the Git hosting provider.

### Add Your Key to the Git Hosting Provider
The general flow is:

{{% steps %}}

### Copy the SSH Public Key to Your Clipboard

```shell
cat ~/.ssh/keys/github.pub
# Then select and copy the displayed contents
```

{{% details title="Alternative Way" %}}
Alternatively, locate the hidden `.ssh` folder, open the file in a text editor, and copy it to your clipboard.
{{% /details %}}

### Add the Public Key to Your User's SSH Keys

{{% /steps %}}

Follow the instructions for your provider:

{{< hextra/feature-grid >}}
{{< hextra/feature-card icon="bitbucket" link="https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-linux/#Provide-Bitbucket-Cloud-with-your-public-key" title="Bitbucket" >}}
{{< hextra/feature-card icon="codeberg" link="https://docs.codeberg.org/security/ssh-key/" title="Codeberg" >}}
{{< hextra/feature-card icon="github" link="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account" title="Github" >}}
{{< hextra/feature-card icon="gitlab" link="https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account" title="Gitlab" >}}
{{< /hextra/feature-grid >}}

{{< callout type="warning" >}}
If your provider is not listed, please refer to their official documentation.
{{< /callout >}}

### Verify SSH Access
Run:

```shell
ssh github.com
```

If you don't get any errors, the setup is successful. 🥳

### Configure Git to Use SSH Instead of HTTPS
{{< tabs items="Bitbucket,Codeberg,Github,Gitlab" >}}
  {{< tab >}}
  ```shell
  git config --global url.ssh://git@bitbucket.org/.insteadOf https://bitbucket.org/
  ```
  {{< /tab >}}
  
  {{< tab >}}
  ```shell
  git config --global url.ssh://git@codeberg.org/.insteadOf https://codeberg.org/
  ```
  {{< /tab >}}
  
  {{< tab >}}
  ```shell
  git config --global url.ssh://git@github.com/.insteadOf https://github.com/
  ```
  {{< /tab >}}
  
  {{< tab >}}
  ```shell
  git config --global url.ssh://git@gitlab.com/.insteadOf https://gitlab.com/
  ```
  {{< /tab >}}
{{< /tabs >}}

{{< callout type="info" >}}
You can omit the `--global` flag while inside a git repository to configure that repository only 
{{< /callout >}}

## Tips & Tricks
### Set Private Key File Permissions
If you encounter:

> Permissions for 'private-key' are too open.

Run the following:

{{< tabs items="Linux/MacOS,Windows" >}}
  {{< tab >}}
  ```shell
  chmod 400 ~/.ssh/keys/github
  ```
  {{< /tab >}}

  {{< tab >}}
  ```powershell
  New-Variable -Name Key -Value "$env:UserProfile\.ssh\keys\github"
  Icacls $Key /c /t /Inheritance:d
  Icacls $Key /c /t /Grant ${env:UserName}:F
  Icacls $Key /c /t /Remove:g Administrator "Authenticated Users" BUILTIN\Administrators BUILTIN Everyone System Users
  Remove-Variable -Name Key
  ```
  {{< /tab >}}
{{< /tabs >}}

### Migrating to a Different Git Hosting Provider
To switch providers, change the `Hostname` and `IdentityFile` in the SSH config to the new provider and add a new `Host` block for it.

All existing repositories will point to the new provider, and new repositories will work as expected.

{{< details title="Migrate from Github to Codeberg Config Example" >}}
```xorg {filename=".ssh/config",linenos=table}
# Edit old "Host" block to automatically push code to new git hosting provider
Host github.com
  Hostname codeberg.org
  IdentityFile %d/.ssh/keys/codeberg
  # Rest of parameters

# New "Host" block to support new repositories
Host codeberg.org
  Hostname codeberg.org
  IdentityFile %d/.ssh/keys/codeberg
  # Rest of parameters
```
{{< /details >}}
