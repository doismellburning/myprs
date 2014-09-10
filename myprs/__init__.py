import datetime
import github3
import os

def myprs(organisation):
    g = github3.login(token=os.environ['GITHUB_AUTH_TOKEN'])
    org = g.organization(organisation)
    prs = []
    for repo in org.iter_repos():
        for pr in repo.iter_pulls(state="open"):
            prs += [pr]

    yours = 0
    count = {}
    lines = []
    for pr in prs:
        r = pr.repository
        line = "%s/%s: #%d: %s @ %s (%s)" % (r[0], r[1], pr.number, pr.title, pr.html_url, pr.user)
        count[pr.user] = count.get(pr.user, 0) + 1
        if pr.user == g.user():
            line += " (YOURS!)"
            yours += 1
        lines.append(line)

    lines.sort()
    print "\n".join(lines)
    print ""
    print "%d open PRs" % len(prs)
    print "%d are yours" % yours
    print ""
    for (u, c) in sorted(count.iteritems()):
        print "%s: %d" % (u, c)
    print ""
    print datetime.datetime.now().isoformat()

def main():
    import sys
    myprs(sys.argv[1])

if __name__ == "__main__":
    main()
