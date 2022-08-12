module CasesPlugin
  @@log = Logger.new(STDERR)  # Could send output to STDOUT
  @@log.level = Logger::WARN
  @@log.progname = 'CasesPlugin'
  @@log.formatter = proc { |severity, datetime, progname, msg|
    "#{severity} #{progname}: #{msg}\n"
  }

  def self.log
    @@log
  end

  class CasesUpdaterGenerator < Jekyll::Generator
    safe true



    def generate(site)
      # Get all the documents in collection cves
      site.collections.each do |n, collection|
        if n == "cases" then
          collection.docs.each do | doc |

            # Case number
            divd = doc.basename_without_ext
            CasesPlugin.log.debug "Case: #{divd}"

            if doc.data.key?("divd") then
              if doc.data["divd"] != divd then
                CasesPlugin.log.error "Case: #{divd} - Has case number #{doc.data["divd"]} set in front matter."
              end
            else
              doc.data["divd"] = divd
            end

            # Lint the title
            if doc.data.key?("title") then
              title = doc.data["title"]
            else
              title = ""
            end
            CasesPlugin.log.debug doc.data["title"]
            if title.length > 80 then
              CasesPlugin.log.error "Case #{divd}, has an overly long title: #{title}"
            end
            if title.match?(/^Divd \d+ \d+/) then
              CasesPlugin.log.error "Case #{divd} - Does not have a title"
            elsif not title.start_with?("#{divd} - ") then
              CasesPlugin.log.info "Setting title to include '#{divd} - '"
              CasesPlugin.log.debug "Old title: #{doc.data["title"]}"
              doc.data["title"] = "#{divd} - #{title}"
              CasesPlugin.log.debug "New title: #{doc.data["title"]}"
            end

            # Permalink
            doc.data["permalink"] = "/cases/#{divd}"

            # Redirection
            if doc.data.key?("redirect_from") then
              if doc.data["redirect_from"][0] != "/#{divd}/" then
                CasesPlugin.log.error "Case #{divd} is set to manually redirect from #{doc.data['redirect_from']}, wich is not /#{divd}/"
              end
            else
              doc.data["redirect_from"] = [ "/#{divd}/" ]
            end

            if not ( doc.data.key?("author") and doc.data["author"] ) then
              CasesPlugin.log.error "Case #{divd}, does not have a author set"
            end
            if not ( doc.data.key?("lead") and doc.data["lead"] ) then
              CasesPlugin.log.error "Case #{divd}, does not have a lead set"
            end

            if doc.data.key?("cves") then
              if doc.data["cves"].kind_of?(Array) then
                doc.data["cves"].each do | cve |
                  if cve then
                    if not cve.match?(/^(CVE\-\d+\-\d+|n\/a|Multiple)$/) then
                      CasesPlugin.log.warn "Case #{divd}, CVE `#{cve}` is not well formed"
                    end
                  end
                end
              else
                if not doc.data["cves"].match?(/^(CVE\-\d+\-\d+|n\/a|Multiple)$/) then
                  CasesPlugin.log.warn "Case #{divd}, CVE `#{doc.data['cves']}` is not well formed"
                end                
              end
            end  

            # Excerpt
            excerpt = doc.data["excerpt"]
            if (not excerpt) or excerpt.start_with?("<h2") or excerpt.start_with?("Please set this to") then
              CasesPlugin.log.error "Case #{divd} does not have an excerpt or the default excerpt"
            end

            # Timeline status etc
            status = doc.data["status"]
            case_start = doc.data["start"]
            case_end   = doc.data["end"] 

            if not ( status and status.match?(/^(Open|Closed)$/)) then
              CasesPlugin.log.error "Case #{divd}, has invalid status '#{status}, should be 'Open' or 'Closed'"
            end

            # Timeline
            if doc.data.key?("timeline") then
              doc.data["timeline"].each do | event |
                valid = true
                if event["end"].kind_of?(String) and event["end"] != "open" then
                  valid = false
                  CasesPlugin.log.error "Case #{divd}, has an event on the timeline with invalid end `#{event["end"]}`"
                end
                if not event["start"].kind_of?(Date) then
                  valid = false
                  CasesPlugin.log.error "Case #{divd}, has an event on the timeline with invalid start `#{event["start"]}`"
                end
                if valid then
                  if event["end"] == "open" and status == "Closed" then
                    CasesPlugin.log.error "Case #{divd} is closed, but there are open items on the timeline"
                  end
                  if event["end"] and event["end"] != "open" then
                    if event["end"] < event["start"] then
                      CasesPlugin.log.error "Case #{divd}, has an event on the timeline that ends before it starts #{event["start"]} -> #{event["end"]} : #{event["event"]}"
                    end
                  end
                end
              end
            end 

            # Closed case tests
            if status == "Closed" then
              if not case_end then
                CasesPlugin.log.error "Case #{divd}, is 'Closed' but end date is not set"
              elsif case_end < case_start then
                CasesPlugin.log.error "Case #{divd}, ends before it starts, #{case_start} -> #{case_end}"
              end
              
              if not ( doc.data.key?("ips") && ( doc.data["ips"] == "n/a" || doc.data["ips"] > 0 ) ) then
                CasesPlugin.log.warn "Case #{divd}, is 'Closed' but 0 ips affected. That's not good for stats (is the ips front matter key set?)"
              end
            end

            # Open case checks
            if status == "Open" then
              if case_end then
                CasesPlugin.log.error "Case #{divd}, is 'Open' but end date is set"
              end
            end



          end
        end
      end
    end
  end

###  # Subclass of `Jekyll::Page` with custom method definitions.
###  class CveJson40Page < Jekyll::Page
###    def initialize(site, data)
###      # Generate a new document with layout cve-json-40-json in /cves based on the original one.
###      CveJson.log.info "Creating a JSON file for #{ data["CVE_data_meta"]["ID"]}"
###      @site = site             # the current site instance.
###      @base = site.source      # path to the source directory.
###      @dir  = "cves"           # the directory the page will reside in.
###      
###      # All pages have the same filename, so define attributes straight away.
###      @basename = data["CVE_data_meta"]["ID"]      # filename without the extension.
###      @ext      = '.json'      # the extension.
###      @name     = "#{@basename}#{ext}" # basically @basename + @ext.
###
###      # Initialize data hash with the new layout and the origina json data
###      @data = {
###        'json' => data,
###        'layout' => 'cve-json-40-json'
###      }
###
###
###      ## Look up front matter defaults 
###      data.default_proc = proc do |_, key|
###        site.frontmatter_defaults #.find(relative_path, :categories, key)
###      end
###    end
###
###    # Placeholders that are used in constructing page URL.
###    def url_placeholders
###      {
###        :path       => @dir,
###        :basename   => basename,
###        :output_ext => output_ext,
###      }
###    end
###  end
end