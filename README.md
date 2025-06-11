import streamlit as st
import pandas as pd
import random

# タイトルと説明
st.title("🎶 ボカロ曲感情推薦アプリ")
st.write("あなたの気分に合わせて、ボカロ曲をおすすめします！")

# 感情選択のドロップダウン
emotions = ["楽しい", "悲しい", "怒っている", "驚いている"]
selected_emotion = st.selectbox("気分を選択してください", emotions)

# ボカロ曲のデータベース
song_data = {
    "曲名": ["千本桜", "メルト", "ロミオとシンデレラ", "裏表ラバーズ", "からくりピエロ", "ワールドイズマイン", "ゴーストルール", "シャルル"],
    "アーティスト": [
        "黒うさP feat. 初音ミク", "ryo (supercell) feat. 初音ミク", "wowaka feat. 初音ミク", "wowaka feat. 初音ミク",
        "40mP feat. 初音ミク", "ryo (supercell) feat. 初音ミク", "DECO*27 feat. 初音ミク", "バルーン feat. flower"
    ],
    "感情": ["楽しい", "悲しい", "楽しい", "怒っている", "悲しい", "楽しい", "怒っている", "悲しい"],
    "YouTubeリンク": [
        "https://www.youtube.com/watch?v=1SJ6gJ3FZ2s", "https://www.youtube.com/watch?v=6lq1BzHk7wA", "https://www.youtube.com/watch?v=Qw0d3qZ1g7I",
        "https://www.youtube.com/watch?v=5Pz5qVY6vM0", "https://www.youtube.com/watch?v=3i8E1Opb5iI", "https://www.youtube.com/watch?v=4zVVK9i6qOg",
        "https://www.youtube.com/watch?v=8VgLKXD-BoY", "https://www.youtube.com/watch?v=VUIEJu4kFLk"
    ]
}

# データフレームの作成
df = pd.DataFrame(song_data)

# 選択された感情に基づいて曲をフィルタリング
recommended_songs = df[df["感情"] == selected_emotion]

# 推薦された曲の表示
if not recommended_songs.empty:
    st.write(f"**{selected_emotion}**な気分にぴったりのボカロ曲はこちら！")
    # ランダムで複数曲を選択
    num_songs = min(3, len(recommended_songs))  # 最大3曲を表示
    random_songs = recommended_songs.sample(n=num_songs)
    for _, song in random_songs.iterrows():
        st.write(f"**{song['曲名']}** - {song['アーティスト']}")
        st.markdown(f"[YouTubeで再生]({song['YouTubeリンク']})")
else:
    st.write(f"**{selected_emotion}**な気分に合うボカロ曲は見つかりませんでした。")
    # ランダムで曲を提案
    random_song = df.sample(1).iloc[0]
    st.write("代わりにこちらの曲をおすすめします！")
    st.write(f"**{random_song['曲名']}** - {random_song['アーティスト']}")
    st.markdown(f"[YouTubeで再生]({random_song['YouTubeリンク']})")
