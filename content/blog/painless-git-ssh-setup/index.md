---
title: Painless Git+SSH Setup
date: 2024-05-25T00:00:00-12:00
draft: true
---

In this guide, we'll walk you through the steps to generate an SSH key pair, add it to your Git account, and configure your local Git setup for seamless integration. 

By the end, you'll have a more efficient and secure Git environment that enhances your productivity and protects your code.

# Why?
Setting up Git to use SSH can significantly enhance your workflow by providing a secure and convenient method for authenticating your repositories. Whether you're a seasoned developer or new to version control, configuring Git with SSH keys streamlines the process of pushing and pulling code, eliminating the need to repeatedly enter your username and password.

# How?
{{< callout type="info" >}}
Although I will use GitHub as my VCS provider in this guide, this setup works for any other VCS provider. Just replace "github" with "gitlab," "bitbucket," etc.
{{< /callout >}}

## Create the `.ssh` directory 
{{< tabs items="Linux/MacOS,Windows" >}}
  {{< tab >}}
  ```shell
  mkdir -p ~/.ssh/keys/
  ```
  {{< /tab >}}

  {{< tab >}}
  ```powershell
  New-Item -Type Directory -Path "$env:UserProfile\.ssh\keys" 
  ```
  {{< /tab >}}
{{< /tabs >}}

{{< callout type="info" >}}
Creating the .ssh/keys directory helps manage multiple SSH keys if needed.
{{< /callout >}}

## Generate an SSH key
{{< tabs items="Linux/MacOS,Windows" >}}
  {{< tab >}}
  ```shell
  ssh-keygen -t ed25519 -b 4096 -C private-pc -f ~/.ssh/keys/githb
  ```
  {{< /tab >}}

  {{< tab >}}
  ```powershell
  ssh-keygen.exe -t ed25519 -b 4097 -C private-pc -f "$env:UserProfile\.ssh\keys\github" 
  ```
  {{< /tab >}}
{{< /tabs >}}

{{< callout type="info" >}}
You can set a password (recommended) or skip it by pressing `<Enter>` twice.
{{< /callout >}}

### Explanation
- `-t`: Type of key, here `ed25519`.
- `-b`: Number of bits, here 4096.
- `-C`: Comment, defaults to `<username>@<computer name>`.
- `-f`: File location and name, here "github". This creates two files:
  * `.ssh/keys/github`: Private key.
  * `.ssh/keys/github.pub`: Public key.

## Create the SSH config file
{{< tabs items="{Linux/MacOS,Windows" >}}
  {{< tab >}}
  ```ssh-config {linenos=table,linenostart=1,filename=".ssh/config"}
  Host github.com
    Hostname github.com
    User git
    IdentityFile "%d/.ssh/keys/github"
    AddKeysToAgent yes
    RequestTTY no
    SessionType none
  ```
  {{< /tab >}}

  {{< tab >}}
  ```ssh-config {linenos=table,linenostart=1,filename=".ssh\config"}
  Host github.com
    Hostname github.com
    User git
    IdentityFile "%d/.ssh/keys/github"
    AddKeysToAgent yes
    RequestTTY no
    SessionType none
  ```
  {{< /tab >}}
{{< /tabs >}}

{{< callout type="info" >}}
Read more about available configuration options [here](https://man.openbsd.org/ssh_config).
{{< /callout >}}

### Explanation
The key to the configuration is the first line: `Host github.com`. This tells SSH to use the defined settings whenever you connect to `github.com`:

```powershell
ssh github.com
```

SSH will use the settings provided:
- `Hostname`: The address to connect to.
- `User`: The user to authenticate as, usually "git".
- `IdentityFile`: Path to the private key, with %d as the user home directory.
- `AddKeysToAgent`: Adds the key to the ssh-agent, usful if the SSH key is password protected.
- `RequestTTY`: Set to no as no shell is needed.
- `SessionType`: Set to none since no commands are executed on the VCS provider.

## Add your key to the VCS provider
Here it really depends on your provider, choose the appropriate one:

- [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-linux/#Provide-Bitbucket-Cloud-with-your-public-key)
- [Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account)
- [Gitlab](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account)

{{< callout type="warning" >}}
If your provider does not appear here, please refer to their official documentation.
{{< /callout >}}

They might be a bit different but they all are following the same steps:

{{% steps %}}

### Copy the SSH public key to your clipboard.

```shell
cat ~/.ssh/keys/github.pub
# Then select and copy the contents of the file
# displayed in the terminal to your clipboard
```

{{% details title="Alternative way" closed="true" %}}
Alternatively, you can locate the hidden `.ssh` folder, open the file in your favorite text editor, and copy it to your clipboard.
{{% /details %}}

### Add the public key to your user's SSH keys.

{{% /steps %}}

## Verify SSH access
If when running:

```shell
ssh github.com
```

You don't get any errors, then everything went fine 🥳

## Configure Git to use SSH instead of https
{{< tabs items="Bitbucket,Gitlab,Github" >}}
  {{< tab >}}
  ```shell
  git config --global url.ssh://git@bitbucket.org/.insteadOf https://bitbucket.org/
  ```
  {{< /tab >}}

  {{< tab >}}
  ```shell
  git config --global url.ssh://git@gitlab.com/.insteadOf https://gitlab.com/
  ```
  {{< /tab >}}

  {{< tab >}}
  ```shell
  git config --global url.ssh://git@github.com/.insteadOf https://github.com/
  ```
  {{< /tab >}}
{{< /tabs >}}

# Tips & Tricks 
## Set private key file permissions 
If you get errors related to 
> Permissions for 'private-key' are too open.

Simply run the following:
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

## Migrating to a different VCS provider 
Simply change the `Hostname` address to you new VCS provider (assuming that you only changed the provider), and append a second `Host` block for your new provider.

All the old repositories will point to the new VCS provider, and new repositories will work as expected.
