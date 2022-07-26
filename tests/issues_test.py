#!/bin/env python3

import json
import unittest
from dotenv import load_dotenv

from issues import GithubIssues

class IssuesTest(unittest.TestCase):

  def setUp(self) -> None:
    # Requires .env with a Personal Access Token
    load_dotenv()
    self.gh = GithubIssues()
    self.gh.loadCredentials()

  def testParseRepoSimple(self):
    repo = "algorand/pyteal"
    self.assertEqual(self.gh.parseRepoName(repo), 'algorand/pyteal')
    
  def testParseRepoFromUrl(self):
    repo = "https://github.com/algorand/pyteal"
    self.assertEqual(self.gh.parseRepoName(repo), 'algorand/pyteal')

  def testFetchGithubAPI(self):
    # An archived project with open issues... but no labels :(
    self.gh.setQueryRepo('github/brubeck')
    self.gh.fetchAPI()
    self.gh.filterResults()
    self.gh.printResults()
    # Issues + Pull Requests
    self.assertEqual(len(self.gh.json_unfiltered), 29)
    # Only Issues
    self.assertEqual(len(self.gh.json_reduced), 17)

  def testFetchIssues(self):
    self.assertTrue(True)

  def testFilteredFields(self):
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()