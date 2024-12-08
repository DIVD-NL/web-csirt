---
layout: none
---
(function() {
  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('search-results');

    if (results.length) {
      var appendString = '';
      for (var i = 0; i < results.length; i++) {
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

  var store = {
    {% for post in site.posts %}
      "{{ post.url | slugify }}": {
        "id": "{{ post.url | slugify }}",
        "title": "{{ post.title | xml_escape }}",
        "author": "{{ post.author | xml_escape }}",
        "category": "{{ post.category | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ post.url | xml_escape }}"
      },
    {% endfor %}
    {% for post in site.cases %}
      "{{ post.url | slugify }}": {
        "id": "{{ post.url | slugify }}",
        "title": "{{ post.title | xml_escape }}",
        "author": "{{ post.author | xml_escape }}",
        "category": "{{ post.category | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ post.url | xml_escape }}"
      },
    {% endfor %}
    {% for year in site.data.cves %}
      {%- for cve in year[1] -%}
      {% assign cveId = cve[0] -%}
      {% assign descriptions = cve[1]["containers"]["cna"]["descriptions"] | where: "lang", "en" | map: "value" %}
        "{{ cve[0] }}": {
          "id": "{{ cve[0] }}",
          "title": {{ cve[1]["containers"]["cna"]["title"] | jsonify }},
          "category": "cve",
          "content": {{ descriptions | join: " " | jsonify }},
          "url": "/cves/{{ cve[0] }}"
        }
      {%- unless forloop.last -%},{%- endunless %}
      {%- endfor -%}
    {% endfor %}
  };

  var searchTerm = getQueryVariable('query');
  if (searchTerm) {
    document.getElementById('search-box').setAttribute("value", searchTerm);

    var idx = lunr(function () {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('author');
      this.field('category');
      this.field('content');

      for(var id in store) {
        this.add(store[id]);
      }
    });

    var results = idx.search(searchTerm);
    displaySearchResults(results, store);
  }
})();
