# Medium-Blog-Bot-V2

[How I Built a Self-Updating Blog Catalog Using a Bot — Part 2](https://levelup.gitconnected.com/how-i-built-a-self-updating-blog-catalog-using-a-bot-part-2-a67968be5f42)

1. Run this in your developer console

```js
posts = []

Array.prototype.forEach.call(document.getElementsByClassName("fo fp ff s"), function(post) {
    postObj = {};
    postObj.title = post.getElementsByTagName("a")[0].innerText;
    postObj.link = post.getElementsByTagName("a")[0].href;
    postObj.pubDate = post.getElementsByClassName("ca")[1].innerText;
    posts.unshift(postObj);
});

cleanPosts = [];
Array.prototype.forEach.call(posts, function(post) {
    post.link = post.link.replace("?source=your_stories_page-------------------------------------", "");
    post.pubDate = post.pubDate.replace("on", "");
    post.pubDate = post.pubDate.includes(",") ? new Date(post.pubDate) : new Date(post.pubDate+" "+new Date().getFullYear());
    post.pubDate = post.pubDate.toISOString().replace('T', ' ').substr(0, 19)
    cleanPosts.push(post);
});

var jsonData = JSON.stringify(cleanPosts, null, "\t");
console.log(jsonData);
```
