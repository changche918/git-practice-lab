# 20260405
"""
- git restore #  處理還沒 commit 的東西
    '''
    # 改壞了一個檔案，想恢復原狀
    git restore index.html

    # 改壞了全部檔案
    git restore .
    '''
- git merge
    '''
    # 你在 feature 分支寫完功能，想合進 main
    git checkout main  # 先切到 main
    git merge feature  # 把 feature 的內容合進來
    '''
- git reset : 回到某個版本 
    '''
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
