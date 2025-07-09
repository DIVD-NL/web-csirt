#!/usr/bin/env python3

import requests
import argparse
import os
import unicodedata
import glob
import json
import re

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

def clean_for_yaml(text):
    """
    Clean text for YAML compatibility by removing problematic Unicode characters.
    """
    if not text:
        return ""
    # Normalize to decomposed form
    normalized = unicodedata.normalize('NFKD', text)
    # Remove all control characters and combining characters
    cleaned = ''.join(char for char in normalized 
                    if unicodedata.category(char)[0] not in ('C', 'M'))
    # Convert to ASCII where possible, remove non-ASCII otherwise
    ascii_cleaned = cleaned.encode('ascii', 'ignore').decode('ascii')
    return ascii_cleaned.strip()

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

def fetch_divd_team_json():
    """
    Fetch team information from DIVD JSON API.
    """
    url = 'https://www.divd.nl/documents/people.json'
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching team JSON: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def process_team_data(people_data):
    """
    Process the JSON data into teams and members.
    """
    teams = {}
    members = {}
    
    for person in people_data:
        # Create full name
        first_name = person.get('firstName', '').strip()
        last_name = person.get('lastName', '').strip()
        full_name = f"{first_name} {last_name}".strip()
        
        if not full_name:
            continue
            
        # Create person ID (slug of full name)
        person_id = slugify(full_name)
        
        # Get role and clean it
        role = clean_for_yaml(person.get('role', ''))
        
        # Get about/description
        about = clean_for_yaml(person.get('about', ''))
        
        # Get social links
        social_links = person.get('socialLinks', {})
        
        # Create member entry
        members[person_id] = {
            'id': person_id,
            'name': full_name,
            'role': role,
            'about': about,
            'social_links': social_links,
            'profile_picture': person.get('profilePicture', ''),
            'teams': person.get('teams', [])
        }
        
        # Process teams
        for team_name in person.get('teams', []):
            team_slug = slugify(team_name)
            
            if team_slug not in teams:
                teams[team_slug] = {
                    'name': team_name,
                    'slug': team_slug,
                    'members': []
                }
            
            teams[team_slug]['members'].append(person_id)
    
    return list(teams.values()), members

def debug_missing_people(members):
    """
    Debug function to check which people from cases are not found in the JSON API.
    """
    # Get all people from cases
    case_people = get_people_from_cases()
    
    # Get all people from JSON API
    api_people = set(member['name'] for member in members.values())
    
    # Find missing people
    missing_people = []
    for person in case_people:
        if person not in api_people:
            missing_people.append(person)
    
    print(f"Found {len(case_people)} unique people in case files")
    print(f"Found {len(api_people)} people in JSON API")
    
    if missing_people:
        print(f"WARNING: {len(missing_people)} people from cases NOT found in JSON API:")
        for person in sorted(missing_people):
            print(f"  - {person}")
        print("These people will not have clickable links in case files.")
    else:
        print("All people from cases found in JSON API!")
    
    return missing_people

def main():
    parser = argparse.ArgumentParser(description='Sync team members and teams from DIVD JSON API', allow_abbrev=False)
    parser.add_argument('--member-path', type=str, metavar="<path to create team member md files>", default="", required=True, help="path of directory to create member md files")
    parser.add_argument('--team-path', type=str, metavar="<path to create team md files>", default="", required=True, help="path of directory to create team md files")
    parser.add_argument('--debug', action='store_true', help="Show debug information about missing people")
    
    args = parser.parse_args()
    
    # Create directories if they don't exist
    os.makedirs(args.member_path, exist_ok=True)
    os.makedirs(args.team_path, exist_ok=True)
    
    print("Fetching DIVD team information from JSON API...")
    people_data = fetch_divd_team_json()
    
    if people_data is None:
        print("Failed to fetch team information")
        return 1
    
    print(f"Processing {len(people_data)} people from JSON API...")
    teams, members = process_team_data(people_data)
    
    # Debug missing people if requested
    if args.debug:
        missing_people = debug_missing_people(members)
    
    # Write team files
    print(f"Updating {len(teams)} teams", end="")
    for team in teams:
        team_file = os.path.join(args.team_path, f"{team['slug']}.md")
        with open(team_file, 'w', encoding='utf-8', newline='\n') as tfh:
            tfh.write("---\n")
            tfh.write("layout: team\n")
            tfh.write(f"slug: {team['slug']}\n")
            tfh.write(f"name: {clean_for_yaml(team['name'])}\n")
            tfh.write(f"title: {clean_for_yaml(team['name'])}\n")
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
        
        # Clean all fields for YAML safety
        clean_name = clean_for_yaml(member['name'])
        clean_role = clean_for_yaml(member['role'])
        clean_person_id = clean_for_yaml(member['id'])
        clean_about = clean_for_yaml(member['about'])
        
        with open(member_file, 'w', encoding='utf-8', newline='\n') as mfh:
            mfh.write("---\n")
            mfh.write("layout: person\n")
            mfh.write(f"person_id: {clean_person_id}\n")
            # Properly escape YAML string values
            name_escaped = clean_name.replace('"', '\\"')
            role_escaped = clean_role.replace('"', '\\"')
            mfh.write(f"name: \"{name_escaped}\"\n")
            mfh.write(f"role: \"{role_escaped}\"\n")
            mfh.write("manager: \n")  # Not available in JSON API
            
            # Write social links
            mfh.write("socials:\n")
            for platform, url in member['social_links'].items():
                if url and url.strip():
                    clean_url = clean_for_yaml(url.strip())
                    mfh.write(f"  {platform.lower()}: {clean_url}\n")
            
            mfh.write("---\n")
            
            # Write about section if available
            if clean_about:
                mfh.write(f"{clean_about}\n")
        print(".", end="")
    print("done")
    
    print(f"\nSummary:")
    print(f"- Created {len(teams)} team files")
    print(f"- Created {len(members)} member files")
    
    return 0

if __name__ == '__main__':
    exit(main())
