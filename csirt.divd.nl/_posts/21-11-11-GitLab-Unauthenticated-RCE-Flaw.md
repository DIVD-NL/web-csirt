---
layout: post
title: GitLab Unauthenticated RCE Flaw
author: Jeroen van de Weerd
excerpt: "Gitlab released versions 13.10.3, 13.9.6, and 13.8.8 for GitLab Community Edition (CE) and Enterprise Edition (EE)."
#jekyll-secinfo:
#  cve:
#    url: /cves/CVE-
---
Today we opened case {% divd DIVD-2021-00030 %} to address a vulnerability known as CVE-2021-22205 in GitLab Community Edition (CE) and Enterprise Edition (EE) affecting all versions starting from 11.9.
GitLab was not properly validating image files that is passed to a file parser, this resulted in a remote command execution (RCE).

We have received a list of GitLab servers running a vulnerable version of GitLab from security researchers at Censys.io who previously wrote a blog post about this (https://censys.io/blog/cve-2021-22205-it-was-a-gitlab-smash/). We have validated these findings by manually verifying a representative sample, and are now sending out notifications.
