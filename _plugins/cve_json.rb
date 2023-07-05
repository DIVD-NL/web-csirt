module CveJson
  @@log = Logger.new(STDERR)  # Could send output to STDOUT
  @@log.level = Logger::WARN
  @@log.progname = 'CveJson'
  @@log.formatter = proc { |severity, datetime, progname, msg|
    "#{severity} #{progname}: #{msg}\n"
  }

  def self.log
    @@log
  end

  class CveJson40Generator < Jekyll::Generator
    safe true



    def generate(site)
      # Get all the documents in collection cves
      site.collections.each do |n, collection|
        if n == "cves" then
          collection.docs.each do | doc |
            if doc.data["layout"] == "cve-json-40"
              # Get data
              cve = doc.data["json"]["CVE_data_meta"]["ID"]
              if doc.data["json"]["CVE_data_meta"].key?("TITLE") then
                title = doc.data["json"]["CVE_data_meta"]["TITLE"]
              else
                doc.data["json"]["description"]["description_data"].each do | d |
                  if d["lang"] == "eng" then
                    title = d["value"]
                    break
                  end
                end
              end
              CveJson.log.info "Title: #{title}"        
              # Set additional attributes
              doc.data["cve"] = cve
              doc.data["title"] = title
              doc.data["redirect_from"] = [ "/#{cve}/" ]
              # Create JSON page too
              site.pages << CveJson40Page.new(site, doc.data["json"])
            elsif doc.data["layout"] == "cve-json-50"
              # Get data
              cve = doc.data["json"]["cveMetadata"]["cveId"]
              if doc.data["json"]["containers"]["cna"].key?("title")
                title = doc.data["json"]["containers"]["cna"]["title"]
              elsif doc.data.key?("title")
                title = doc.data["title"]
              else
                title = doc["title"]
              end
              CveJson.log.info "Title: #{title}"        
              # Set additional attributes
              doc.data["cve"] = cve
              doc.data["title"] = title
              doc.data["redirect_from"] = [ "/#{cve}/" ]
              # Create JSON page too
              site.pages << CveJson50Page.new(site, doc.data["json"])
            elsif doc.data["layout"] == "cve" then
              CveJson.log.info doc.basename_without_ext
              cve = doc.basename_without_ext
              unless doc.data.key?("cve") then
                doc.data["cve"] = cve
              end
              unless doc.data.key?("redirect_from")  then
                doc.data["redirect_from"] = [ "/#{cve}/" ]
              end
            end
          end
        end

      end
    end
  end

  # Subclass of `Jekyll::Page` with custom method definitions.
  class CveJson40Page < Jekyll::Page
    def initialize(site, data)
      # Generate a new document with layout cve-json-40-json in /cves based on the original one.
      CveJson.log.info "Creating a JSON file for #{ data["CVE_data_meta"]["ID"]}"
      @site = site             # the current site instance.
      @base = site.source      # path to the source directory.
      @dir  = "cves"           # the directory the page will reside in.
      
      # All pages have the same filename, so define attributes straight away.
      @basename = data["CVE_data_meta"]["ID"]      # filename without the extension.
      @ext      = '.json'      # the extension.
      @name     = "#{@basename}#{ext}" # basically @basename + @ext.

      # Initialize data hash with the new layout and the origina json data
      @data = {
        'json' => data,
        'layout' => 'cve-json'
      }


      ## Look up front matter defaults 
      data.default_proc = proc do |_, key|
        site.frontmatter_defaults #.find(relative_path, :categories, key)
      end
    end

    # Placeholders that are used in constructing page URL.
    def url_placeholders
      {
        :path       => @dir,
        :basename   => basename,
        :output_ext => output_ext,
      }
    end
  end

  # Subclass of `Jekyll::Page` with custom method definitions.
  class CveJson50Page < Jekyll::Page
    def initialize(site, data)
      # Generate a new document with layout cve-json-40-json in /cves based on the original one.
      CveJson.log.info "Creating a JSON file for #{ data['cveMetadata']['cveId'] }"
      @site = site             # the current site instance.
      @base = site.source      # path to the source directory.
      @dir  = "cves"           # the directory the page will reside in.
      
      # All pages have the same filename, so define attributes straight away.
      @basename = data["cveMetadata"]["cveId"]      # filename without the extension.
      @ext      = '.json'      # the extension.
      @name     = "#{@basename}#{ext}" # basically @basename + @ext.

      # Initialize data hash with the new layout and the origina json data
      @data = {
        'json' => data,
        'layout' => 'cve-json'
      }


      ## Look up front matter defaults 
      data.default_proc = proc do |_, key|
        site.frontmatter_defaults #.find(relative_path, :categories, key)
      end
    end

    # Placeholders that are used in constructing page URL.
    def url_placeholders
      {
        :path       => @dir,
        :basename   => basename,
        :output_ext => output_ext,
      }
    end
  end
end