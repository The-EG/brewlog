{% assign posts = site.posts | where: "title", {{page.title}} %}

{% if posts.size > 1 %}
### Other Brews

{% for post in posts %}
{% if post.id == page.id %}{% continue %}{% endif %}
 - [{{post.date | date: site.minima.date_format}}]({{post.url}})
{% endfor %}
{% endif %}
