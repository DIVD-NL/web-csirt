---
layout: none
---
(function() {
  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('search-results');

    if (results.length) { // Are there any results?
      var appendString = '';

      for (var i = 0; i < results.length; i++) {  // Iterate over the results
        var item = store[results[i].ref];
        appendString += '<li><a href="' + item.url + '"><h3>' + item.title + '</h3></a>';
        appendString += '<p>' + item.content.substring(0, 150) + '...</p></li>';
      }

      searchResults.innerHTML = appendString;
    } else {
      searchResults.innerHTML = '<li>No results found</li>';
    }
  }

  function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');

    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split('=');

      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      }
    }
  }

  store = {
    {% for post in site.posts %}
      "{{ post.url | slugify }}": {
        "id" : "{{ post.url | slugify }}",
        "title": "{{ post.title | xml_escape }}",
        "author": "{{ post.author | xml_escape }}",
        "category": "{{ post.category | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ post.url | xml_escape }}"
      },
    {% endfor %}
    {% for post in site.cases %}
      "{{ post.url | slugify }}": {
        "id" : "{{ post.url | slugify }}",
        "title": "{{ post.title | xml_escape }}",
        "author": "{{ post.author | xml_escape }}",
        "category": "{{ post.category | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ post.url | xml_escape }}"
      },
    {% endfor %}
    {% for post in site.cves %}
      "{{ post.url | slugify }}": {
        "id" : "{{ post.url | slugify }}",
        "title": "{{ post.title | xml_escape }}",
        {% if post.layout == "cve-json-50" %}
          "author": "{%- for c in post.json.containers.cna.credits -%}{{ c.value | xml_escape }} {% endfor %} {{ post.author | xml_escape }}",
        {% elsif post.layout == "cve-json-40" %}
          "author": "{%- for c in post.json.credit -%}{{ c.value | xml_escape }} {% endfor %} {{ post.author | xml_escape }}",
        {% else %}
          "author": "{{ post.author | xml_escape }}",
        {% endif %}
        "category": "{{ post.category | xml_escape }}",
        {% if post.layout == "cve-json-40" %}
          "content": {{ post.json.description.description_data[0].value | strip_html | strip_newlines | jsonify }},
        {% elsif post.layout == "cve-json-50" %}
          "content": {{ post.json.containers.cna.descriptions[0].value | strip_html | strip_newlines | jsonify }},
        {% else %}
          "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        {% endif %}
        "url": "{{ post.url | xml_escape }}"
      }
      {% unless forloop.last %},{% endunless %}
    {% endfor %}
  };

  var searchTerm = getQueryVariable('query');
  if (searchTerm) {
    document.getElementById('search-box').setAttribute("value", searchTerm);

    // Initalize lunr with the fields it will be searching on. I've given title
    // a boost of 10 to indicate matches on this field are more important.
    var idx = lunr(function () {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('author');
      this.field('category');
      this.field('content');

      for(var id in store) {
        this.add(store[id])
      }
    });

    /*
    for (var key in store) { // Add the data to lunr
      idx.add({
        'id': key,
        'title': window.store[key].title,
        'author': window.store[key].author,
        'category': window.store[key].category,
        'content': window.store[key].content
      });
    */

    var results = idx.search(searchTerm); // Get lunr to perform a search
    displaySearchResults(results, store); // We'll write this in the next section
  }
})();