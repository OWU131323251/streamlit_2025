import streamlit as st
import pandas as pd
import os
from PIL import Image
import base64

# CSSの埋め込み（ミクカラーとフォント）
st.markdown("""
    <style>
    body {
        background-color: #000000;
    }

    .main {
        background-color: #1e1e1e;
        color: #39C5BB;
        font-family: 'M PLUS 1p', sans-serif;
    }

    h1, h2, h3 {
        color: #00C8C8 !important;
    }

                label {
        color: #00F0F0 !important;  /* 明るめのミクブルー */
        font-weight: bold;
        font-size: 18px;
    }
    a {
        color: #FF66CC !important;
        text-decoration: none;
        font-weight: bold;
    }

    a:hover {
        color: #FFFFFF !important;
    }
    </style>

    <link href="https://fonts.googleapis.com/css2?family=M+PLUS+1p&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# DataFrame作成など前処理（song_data）省略
def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# 曲データの作成
song_data = {
    "感情": [
        "楽しい",
        "楽しい",
        "悲しい",
        "切ない",
        "悲しい", 
        "切ない",
        "好き",
        "イライラ",
        "好き",
        "イライラ"
        ],

    "曲名": [
        "39みゅーじっく!",
        "ビバハピ", 
        "アイロニ",
        "ロミオとシンデレラ", 
        "クライヤ", 
         "魔法の鏡",
        "メランコリック",
        "おこちゃま戦争",
        "スキスキ絶頂症",
        "snooze"
        ],

    "アーティスト": [
        "みきとP feat. 初音ミク", 
        "Mitchie M feat. 初音ミク", 
        "すこっぷ feat. 初音ミク",
        "doriko feat. 初音ミク",
        "すこっぷ feat. 初音ミク",
        "ひとしずく×やま△ feat. 鏡音リン・レン",
        "Junky feat. 鏡音リン", 
        "ギガP feat. 鏡音リンレン", 
        "koyori feat. GUMI",
        "wotaku feat. 初音ミク"
        ],

    "YouTubeリンク": [
        "https://youtu.be/OuLZlZ18APQ?feature=shared", 
        "https://youtu.be/WiUjG9fF3zw?feature=shared",
        "https://youtu.be/clPjNKWe6N0?feature=shared",
        "https://youtu.be/9HrOqmiEsN8?feature=shared",
        "https://youtu.be/cPVD9tdxS0I?feature=shared",
        "https://youtu.be/RquwdfMQ_EE?feature=shared",
        "https://youtu.be/86_kvUqhY-A?feature=shared",
        "https://youtu.be/qYAmduGAwBQ?feature=shared",
        "https://youtu.be/49q36mUMh9k?feature=shared",
        "https://youtu.be/fqBpGiVn2k0?feature=shared"
    ],

    "歌詞": [
        "大サービス！ Oh Yeah！ 大熱唱！ Hey Making Groovy Night\n未体験Night！ Oh Yeah！",
        "ミニスカートで襲撃だ！（キュン）　ギャップ萌えして衝撃だ！（キュン）恋の妄想　回路暴走　デマ デマ ホラ",
        "少し歩き疲れたんだ　少し歩き疲れたんだ　月並みな表現だけど人生とかいう長い道を　少し休みたいんだ　少し休みたいんだけど　時間は刻一刻こくいっこく残酷と　私を引っぱっていくんだ",
        "私の恋を悲劇のジュリエットにしないで\nここから連れ出して…\nそんな気分よ",
        "不安になるとね　涙は自然と溢れて\n泣き終われば疲れて眠りについて\nそうだよ　そんな夜ばかり繰り返して変わらずに\n今日もまた息苦しい朝が来るよ",
        "このままでずっといられたらよかった　魔法なんてなくてもあなたの側に居たい　だから、もう一度此処の会いに来て",
        "全然つかめないきみのこと　全然しらないうちに　ココロ奪われるなんてこと　あるはずないでしょ",
        "あﾞーむかつくぜ！まーぢむかつくぜ！僕に向かって減らず口なんざとっておきを　きみに見舞え　報復！制裁！挑発しちゃって",
        "もう考えたって抗ったって　好き好き絶頂症　べたべたしちゃうから もっと欲張って",
        "ダークマターのせいで 生まれた時代が悪かったせいで 全部あなたのせいで 今日傘を持ってくるのを忘れた"
    ]
    
}

# DataFrameの作成
df = pd.DataFrame(song_data)

# タイトルと説明
st.title("🎶 ボカロ曲感情推薦アプリ")
st.write("あなたの気分に合わせて、ボカロ曲をおすすめします！")

# 感情選択のドロップダウン
emotions = ["楽しい", "悲しい", "切ない","好き","イライラ"]
selected_emotion = st.selectbox("気分を選択してください", emotions)

# 選択された感情に基づいて曲をフィルタリング
recommended_songs = df[df["感情"] == selected_emotion]

for _, row in recommended_songs.iterrows():
    # 動画IDの抽出（youtu.be/xxxxx?〜 の形式に対応）
    video_id = row["YouTubeリンク"].split("youtu.be/")[-1].split("?")[0]
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

# 曲が見つかった場合
if not recommended_songs.empty:
    st.write(f"おすすめの曲（{selected_emotion}気分）:")

    for _, row in recommended_songs.iterrows():
        st.subheader(row["曲名"] + " - " + row["アーティスト"])
        
        image_path = os.path.join("thumbnails", f"{row['曲名']}.jpg")
        st.write(f"🎧 [視聴する]({row['YouTubeリンク']})")

        if os.path.exists(image_path):
            # base64で画像をエンコード
            img_base64 = get_image_base64(image_path)
            # HTMLで画像をリンクで囲む
            html = f"""
                <a href="{row['YouTubeリンク']}" target="_blank">
                    <img src="data:image/jpeg;base64,{img_base64}" width="320" style="border-radius: 10px;"/>
                </a>
            """
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write("🖼 サムネイル画像が見つかりませんでした。")
        st.write(f"🎵 歌詞の一部:\n{row['歌詞']}")
else:
    st.write("選択された感情に合う曲は見つかりませんでした。")
