import git
# clone the repository
repo = git.Repo.clone_from('https:github.com/samwineprisca/repo.git', '/path/to/local/repo')

# list all the branches in the repository
branches = repo.branches
for branch in branches:
    print(branch.name)