#!/bin/env python3

import argparse
import json
import pyjq
import os
import requests
import sys
from typing import List
from dotenv import load_dotenv

class GithubIssues():
  GITHUB_API = 'https://api.github.com/'
  GITHUB_API_ISSUES_PATH = r'repos/{{REPO}}/issues'
  JSONPATH_EXP =  '$.[*].[title, number]' # TODO: REMOVE THIS
  JQ_EXP = 'map(select(has("pull_request") | not)) | .[] | {title: .title, number: .number, labels: [.labels[].name]}'

  def loadParams(self):
    parser = argparse.ArgumentParser(exit_on_error=True)
    parser.add_argument('github_repo', type=str, help="GitHub repository in ORG/REPO or full URL format")
    args = parser.parse_args()
    self.setQueryRepo(self.parseRepoName(args.github_repo))

  def setQueryRepo(self, query_repo: str):
    self.query_repo = query_repo

  def loadCredentials(self):
    self.github_token = os.getenv('GITHUB_TOKEN')
    if self.github_token is None:
      sys.exit('ERROR: GITHUB_TOKEN must be set in a .env file!')

  def parseRepoName(self, repo: str):
    """Reads either a Repo URL or ORG/REPO string"""
    if repo.startswith('http'):
      return '/'.join(repo.split('/')[3:5])
    else:
      return repo

  def fetchAPI(self):
    """Requests open issues from GitHub's API for this Repository"""
    headers = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"token {self.github_token}",
      "state": "open" # Open Issues only!
    }
    gh_issues_endpoint = self.GITHUB_API + self.GITHUB_API_ISSUES_PATH.replace(r"{{REPO}}", self.query_repo)
    print(gh_issues_endpoint)
    result = requests.get(gh_issues_endpoint, headers=headers)
    self.fetch_result = result.text

  def filterResults(self):
    """Uses JQ expression to transform the JSON API result to what's relevant"""
    print(self.fetch_result)
    self.json_unfiltered = json.loads(self.fetch_result)
    self.json_reduced = pyjq.all(self.JQ_EXP, self.json_unfiltered)

  def printResults(self):
    """Prints human readable JSON output"""
    print(json.dumps(self.json_reduced, indent=4))


if __name__ == '__main__':
  load_dotenv()
  gh = GithubIssues()
  gh.loadParams()
  gh.loadCredentials()
  gh.fetchAPI()
  gh.filterResults()
  gh.printResults()