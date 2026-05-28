2024-09-26 17:59

Status: #baby

Tags: [[html]] [[webdev]] 

# How to add WoWhead tooltips to web pages


You just need this script here

`<script src="https://wow.zamimg.com/widgets/power.js" async></script>`.

In an .mdx file, you can just include it at the top. In standard html it should be enclosed with the `<head>`.

After that, all you need to do is just add a link to a Wowhead page, and when formatting the link, add the "wowhead" class as an attribute, like so:

`<a href="https://www.wowhead.com/spell=2948/scorch" class="wowhead">Scorch</a>`

Empty template:
```
<a href="https://www.wowhead.com/spell=/" class="wowhead"></a>
```


And it will properly display a tooltip on hover.


## Reference:
2024-09-26 17:59

Status: #baby 

Tags: [[guide]]



How to add WoWhead tooltips to web pages







## References:
