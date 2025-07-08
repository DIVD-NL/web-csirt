#!/usr/bin/env python3

import requests
import argparse
import re
from bs4 import BeautifulSoup
import os
import unicodedata
import glob
import urllib.parse

def slugify(value):
    """
    Convert a string to a slug (URL-friendly format).
    """
    # Convert to lowercase and normalize unicode
    value = unicodedata.normalize('NFKD', value.lower())
    # Remove non-alphanumeric characters except spaces and hyphens
    value = re.sub(r'[^a-z0-9\s\-]', '', value)
    # Replace spaces with hyphens
    value = re.sub(r'\s+', '-', value)
    # Remove multiple consecutive hyphens
    value = re.sub(r'-+', '-', value)
    # Remove leading/trailing hyphens
    value = value.strip('-')
    return value

def extract_person_id_from_url(url):
    """
    Extract person ID from URL like /who-we-are/team/people/name/
    """
    if url and '/people/' in url:
        # Extract the part after /people/
        name_part = url.split('/people/')[-1].rstrip('/')
        # URL decode the name part to handle special characters
        decoded_name = urllib.parse.unquote(name_part)
        return decoded_name
    return None

def get_people_from_cases():
    """
    Extract all people mentioned in case files (author and lead).
    """
    people = set()
    
    # Find all case files
    case_files = glob.glob('_cases/*/*.md')
    
    for case_file in case_files:
        try:
            with open(case_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract author and lead from frontmatter
            lines = content.split('\n')
            in_frontmatter = False
            frontmatter_end_count = 0
            
            for line in lines:
                if line.startswith('---'):
                    frontmatter_end_count += 1
                    if frontmatter_end_count == 1:
                        in_frontmatter = True
                    elif frontmatter_end_count == 2:
                        # End of frontmatter
                        break
                elif in_frontmatter:
                    if line.startswith('author:'):
                        author = line.replace('author:', '').strip()
                        if author:
                            people.add(author)
                    elif line.startswith('lead:'):
                        lead = line.replace('lead:', '').strip()
                        if lead:
                            people.add(lead)
        except Exception as e:
            print(f"Warning: Could not read {case_file}: {e}")
    
    return sorted(people)

def scrape_divd_team():
    """
    Scrape team information from DIVD website.
    """
    url = 'https://www.divd.nl/who-we-are/team/'
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching team page: {e}")
        return None, None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    teams = []
    members = {}
    
    # Find all accordion items (teams)
    accordion_items = soup.find_all('div', class_='accordion-item')
    
    for item in accordion_items:
        # Get team name from h3 tag
        team_name_elem = item.find('h3')
        if not team_name_elem:
            continue
            
        team_name = team_name_elem.get_text(strip=True)
        team_slug = slugify(team_name)
        
        # Find all team members in this accordion item
        team_members = []
        person_cards = item.find_all('a', class_='card-link')
        
        for card in person_cards:
            # Extract person URL and info
            person_url = card.get('href', '')
            person_id = extract_person_id_from_url(person_url)
            
            if not person_id:
                continue
                
            # Extract name from h3 inside the card
            name_elem = card.find('h3')
            if not name_elem:
                continue
                
            name = name_elem.get_text(strip=True)
            
            # Extract role from h6 inside the card
            role_elem = card.find('h6')
            role = role_elem.get_text(strip=True) if role_elem else ""
            
            # Store member info
            if person_id not in members:
                members[person_id] = {
                    'id': person_id,
                    'name': name,
                    'role': role,
                    'url': person_url
                }
            
            team_members.append(person_id)
        
        # Store team info
        if team_members:  # Only add teams with members
            teams.append({
                'name': team_name,
                'slug': team_slug,
                'members': team_members
            })
    
    return teams, members

def debug_missing_people(members):
    """
    Debug function to check which people from cases are not found on the website.
    """
    # Get all people from cases
    case_people = get_people_from_cases()
    
    # Get all people from website
    website_people = set(member['name'] for member in members.values())
    
    # Find missing people
    missing_people = []
    for person in case_people:
        if person not in website_people:
            missing_people.append(person)
    
    print(f"Found {len(case_people)} unique people in case files")
    print(f"Found {len(website_people)} people on website")
    
    if missing_people:
        print(f"WARNING: {len(missing_people)} people from cases NOT found on website:")
        for person in sorted(missing_people):
            print(f"  - {person}")
        print("These people will not have clickable links in case files.")
    else:
        print("All people from cases found on website!")
    
    return missing_people

def main():
    parser = argparse.ArgumentParser(description='Sync team members and teams from DIVD website', allow_abbrev=False)
    parser.add_argument('--member-path', type=str, metavar="<path to create team member md files>", default="", required=True, help="path of directory to create member md files")
    parser.add_argument('--team-path', type=str, metavar="<path to create team md files>", default="", required=True, help="path of directory to create team md files")
    parser.add_argument('--debug', action='store_true', help="Show debug information about missing people")
    
    args = parser.parse_args()
    
    # Create directories if they don't exist
    os.makedirs(args.member_path, exist_ok=True)
    os.makedirs(args.team_path, exist_ok=True)
    
    print("Scraping DIVD team information...")
    teams, members = scrape_divd_team()
    
    if teams is None or members is None:
        print("Failed to scrape team information")
        return 1
    
    # Debug missing people if requested
    if args.debug:
        missing_people = debug_missing_people(members)
    
    # Write team files
    print(f"Updating {len(teams)} teams", end="")
    for team in teams:
        team_file = os.path.join(args.team_path, f"{team['slug']}.md")
        with open(team_file, 'w', encoding='utf-8') as tfh:
            tfh.write("---\n")
            tfh.write("layout: team\n")
            tfh.write(f"slug: {team['slug']}\n")
            tfh.write(f"name: {team['name']}\n")
            tfh.write(f"title: {team['name']}\n")
            tfh.write(f"size: {len(team['members'])}\n")
            tfh.write("members:\n")
            for member_id in team['members']:
                tfh.write(f"  - {member_id}\n")
            tfh.write("---\n")
        print(".", end="")
    print("done")
    
    # Write member files
    print(f"Updating {len(members)} people", end="")
    for member_id, member in members.items():
        # Sanitize filename by normalizing Unicode and removing problematic characters
        safe_name = unicodedata.normalize('NFKD', member['name'])
        safe_name = re.sub(r'[^\w\s-]', '', safe_name)
        safe_name = re.sub(r'[-\s]+', ' ', safe_name).strip()
        member_file = os.path.join(args.member_path, f"{safe_name}.md")
        
        # Clean the name and role by removing problematic Unicode characters
        def clean_for_yaml(text):
            # Normalize to decomposed form
            normalized = unicodedata.normalize('NFKD', text)
            # Remove all control characters and combining characters
            cleaned = ''.join(char for char in normalized 
                            if unicodedata.category(char)[0] not in ('C', 'M'))
            # Convert to ASCII where possible, remove non-ASCII otherwise
            ascii_cleaned = cleaned.encode('ascii', 'ignore').decode('ascii')
            return ascii_cleaned.strip()
        
        clean_name = clean_for_yaml(member['name'])
        clean_role = clean_for_yaml(member['role'])
        clean_person_id = clean_for_yaml(member['id'])
        
        with open(member_file, 'w', encoding='utf-8', newline='\n') as mfh:
            mfh.write("---\n")
            mfh.write("layout: person\n")
            mfh.write(f"person_id: {clean_person_id}\n")
            # Properly escape YAML string values by using YAML-safe quoting
            name_escaped = clean_name.replace('"', '\\"')
            role_escaped = clean_role.replace('"', '\\"')
            mfh.write(f"name: \"{name_escaped}\"\n")
            mfh.write(f"role: \"{role_escaped}\"\n")
            mfh.write("manager: \n")  # No manager info available from website
            mfh.write("socials:\n")  # No social info available from website
            mfh.write("---\n")
            # No description available from website
        print(".", end="")
    print("done")
    
    print(f"\nSummary:")
    print(f"- Created {len(teams)} team files")
    print(f"- Created {len(members)} member files")
    
    return 0

if __name__ == '__main__':
    exit(main())
