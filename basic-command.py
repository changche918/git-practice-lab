# 20260405
'''
- git restore file.txt (還原最後一次 file.txt 檔案的 commit)
    - 如果你修改了一個檔案，但還沒執行 git add，現在後悔了想變回修改前的樣子：
    - 語法： git restore <檔案名稱>
    - 效果： 丟棄目前的修改，檔案內容會變回上一次 Commit 或暫存時的狀態。

    - 如果你已經執行了 git add 把檔案送進暫存區（Staging Area），但突然發現還有東西沒改好，想把它從暫存區拿出來：
    - 語法： git restore --staged <檔案名稱>
    - 效果： 檔案會從暫存區退回到工作區，但修改的內容會保留。
    - 常用場景： 不小心 git add . 加到不想提交的檔案，想把它踢出這次的 Commit 清單。
- git merge : 把分支合併 git checkout main、git merge feature
- git rebase : 把你的 commit「接到別的分支後面」，git checkout feature、git rebase main
- git reset : 回到某個版本 
- git revert <commit_id> : 清掉上一個 commit 點
'''

# 1
print("1. PRINT 輸出")

# 2
print("1. PRINT 輸出")

# 3
print("1. PRINT 輸出")

# 4
print("1. PRINT 輸出")
