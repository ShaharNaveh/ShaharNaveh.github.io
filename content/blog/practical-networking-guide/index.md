---
title: Practical Networking Guide
date: 2024-07-13
draft: true
description: Networking concepts cheatsheet.
tags:
  - networking
---

Understanding basic networking concepts is important in today's digital world. It helps people know how data moves, fix connection problems, and keep communications secure.
Knowing these basics is key to using modern technology.

## Why this Post?
This post provides a concise overview of basic networking flow, designed as a "Networking for Dummies" guide rather than a deep dive.

## What is a Network?
A network is a group of two or more computers that are interconnected for the purpose of exchanging data.

## Network Types
There are many network types, but we are going to focus on two types: `LAN` and `WAN`

| | LAN | WAN |
| ---  | --- | --- |
| Stands For | Local Area Netowrk | Wide Area Network |
| What People Actually Mean | Private Network | The Internet |
| Example | Your Home/Office Network | The Internet |

{{< callout type="info" >}}
You can read more about available network types [here](https://en.m.wikipedia.org/wiki/Computer_network#Geographic_scale).
{{< /callout >}}

## IP Addressing
An IPv4 is comprised of 4 numbers separated by a dot, each of those numbers can be between 0-255.

```diff
+ 0.0.0.0 # Valid
+ 127.0.0.1 # Valid
+ 255.255.255.255 # Valid
- 256.256.256.256 # Invalid
```

<div class="highlight">
  <div class="chroma">
    <ul>
      <li><span class="gi">0.0.0.0</span> # Valid </li>
      <li><span class="gi">127.0.0.1</span> # Valid </li>
    </ul>
  </div>
</div>
