import streamlit as st

# ページ設定
st.set_page_config(page_title="プロンプトジェネレーター", layout="wide")

st.title("🌐 汎用Webサイト プロンプトジェネレーター")
st.markdown("作りたいサイトの種類を選ぶと、入力フォームが最適化されます。")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 1. サイト情報の入力")
    
    # 1. サイトの種類を選択
    site_type = st.selectbox("サイトの種類", [
        "商品・サービス向け ランディングページ（LP）",
        "イベント・セミナー向け 特設サイト",
        "コーポレートサイト / ブランドサイト",
        "採用向け リクルートサイト",
        "その他"
    ])
    
    # トンマナ設定（全タイプ共通）
    st.markdown("---")
    st.markdown("🎨 **デザイン設定**")
    base_tone = st.selectbox("トンマナ（ベースの雰囲気）", [
        "シックでクリエイティブ（黒・ダークトーン）",
        "クリーンで先進的（白背景・ブルー系・IT系）",
        "温かみとナチュラル（アースカラー・オーガニック系）",
        "ポップでエネルギッシュ（ビビッドカラー・若者向け）",
        "その他（自由入力）"
    ])
    custom_tone = ""
    if base_tone == "その他（自由入力）":
        custom_tone = st.text_input("独自のトンマナを入力", "例：余白を広めにとった高級感のある雑誌スタイル")
    final_tone = custom_tone if base_tone == "その他（自由入力）" else base_tone

    st.markdown("---")
    st.markdown("📄 **コンテンツ情報**")

    # ==========================================
    # ▼ ここから選択した「サイトの種類」でフォームが分岐 ▼
    # ==========================================
    
    prompt_template = "" # プロンプトの初期化

    # ------------------------------------------
    # パターンA: 商品・サービス向け LP
    # ------------------------------------------
    if site_type == "商品・サービス向け ランディングページ（LP）":
        product_name = st.text_input("商品・サービス名", "スーパーフード BarleyMax")
        target = st.text_area("ターゲット層", "健康志向の20〜40代女性")
        usp = st.text_area("最大のウリ・特徴 (USP)", "食物繊維の代表格を、量で超える。")
        structure = st.text_area("構成案", 
            "1. ヒーローセクション\n"
            "2. 商品の特徴3つ\n"
            "3. 日常への取り入れ方（利用シーン）\n"
            "4. FAQ\n"
            "5. 購入ボタン"
        )
        images = st.text_area("画像アセットの指定", "hero_bg.jpg, product_main.png")
        extra_notes = st.text_area("特記事項", "女性らしく洗練されたアニメーションを入れること")

        prompt_template = f"""あなたは優秀なWebデザイナー兼フロントエンドエンジニアです。
以下の要件に基づき、「{product_name}」の魅力が伝わる商品LPのHTMLファイルを1つ作成してください。

【デザイン・トンマナ】
・方向性: {final_tone}
・Tailwind CSS（CDN）を使用すること
・`onerror` 属性は絶対に使用しないこと

【基本情報】
・商品名: {product_name}
・ターゲット: {target}
・最大のウリ: {usp}

【構成案】
{structure}

【画像アセット】
{images}

【特記事項】
{extra_notes}

出力はHTML、CSS(Tailwind)、JSをすべて1ファイルにまとめ、コードブロックで出力してください。"""

    # ------------------------------------------
    # パターンB: イベント・セミナー向け
    # ------------------------------------------
    elif site_type == "イベント・セミナー向け 特設サイト":
        event_title = st.text_input("イベントタイトル", "KURUME SPACE INNOVATION 2026")
        event_date = st.text_input("日時", "2026.06.01 MON 15:00 - 18:10")
        event_venue = st.text_input("会場・アクセス", "久留米商工会議所 5階 大ホール")
        target = st.text_area("対象者", "宇宙産業に挑戦したい企業・自治体・学生")
        organizers = st.text_input("主催 / 共催", "主催 : 久留米市、QSS、クロスユー")
        agenda = st.text_area("アジェンダと登壇者", "15:00 開会挨拶\n15:10 インプットセッション\n...")
        images = st.text_area("画像アセットの指定", "hero_bg.jpg, speaker_01.jpg")
        extra_notes = st.text_area("特記事項", "フルスクリーン・ワンカラムレイアウトにすること")

        prompt_template = f"""あなたは優秀なWebデザイナー兼フロントエンドエンジニアです。
以下のイベント要件に基づき、参加したくなる特設サイトのHTMLファイルを1つ作成してください。

【デザイン・トンマナ】
・方向性: {final_tone}
・Tailwind CSS（CDN）を使用すること
・`onerror` 属性は絶対に使用しないこと

【イベント基本情報】
・タイトル: {event_title}
・日時: {event_date}
・会場: {event_venue}
・対象者: {target}
・主催: {organizers}

【アジェンダ・登壇者】
{agenda}

【画像アセット】
{images}

【特記事項】
{extra_notes}

出力はHTML、CSS(Tailwind)、JSをすべて1ファイルにまとめ、コードブロックで出力してください。"""

    # ------------------------------------------
    # パターンC: コーポレート・ブランドサイト / リクルート / その他
    # ------------------------------------------
    else:
        site_purpose = st.text_area("目的とターゲット層", "例：企業の信頼感を高め、新規問い合わせを獲得する")
        structure = st.text_area("構成案", "1. トップビジュアル\n2. 企業理念\n3. 事業内容\n4. 会社概要\n5. お問い合わせ")
        images = st.text_area("画像アセットの指定", "hero_office.jpg, member_01.jpg")
        extra_notes = st.text_area("特記事項", "スマホ対応（レスポンシブ）を完璧にすること")

        prompt_template = f"""あなたは優秀なWebデザイナー兼フロントエンドエンジニアです。
以下の要件に基づき、洗練された{site_type}のHTMLファイルを1つ作成してください。

【デザイン・トンマナ】
・方向性: {final_tone}
・Tailwind CSS（CDN）を使用すること
・`onerror` 属性は絶対に使用しないこと

【目的・ターゲット】
{site_purpose}

【構成案】
{structure}

【画像アセット】
{images}

【特記事項】
{extra_notes}

出力はHTML、CSS(Tailwind)、JSをすべて1ファイルにまとめ、コードブロックで出力してください。"""

with col2:
    st.subheader("✨ 2. 生成されたプロンプト")
    st.markdown("以下のテキストをコピーし、**Gemini**に貼り付けてください。")
    st.code(prompt_template, language="text")
