FAQ
===
<ul>
{% for p in site.pages%}
    {% if p.layout == "faq" %}
        <li><a href="{{p.url}}">{{ p.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>
