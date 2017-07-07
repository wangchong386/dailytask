## 1. git push
```
$ git push
fatal: You didn't specify any refspecs to push, and push.default is "nothing".
```
解决办法：[命令](https://stackoverflow.com/questions/1475468/git-push-failed-you-did-not-specify-any-refspecs-to-push)

If you want Git to push the current branch when [branchname] is not specified without warning, do this:
```
git config push.default current
```