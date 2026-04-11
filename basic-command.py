# 20260405
"""
- git restore #  處理還沒 commit 的東西
    '''
    先下，從暫存區退出來 : git restore --staged index.html
    # 改壞了一個檔案，想恢復原狀
    git restore index.html

    # 改壞了全部檔案
    git restore .
    '''
- git merge
    '''
    merge 是本地操作 (commit後執行)
    # 你在 feature 分支寫完功能，想合進 main
    git checkout main  # 先切到 main
    git merge feature  # 把 feature 的內容合進來
    '''
- git reset : 回到某個版本 
    '''
    1. git add 之後，想退回來。2. commit 之後，想反悔。3. git push 後也可但不建議
        d91fec4 → HEAD（現在）
        30508dd → HEAD~1（上一個）
        a4c0161 → HEAD~2（上兩個）
    # 查看 commit 紀錄，找到想回去的版本
    git log --oneline

    # 回到那個版本，但保留修改在工作區
    git reset abc1234

    # 回到那個版本，什麼都不留（危險！）
    git reset --hard abc1234
    '''
- git revert <commit_id> : 清掉上一個 commit 點
    '''
    git revert abc1234

    '''
"""
