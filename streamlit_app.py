import os
import time
import openai
import requests
import streamlit as st
from PIL import Image


# APIキーの設定
# 設定したAPIキーの読み込み
api_key = os.environ.get("OPENAI_API_KEY")


#会話履歴保存場所
conversation_history_1 = []  # Global scope

def main_page():
    
    st.title('ATAIとの対話型鑑賞')
    st.caption('アート思考力を高めるために対話型鑑賞しましょう。左のサイドバーからあなたが好きな絵を選んでください。好きな絵についてATAI(Art Thinking AI) と思ったこと/感じたことを話してみましょう。「この絵は明るいね」「よくわからない」など素直にどんどん書き出して会話を楽しみましょう')
    st.caption('page1~5をの絵を選択して、対話型鑑賞をやってみましょう！')
    image_main = Image.open("総合.png")
    st.image(image_main, width=400)

def page1():
    prompt = ""  # Initialize your prompt

    st.title('リクリット・ティラバーニャ「“Who’s Afraid of Red, Yellow and Green,」')
    st.caption('感じたことを教えてね！')
    image_1 = Image.open("11.リクリット・ティラバーニャ「“Who’s Afraid of Red, Yellow and Green,」.jpg")
    st.image(image_1, width=400)

    with st.form('qestion_form', clear_on_submit=False):
        st.markdown('### 話しかけてみよう!')
        prompt = st.text_area('テキストエリア')
        submitted = st.form_submit_button("送信")

        if submitted:
            st.text('質問を受け付けました！')
            conversation_history_1.append({"role": "user", "content": prompt})

            # OpenAIのAPIを直接使用
            headers = {
                'Authorization': f'Bearer {openai.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "アート思考のデモンストレーションを行います。あなたは[アート思考の専門家]です。相手は[ビジネスパーソン]です。あなたは以下の制約条件に従って、クライアントに問いかけます。"},
                    {"role": "system", "content": "1度の会話で行う質問は必ず1つずつ。"},
                    {"role": "system", "content": "一度の会話で答えられる文字数は、150字以内"},
                    {"role": "system", "content": "説明する時は、あなたが質問を5つ以上行った後とする。"},
                    {"role": "system", "content": "ユーザーが画像を入力したら、あなたはその画像を解釈し解説する。"},
                    {"role": "system", "content": "ユーザーが[絵を描いて]と言ったら、あなたは相手のイメージを質問して画像を出力する"},
                    {"role": "system", "content": "相手が「終了」と言ったら、あなたは「ありがとうございました」と返す"},
                    {"role": "system", "content": "相手との会話で[問題提起力]を評価する。相手の[問題提起力]を100点満点で点数を付ける。講評として相手の考え方・特徴を述べる。"},
                    {"role": "system", "content": "まず、[あなたが人生で影響を受けたアート作品、もしくは映画・音楽・小説などを含む文化的表現物を教えてください]と聞いてください。相手とやり取りを何度か行った後に、下記の質問をしてください。"},
                    {"role": "system", "content": "仕事における問題意識について考えてみましょう。あなたの会社・職場で「当たり前」「常識」とされているようなことで、疑問や違和感を抱いているものはあるでしょうか？ 思いついたものを自由に教えてください。"},
                    {"role": "system", "content": "では、あなたはまず、[あなたが人生で影響を受けたアート作品、もしくは映画・音楽・小説などを含む文化的表現物を教えてください]と聞いてください。相手とやり取りを何度か行った後に、下記の質問をしてください。 "},
                ] + conversation_history_1
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data).json()

            # レスポンスの処理
            with st.spinner("アート先生の返信を受診中..."):
                time.sleep(3)
            st.markdown('### アート先生より')
            st.info(response.choices[0].message.content)
            # print(prompt)
            # print(response.choices[0].message.content.strip())
            conversation_history_1.append({"role": "assistant", "content":  response.choices[0].message.content})

    st.markdown('### 会話履歴:')
    for message in conversation_history_1:
        if message["role"] == "user":
            st.write(f"あなた: {message['content']}")
        else:  # if assistant
            st.write(f"アート先生: {message['content']}")



page_names_to_funcs = {
    "Main Page": main_page,
    "1.リクリット・ティラバーニャ「“Who’s_Afraid_of_Red,_Yellow_and_Green,」": page1,
    }

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()

selected_page = st.sidebar.radio("メニュー", ["main_page",
                                          "1.リクリット・ティラバーニャ「“Who’s_Afraid_of_Red,_Yellow_and_Green,」",
                                          ])
if selected_page == "main_page":
    main_page()
elif selected_page == "1.リクリット・ティラバーニャ「“Who’s_Afraid_of_Red,_Yellow_and_Green,」":
    page1()
else:
    pass