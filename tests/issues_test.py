#!/bin/env python3

import unittest

from issues import GithubIssues

class IssuesTest(unittest.TestCase):

  def testValidateParamsOk(self):
    params = ['https://github.com/algorand/pyteal']
    gh = GithubIssues()
    self.assertTrue(gh.validateParams(params))
    
  def testValidateParamsMissing(self):
    params = []
    with self.assertRaises(SystemExit):
      gh = GithubIssues()
      gh.validateParams(params)

  def testParseRepoSimple(self):
    repo = "algorand/pyteal"
    gh = GithubIssues()
    self.assertEqual(gh.parseRepo(repo), 'algorand/pyteal')
    
  def testParseRepoFromUrl(self):
    repo = "https://github.com/algorand/pyteal"
    gh = GithubIssues()
    self.assertEqual(gh.parseRepo(repo), 'algorand/pyteal')

  def testFetchGithubAPI(self):
    self.assertTrue(True)

  def testFetchIssues(self):
    self.assertTrue(True)

  def testFilteredFields(self):
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()