def simplifyPath(path: str) -> str:
    pathes = []
    splitted = path.split('/')
    
    for i, x in enumerate(splitted):
        if not x or x == '.':
            continue

        if x == '..':
            if len(pathes) > 0:
                pathes.pop()
        else:
            pathes.append(x)

    return '/' + '/'.join(str(e) for e in pathes)

print(simplifyPath("/../"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/"))
print(simplifyPath("/home/foo/.."))
print(simplifyPath("/a/./b/../../c/"))