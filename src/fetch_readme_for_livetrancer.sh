source .env

curl -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3.raw" \
     "https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO/readme" -o fetched_data/fetched_README.md

echo "fetched_README.md has been saved."


curl -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3.raw" \
     "https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO/contents/README_ja.md" -o fetched_data/fetched_README_ja.md

echo "fetched_README_ja.md has been saved."


curl -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3.raw" \
     "https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO/contents/README_tree.md" -o fetched_data/fetched_README_tree.md

echo "fetched_README_tree.md has been saved."


curl -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     "https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO/issues?state=all" -o fetched_data/fetched_issues.json

echo "fetched_issues.json has been saved."


curl -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     "https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO/commits" -o fetched_data/fetched_commits.json

echo "fetched_commits.json has been saved."
