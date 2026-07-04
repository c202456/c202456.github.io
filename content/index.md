cd ~/Documents/quartz

cat > content/index.md <<'EOF'
---
title: 我的知識庫
---

<div class="kb-hero">

# 我的知識庫

<div class="kb-subtitle">
整理工作、生活、閱讀與學習內容的個人知識庫
</div>

</div>

## 🧭 內容分類

<div class="kb-grid">

<a class="kb-card" href="/我的知識庫/🏯佛堂/">
  <div class="kb-card-icon">🏯</div>
  <div class="kb-card-body">
    <div class="kb-card-title">佛堂</div>
    <div class="kb-card-desc">佛堂資料、先生與眾共勉事項及學習紀錄</div>
  </div>
  <div class="kb-card-arrow">→</div>
</a>

<a class="kb-card" href="/我的知識庫/🌍 eSIM/">
  <div class="kb-card-icon">🌍</div>
  <div class="kb-card-body">
    <div class="kb-card-title">eSIM</div>
    <div class="kb-card-desc">各國方案、產品資料與使用紀錄</div>
  </div>
  <div class="kb-card-arrow">→</div>
</a>

<a class="kb-card" href="/我的知識庫/👨‍👩‍👧‍👦 家庭/">
  <div class="kb-card-icon">👨‍👩‍👧‍👦</div>
  <div class="kb-card-body">
    <div class="kb-card-title">家庭</div>
    <div class="kb-card-desc">親子生活、家庭活動與日常紀錄</div>
  </div>
  <div class="kb-card-arrow">→</div>
</a>

<a class="kb-card" href="/我的知識庫/💼 工作/">
  <div class="kb-card-icon">💼</div>
  <div class="kb-card-body">
    <div class="kb-card-title">工作</div>
    <div class="kb-card-desc">工作流程、專案、商務與營運資料</div>
  </div>
  <div class="kb-card-arrow">→</div>
</a>

<a class="kb-card" href="/我的知識庫/📚 書籍/">
  <div class="kb-card-icon">📚</div>
  <div class="kb-card-body">
    <div class="kb-card-title">書籍</div>
    <div class="kb-card-desc">閱讀筆記、書籍整理與個人心得</div>
  </div>
  <div class="kb-card-arrow">→</div>
</a>

<a class="kb-card" href="/我的知識庫/📝 筆記/">
  <div class="kb-card-icon">📝</div>
  <div class="kb-card-body">
    <div class="kb-card-title">筆記</div>
    <div class="kb-card-desc">想法、研究、教學與其他整理內容</div>
  </div>
  <div class="kb-card-arrow">→</div>
</a>

</div>
EOF

~/Desktop/發布知識庫.command