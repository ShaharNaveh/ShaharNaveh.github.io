---
title: Painless Git+SSH Setup
date: 2024-05-20T00:00:00-12:00
draft: false
---

In this guide, we'll walk you through the steps to generate an SSH key pair, add it to your Git account, and configure your local Git setup for seamless integration. 

By the end, you'll have a more efficient and secure Git environment that enhances your productivity and protects your code.

# Why?
Setting up Git to use SSH can significantly enhance your workflow by providing a secure and convenient method for authenticating your repositories. Whether you're a seasoned developer or new to version control, configuring Git with SSH keys streamlines the process of pushing and pulling code, eliminating the need to repeatedly enter your username and password.

# How?
{{< callout type="info" >}}
In this post I will use github as my VCS provider, but this setup works for any other VCS provider, just replace "github" with gitlab/bitbucket/etc and it will work.
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
  New-Item -Type Directory -Path "$env:USERPROFILE\.ssh\keys" 
  ```
  {{< /tab >}}
{{< /tabs >}}

{{< callout type="info" >}}
We created `.ssh/keys` as well. this will help to manage multiple SSH keys if needed.
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
  ssh-keygen.exe -t ed25519 -b 4097 -C private-pc -f "$env:USERPROFILE\.ssh\keys\github" 
  ```
  {{< /tab >}}
{{< /tabs >}}

{{< callout type="info" >}}
You can configure a password (recommended) or skip it by hitting `<Enter>` twice.
{{< /callout >}}

### Explanation
- `-t`: Type, here we choose `ed25519`.
- `-b`: Bytes, Number of bytes to generate the key pair with.
- `-C`: Comment, defaults to `<username>@<computer name>`, you can omit this.
- `-f`: File location, we choose "github". Replace this with whatever name you desire. In this example two files will be created:
  * `.ssh/keys/github`: Private key.
  * `.ssh/keys/github.pub`: Public key.

## Set private key file permissions

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
You can read more about the available configuration options [here](https://man.openbsd.org/ssh_config).
{{< /callout >}}

### Explanation
The "secret sauce" for the configuration lies in the very first line: `Host github.com`. We tell SSH to define a host alias named "github.com", so when we run:

```shell
ssh github.com
```

SSH will automatically connect to the defined `Hostname` (which is "github.com"), with the rest of the arguments such as the user, private-key and so on.

- `Host`: This what allows us to start using SSH without changing the [remote origin](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes).
- `Hostname`: The address to connect to, we set it to be the same as `Host`.
- `User`: User to authenticate as. usually it's "git".
- `IdentityFile`: Path to the private key. ssh will interpret `%d` as the user home directory.
- `AddKeysToAgent`: Pretty much only useful if you set a password for your ssh key in [here](#generate-an-ssh-key).
- `RequestTTY`: We set this to `no`, as we aren't planning on getting a shell.
- `SessionType`: Setting this to `none`, as we will not execute any commands on our VCS provider.

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
## Migrating to a different VCS provider 
Simply change the `Hostname` address to you new VCS provider (assuming that you only changed the provider), and append a second `Host` block for your new provider.

All the old repositories will point to the new VCS provider, and new repositories will work as expected.
