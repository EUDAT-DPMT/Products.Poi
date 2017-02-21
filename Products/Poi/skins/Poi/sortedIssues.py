##parameters=issues
issues = list(issues)
issues.sort(lambda x,y: cmp(int(x.getId[:3]), int(y.getId[:3])))
return issues
