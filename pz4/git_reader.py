import git
res = []


with open('pz4\input.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        repo = git.Repo.clone_from(line.strip(), '/dpp_course')
        if repo:
            res.append((repo, 'OK'))
        else:
            res.append((repo, 'FAIL'))


