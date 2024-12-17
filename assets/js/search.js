---
layout: none
---
(function() {
  function sanitizeHTML(str) {
    const temp = document.createElement('div');
    temp.textContent = str;
    return temp.innerHTML;
  }

  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('search-results');

    if (results.length > 0) {
      let appendString = '';
      results.forEach(function(result) {
        const item = store[result.ref];
        appendString += `
          <li>
            <a href="${sanitizeHTML(item.url)}">
              <h3>${sanitizeHTML(item.title)}</h3>
            </a>
            <p>${sanitizeHTML(item.content.substring(0, 150))}...</p>
          </li>
        `;
      });
      searchResults.innerHTML = appendString;
    } else {
      searchResults.innerHTML = '<li>No results found</li>';
    }
  }

  function getQueryVariable(variable) {
    const query = window.location.search.substring(1);
    const vars = query.split('&');
    for (let i = 0; i < vars.length; i++) {
      const pair = vars[i].split('=');
      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, ' '));
      }
    }
    return null;
  }

  const store = {};
  {% for post in site.posts %}
    store["{{ post.url | slugify }}"] = {
      id: "{{ post.url | slugify }}",
      title: "{{ post.title | xml_escape }}",
      author: "{{ post.author | xml_escape }}",
      category: "{{ post.category | xml_escape }}",
      content: {{ post.content | strip_html | strip_newlines | jsonify }},
      url: "{{ post.url | xml_escape }}"
    };
  {% endfor %}

  {% for post in site.cases %}
    store["{{ post.url | slugify }}"] = {
      id: "{{ post.url | slugify }}",
      title: "{{ post.title | xml_escape }}",
      author: "{{ post.author | xml_escape }}",
      category: "{{ post.category | xml_escape }}",
      content: {{ post.content | strip_html | strip_newlines | jsonify }},
      url: "{{ post.url | xml_escape }}"
    };
  {% endfor %}

  {% for year in site.data.cves %}
    {%- for cve in year[1] -%}
      {% assign descriptions = cve[1]["containers"]["cna"]["descriptions"] | where: "lang", "en" | map: "value" %}
      store["{{ cve[0] }}"] = {
        id: "{{ cve[0] }}",
        title: {{ cve[1]["containers"]["cna"]["title"] | jsonify }},
        category: "cve",
        content: {{ descriptions | join: " " | jsonify }},
        url: "/cves/{{ cve[0] }}"
      };
    {%- endfor -%}
  {% endfor %}

  const searchTerm = sanitizeHTML(getQueryVariable('query'));
  if (searchTerm) {
    document.getElementById('search-box').setAttribute("value", searchTerm);

    const idx = lunr(function() {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('author');
      this.field('category');
      this.field('content');

      for (const key in store) {
        if (store.hasOwnProperty(key)) {
          this.add(store[key]);
        }
      }
    });

    const results = idx.search(searchTerm);
    displaySearchResults(results, store);
  }
})();