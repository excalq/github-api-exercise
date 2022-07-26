#!/bin/bash
# Returns a JSON set of open issues and their labels, given an accessible Repo and Personal Access Token

export $(grep -v '^#' .env | xargs)
GITHUB_REPO=$1 # e.g. https://github.com/algorand/go-algorand

curl -s \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "state: open" https://api.github.com/repos/$(cut -d'/' -f 4,5 <<<$GITHUB_REPO)/issues \
  | jq '.[] | {title: .title, number: .number, labels: [.labels[].name]}'
