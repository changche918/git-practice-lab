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
    選項  /  意思
    Accept Current Change保留「# test 10 我要測試 revert 指令」
    Accept Incoming Change恢復成「# test 10」（revert 的目的）
    Accept Both Changes兩個都留Compare Changes看差異再決定
    git add .
    git commit -m "revert 完成"
    '''
"""
