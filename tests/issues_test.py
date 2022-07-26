#!/bin/env python3

import json
import unittest
from dotenv import load_dotenv
from issues import GithubIssues

TEST_API_DATA = """[{
    "title": "foo",
    "number": 111,
    "labels": [
      {
        "id": 12345,
        "name": "foo-label1"
      },
      {
        "id": 12346,
        "name": "foo-label2"
      }
    ]
  },
  {
    "title": "bar",
    "number": 2222,
    "labels": [
      {
        "id": 12345,
        "name": "bar-label1"
      },
      {
        "id": 32122,
        "name": "bar-label2"
      }
    ]
  },
  {
    "title": "a pull request",
    "number": 333,
    "pull_request": {},
    "labels": [
      {
        "id": 12347,
        "name": "pr-label1"
      },
      {
        "id": 12348,
        "name": "pr-label2"
      }
    ]
  }]
"""

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
    # Issues + Pull Requests
    self.assertEqual(len(self.gh.json_unfiltered), 29)
    # Only Issues
    self.assertEqual(len(self.gh.json_reduced), 17)

  def testFilteredResults(self):
    self.gh.fetch_result = TEST_API_DATA
    self.gh.filterResults()
    self.assertEqual(
      [item['title'] for item in self.gh.json_reduced],
      ["foo", "bar"]
    )
    self.assertEqual(
      [item['labels'] for item in self.gh.json_reduced],
      [['foo-label1', 'foo-label2'], ['bar-label1', 'bar-label2']]
    )

if __name__ == '__main__':
  unittest.main()