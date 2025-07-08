#!/usr/bin/env python3

import requests
import argparse
import re
from bs4 import BeautifulSoup
import os
import unicodedata
import glob

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
        return name_part
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
    print("\n" + "="*60)
    print("DEBUG: Checking for missing people from cases")
    print("="*60)
    
    # Get all people from cases
    case_people = get_people_from_cases()
    print(f"Found {len(case_people)} unique people in case files")
    
    # Get all people from website
    website_people = set(member['name'] for member in members.values())
    print(f"Found {len(website_people)} people on website")
    
    # Find missing people
    missing_people = []
    for person in case_people:
        if person not in website_people:
            missing_people.append(person)
    
    print(f"\n{len(missing_people)} people from cases NOT found on website:")
    print("-" * 50)
    
    if missing_people:
        for person in sorted(missing_people):
            print(f"  ❌ {person}")
    else:
        print("  ✅ All people from cases found on website!")
    
    print(f"\n{len(case_people) - len(missing_people)} people from cases FOUND on website:")
    print("-" * 50)
    
    found_people = [person for person in case_people if person in website_people]
    for person in sorted(found_people):
        print(f"  ✅ {person}")
    
    print("\nWebsite people NOT mentioned in any case:")
    print("-" * 50)
    
    unused_people = []
    for person in website_people:
        if person not in case_people:
            unused_people.append(person)
    
    if unused_people:
        for person in sorted(unused_people):
            print(f"  ℹ️  {person}")
    else:
        print("  All website people are mentioned in cases!")
    
    print("\n" + "="*60)
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
        if missing_people:
            print(f"\n⚠️  WARNING: {len(missing_people)} people from cases not found on website!")
            print("These people will not have clickable links in case files.")
    
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
        member_file = os.path.join(args.member_path, f"{member['name']}.md")
        with open(member_file, 'w', encoding='utf-8') as mfh:
            mfh.write("---\n")
            mfh.write("layout: person\n")
            mfh.write(f"person_id: {member['id']}\n")
            mfh.write(f"name: \"{member['name']}\"\n")
            mfh.write(f"role: \"{member['role']}\"\n")
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
