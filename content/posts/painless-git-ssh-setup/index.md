---
title: "Painless Git+Ssh Setup"
date: 2024-05-20T00:00:00-12:00
draft: false 
---

# Title 1
text 

# Title 2
foo

{{< tabs >}}
{{% tab name="python" %}}
```python
print("Hello World!")
```
{{% /tab %}}
{{% tab name="R" %}}
```R
> print("Hello World!")
```
{{% /tab %}}
{{% tab name="Bash" %}}
```Bash
echo "Hello World!"
```
{{% /tab %}}
{{< /tabs >}}

Tab views with the same tabs that belong to the same group sychronize their selection:

{{< tabs >}}
{{% tab name="python" %}}
```python
print("Hello World!")
```
{{% /tab %}}
{{% tab name="R" %}}
```R
> print("Hello World!")
```
{{% /tab %}}
{{% tab name="Bash" %}}
```Bash
echo "Hello World!"
```
{{% /tab %}}
{{< /tabs >}}

## Config example

	{{</* tabs groupId="config" */>}}
	{{%/* tab name="json" */%}}
	```json
	{
	  "Hello": "World"
	}
	```
	{{%/* /tab */%}}
	{{%/* tab name="XML" */%}}
	```xml
	<Hello>World</Hello>
	```
	{{%/* /tab */%}}
	{{%/* tab name="properties" */%}}
	```properties
	Hello = World
	```
	{{%/* /tab */%}}
	{{</* /tabs */>}}

Renders as:

{{< tabs groupId="config" >}}
{{% tab name="json" %}}
```json
{
  "Hello": "World"
}
```
{{% /tab %}}
{{% tab name="XML" %}}
```xml
<Hello>World</Hello>
```
{{% /tab %}}
{{% tab name="properties" %}}
```properties
Hello = World
```
{{% /tab %}}
{{< /tabs >}}
