#!/usr/bin/env python3

import json
import requests
import argparse

# Main

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Update team members and teams from theorg.com', allow_abbrev=False)
	parser.add_argument('--member-path', type=str, metavar="<path to create team member md files>", default="", required=True, help="path of directory to create member md files")
	parser.add_argument('--team-path', type=str, metavar="<path to create team md files>", default="", required=True, help="path of directory to create member md files")


	args = parser.parse_args()

	url = 'https://prod-graphql-api.theorg.com/graphql'
	#payload = {'some': 'data'}
	payload = {
		"operationName": "teamsByCompany",
		"variables": {
			"companySlug": "dutch-institute-for-vulnerability-disclosure",
			"membersLimit": 20,
			"offset": 0,
			"limit": 100
		},
		"query": 'query teamsByCompany($companySlug: String!, $limit: Int!, $offset: Int!, $membersLimit: Int!) {\n  teamsByCompany(companySlug: $companySlug, limit: $limit, offset: $offset) {\n    ...LightTeam\n    __typename\n  }\n}\n\nfragment LightTeam on Team {\n  id\n  slug\n  name\n  memberCount\n  members(limit: $membersLimit) {\n    ...LightPositionFragment\n    __typename\n  }\n  __typename\n}\n\nfragment LightPositionFragment on LightPosition {\n  id\n  slug\n  fullName\n  profileImage {\n    ...ImageFragment\n    __typename\n  }\n  role\n  parentPositionId\n  isAdviser\n  lastUpdate\n  __typename\n}\n\nfragment ImageFragment on Image {\n  endpoint\n  ext\n  placeholderDataUrl\n  prevailingColor\n  uri\n  versions\n  __typename\n}\n'
		}
	headers = {'content-type': 'application/json'}

	r = requests.post(url, data=json.dumps(payload), headers=headers)
	#r = requests.post(url, data=payload, headers=headers)
	
	print("updating teams",end="")
	for team in r.json()["data"]["teamsByCompany"] :
		#print(json.dumps(team))
		with open("{}/{}.md".format(args.team_path,team["slug"]), "w") as tfh :
			tfh.write("---\n")
			tfh.write("layout: team\n")
			tfh.write("slug: {}\n".format(team["slug"]))
			tfh.write("name: {}\n".format(team["name"]))
			tfh.write("title: {}\n".format(team["name"]))
			tfh.write("size: {}\n".format(team["memberCount"]))
			tfh.write("members:\n")
			for member in team["members"] :
				tfh.write("  - {}\n".format(member["id"]))
			tfh.write("---\n")
		print(".",end="")
	print("done")

	payload = {
    	"operationName": "Company",
    	"variables": {
        	"slug": "dutch-institute-for-vulnerability-disclosure"
    	},
    	"query": "query Company($slug: String!) {\n  company(slug: $slug) {\n    ...FullCompany\n    __typename\n  }\n}\n\nfragment FullCompany on Company {\n  id\n  name\n  slug\n  extensions\n  logoImage {\n    ...ImageFragment\n    __typename\n  }\n  social {\n    ...CompanySocialFragment\n    __typename\n  }\n  location {\n    ...CompanyLocation\n    __typename\n  }\n  description\n  type\n  industry\n  status\n  private\n  teams {\n    id\n    __typename\n  }\n  meta {\n    ...MetaFragment\n    __typename\n  }\n  nodes {\n    ...PositionNode\n    __typename\n  }\n  stats {\n    ...CompanyStats\n    __typename\n  }\n  verification {\n    verificationType\n    __typename\n  }\n  adminLocked\n  stage\n  companyValues {\n    ...CompanyValue\n    __typename\n  }\n  imageGallery {\n    ...ImageFragment\n    __typename\n  }\n  testimonials {\n    ...CompanyTestimonialConnection\n    __typename\n  }\n  industries {\n    ...CompanyIndustryFragment\n    __typename\n  }\n  lastUpdate\n  permissionSettings {\n    companyId\n    restrictMembersFromEditing\n    __typename\n  }\n  __typename\n}\n\nfragment ImageFragment on Image {\n  endpoint\n  ext\n  placeholderDataUrl\n  prevailingColor\n  uri\n  versions\n  __typename\n}\n\nfragment CompanySocialFragment on CompanySocial {\n  twitterUrl\n  linkedInUrl\n  facebookUrl\n  websiteUrl\n  __typename\n}\n\nfragment CompanyLocation on CompanyLocation {\n  id\n  street\n  postalCode\n  city\n  subLocality\n  country\n  countryIso\n  state\n  locationString\n  isPrimary\n  __typename\n}\n\nfragment MetaFragment on CompanyMeta {\n  noIndex\n  importanceScore\n  tags\n  __typename\n}\n\nfragment PositionNode on OrgChartStructureNode {\n  id\n  title\n  leafMember {\n    ...FlatPositionFragment\n    __typename\n  }\n  containingNodeId\n  node {\n    ... on Vacant {\n      job {\n        id\n        slug\n        title\n        location {\n          city\n          state\n          country\n          __typename\n        }\n        atsProvider {\n          provider\n          __typename\n        }\n        createdOn\n        jobFunction\n        remote\n        manager {\n          ... on ChartNodeGroup {\n            positions {\n              ... on PositionOrgChartPosition {\n                positionId\n                fullName\n                profileImage {\n                  ...ImageFragment\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          ... on ChartNodeSingular {\n            positionId\n            position {\n              ... on PositionOrgChartPosition {\n                profileImage {\n                  ...ImageFragment\n                  __typename\n                }\n                fullName\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  order\n  parentId\n  section\n  type\n  __typename\n}\n\nfragment FlatPositionFragment on FlatPosition {\n  id\n  slug\n  fullName\n  role\n  roleFunction\n  roleAutoFunction\n  description\n  parentPositionId\n  profileImage {\n    ...ImageFragment\n    __typename\n  }\n  social {\n    ...UserSocialFragment\n    __typename\n  }\n  isAdviser\n  group {\n    ...PositionGroupFragment\n    __typename\n  }\n  companyStartDate {\n    day\n    month\n    year\n    __typename\n  }\n  roleStartDate {\n    day\n    month\n    year\n    __typename\n  }\n  location {\n    ...CompanyLocation\n    __typename\n  }\n  invitedAt\n  remote\n  lastUpdate\n  pronoun\n  invitedAt\n  claimedBy\n  __typename\n}\n\nfragment UserSocialFragment on UserSocial {\n  twitterUrl\n  linkedInUrl\n  facebookUrl\n  websiteUrl\n  __typename\n}\n\nfragment PositionGroupFragment on PositionGroup {\n  id\n  name\n  __typename\n}\n\nfragment CompanyStats on CompanyStats {\n  tags\n  employeeRange\n  followerCount\n  positionCount\n  jobsCount\n  teamsCount\n  announcementsCount\n  following\n  promptDismissals\n  latestFundingRound {\n    id\n    fundingType\n    __typename\n  }\n  __typename\n}\n\nfragment CompanyValue on CompanyValue {\n  id\n  value\n  description\n  __typename\n}\n\nfragment CompanyTestimonialConnection on CompanyTestimonialConnection {\n  testimonial {\n    id\n    question\n    answer\n    __typename\n  }\n  position {\n    id\n    slug\n    fullName\n    profileImage {\n      ...ImageFragment\n      __typename\n    }\n    role\n    parentPositionId\n    isAdviser\n    lastUpdate\n    __typename\n  }\n  __typename\n}\n\nfragment CompanyIndustryFragment on CompanyTag {\n  id\n  title\n  __typename\n}\n"
		}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	
	print("Updating people",end="")
	for node in r.json()["data"]["company"]["nodes"] :
		if node["leafMember"]["slug"] :
			with open("{}/{}.md".format(args.member_path, node["leafMember"]["fullName"]), "w") as mfh :
				mfh.write("---\n")
				mfh.write("layout: person\n")
				mfh.write("person_id: {}\n".format(node["leafMember"]["id"] or ""))
				mfh.write("name: \"{}\"\n".format(node["leafMember"]["fullName"] or ""))
				mfh.write("role: \"{}\"\n".format(node["leafMember"]["role"] or "")) 
				mfh.write("manager: {}\n".format(node["leafMember"]["parentPositionId"] or ""))
				mfh.write("socials :\n")
				for social in node["leafMember"]["social"] :
					if not social.startswith("__"):
						mfh.write("  {}: {}\n".format(social, node["leafMember"]["social"][social] or ""))
				if "companyStartDate" in node["leafMember"] and node["leafMember"]["companyStartDate"] :
					mfh.write("start: {:04d}-{:02d}-{:02d}\n".format(
						node["leafMember"]["companyStartDate"]["year"],
						node["leafMember"]["companyStartDate"]["month"],
						node["leafMember"]["companyStartDate"]["day"])
					)
				mfh.write("---\n")
				mfh.write("{}\n".format(node["leafMember"]["description"] or ""))
		print(".",end="")
	print("done")
