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
Every device on a network must be addressable. This means that it can be reached by referencing its address (usually an IPv4 address).

This IP address allows a device to communicate with another device using 
An IP address is associated with a computer's network interface 

An IPv4 is comprised of 4 numbers separated by a dot, each of those numbers can be between 0-255.

| IPv4 | Valid? |
| --- | --- |
| 0.0.0.0 | :white_check_mark: |
| 127.0.0.1 | :white_check_mark: |
| 255.255.255.255 | :white_check_mark: |
| 256.256.256.256 | :x: |

## Netmasks and Subnets 

## Network CIDR Notation
