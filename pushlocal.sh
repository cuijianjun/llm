#!/bin/bash
direction_branch="" 
direction_branch=`git rev-parse --abbrev-ref HEAD` #获取分支名
git add .
git commit -m "$1"
default="master"
branch=${direction_branch-$default}
git pull origin $branch
git push origin $branch
