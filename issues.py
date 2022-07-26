#!/bin/env python3

from ctypes.wintypes import HHOOK
import http
import json
import jsonpath
import os
import requests
import sys
from typing import List
from dotenv import load_dotenv

class GithubIssues():
  GITHUB_API = 'https://api.github.com/'
  GITHUB_API_ISSUES_PATH = r'repos/{{REPO}}/issues'

  def loadParams(self, params):
    self.validateParams(params)
    self.query_repo = self.parseRepo(params[1])

  def loadCredentials(self):
    self.github_token = os.getenv('GITHUB_TOKEN')
    if self.github_token is None:
      sys.exit('ERROR: GITHUB_TOKEN must be set in a .env file!')

  def validateParams(self, params: List[str]) -> bool:
    """For now, just exit if there's not a lone parameter
       This may provide more detailed validation in the future
    """
    if len(params) != 2:
      print(f"Expected 1 parameter (Github Repository), got {params}.", file=sys.stderr )
      sys.exit(2)
    return True

  def parseRepo(self, repo: str):
    """Reads either a Repo URL or ORG/REPO string"""
    if repo.startswith('http'):
      return '/'.join(repo.split('/')[3:5])
    else:
      return repo

  def fetchAPI(self):
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
    print(self.fetch_result)
    json_unfiltered = json.loads(self.fetch_result)
    json_reduced = jsonpath.jsonpath(json_unfiltered, '$.[*].[title, number]')
     # | {title: .title, number: .number, labels: [.labels[].name]}')
    print(json.dumps(json_reduced, indent=4))
    # print(json.dumps(self.result))

  def printResults(self):
    pass


if __name__ == '__main__':
  load_dotenv()
  gh = GithubIssues()
  gh.loadParams(sys.argv)
  gh.loadCredentials()
  gh.fetchAPI()
  gh.filterResults()
  gh.printResults()