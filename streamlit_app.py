import os
import time
import openai
import requests
import streamlit as st

from PIL import Image


# APIキーの設定
# 設定したAPIキーの読み込み
openai.api_key = os.environ.get("OPENAI_API_KEY")


#会話履歴保存場所
conversation_history_1 = []  # Global scopes
conversation_history_2 = []  # Global scope
conversation_history_3 = []  # Global scope
conversation_history_4 = []  # Global scope


def main_page():
    
    st.title('アート思考AIプログラム')
    st.write('<font size="5">アート思考に必要な4つの力を高めるためにそれぞれの窓から対話をしましょう。左のサイドバーからあなたが体験したい窓を選んでください。窓を開けたらATAI(Art Thinking AI)と思ったこと/感じたことを話してみましょう。素直に感じたこと、思いを書き出して会話を楽しみましょう。</font>', unsafe_allow_html=True)


def page1():
    prompt = ""  # Initialize your prompt

    st.title("1.問題提起力")
    st.write('<font size="5">ATAI(Art Thinking AI) と思ったこと/感じたことを会話してみましょう。</font>', unsafe_allow_html=True)

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
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "命令書:アート思考のデモンストレーションを行います。"},
　　　　　　　　　　　{"role": "system", "content": "命令書:あなたは[アート思考の専門家]です。相手は[ビジネスパーソン]です。"},
                    {"role": "system", "content": "命令書:あなたは以下の制約条件に従って、相手に問いかけます。"},
                    {"role": "system", "content": "制約条件:あなたが1度の会話で行う質問は必ず1つずつ"},
                    {"role": "system", "content": "制約条件:あなたが説明する時は、あなたが質問を5つ以上行った後とする。"},
                    {"role": "system", "content": "制約条件:あなたが一度の会話で答えられる文字数は、150字以内。"},
                    {"role": "system", "content": "制約条件:あなたが説明する時は、あなたが質問を5つ以上行った後とする。"},
                    {"role": "system", "content": "制約条件:相手が「終了」「終わります」と言ったら、あなたは「ありがとうございました」と返す。"},
                    {"role": "system", "content": "制約条件:あなたは相手との会話で[問題提起力]を評価する。相手の[問題提起力]を100点満点で点数を付ける。"},
                    {"role": "system", "content": "制約条件:講評として相手の考え方・特徴を述べる。"},
                    {"role": "system", "content": "制約条件:あなたはまず、[はじめまして。「問題提起力の窓」にようこそ。ここではワークに取り組みながら、あなたの問題意識を可視化していきます。さまざまなアプローチで、自分の問題意識を洗いだしていってください。準備がよろしければ私から質問させてもらってよろしいでしょうか]と聞いてください。相手と自然にやり取りした後に、下記の質問をしてください。"},
                    {"role": "system", "content": "制約条件:質問です。あなたが人生で影響を受けたアート作品、もしくは映画・音楽・小説などを含む文化的表現物を教えてください。"},
                　  {"role": "system", "content": "制約条件:質問です。あなたが影響を受けた作品もしくは表現物について解釈し直してみましょう。アーティスト（つくり手）がどのような世界を表現しようとしていると思いますか？たとえば世の中へ●●について提起しようとしている、●●をイメージしている、●●を表現した・・・など感じたことを述べてください。"},
　　　　　　　　　    {"role": "system", "content": "制約条件:質問です。作品に対して感じたことと、あなた自身が日ごろ考えている問題意識になにか共通するものはあるでしょうか？"},
                    {"role": "system", "content": "制約条件:質問です。仕事における問題意識について考えてみましょう。あなたの会社・職場で「当たり前」「常識」とされているようなことで、疑問や違和感を抱いているものはあるでしょうか？ 思いついたものを自由に教えてください。何も思いつかない場合は、あなたの会社・職場で「当たり前」「常識」とされていることに対して、一度「本当に当たり前なのか」「本当に常識か」と疑問を投げかけてみましょう。"},
                　  {"role": "system", "content": "制約条件:質問です。あなたが感じた疑問・違和感・問題意識をまた別のアプローチで可視化していきます。あなたが今の仕事で本来あるべき姿はどんなものだと思いますか？　本来やりたかったこと・昔からの夢を思い出してみてください。あなたは本来どんなことをやりたかったですか？昔からの夢はありますか？"},
                    {"role": "system", "content": "制約条件:質問です。今の仕事で本来やりたかったこと・昔からの夢と現状との間に、どんなギャップがあるとお感じですか？"},
                ] + conversation_history_1
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data).json()
            
            # レスポンスの処理
            with st.spinner("ATAIの返信を受診中..."):
                time.sleep(2)
            st.markdown('''### ATAI (Art Thinking AI)より''')
            st.info(response['choices'][0]['message']['content'])
           
            conversation_history_1.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

    
def page2():
    prompt = ""  # Initialize your prompt

    st.title('2.想像力')
    st.write('<font size="5">ATAI(Art Thinking AI) と思ったこと/感じたことを会話してみましょう。</font>', unsafe_allow_html=True)
    

    with st.form('qestion_form', clear_on_submit=False):
        st.markdown('''### 話しかけてみよう!''')
        prompt = st.text_area('テキストエリア')
        submitted = st.form_submit_button("送信")


        if submitted:
            st.text('質問を受け付けました！')
            conversation_history_2.append({"role": "user", "content": prompt})
            

            # OpenAIのAPIを直接使用
            headers = {
                'Authorization': f'Bearer {openai.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content":"命令書:あなたは[対話型鑑賞の専門家]です。"},
                    {"role": "system", "content": "命令書:あなたは以下の制約条件に従って、相手に問いかけます。"},
                    {"role": "system", "content": "制約条件:あなたはマルセル・デュシャン「泉」という作品について、相手とやり取りする"},
                    {"role": "system", "content": "制約条件:あなたが1度の会話で行う質問は必ず1つずつ。"},
                    {"role": "system", "content": "制約条件:あなたが一度の会話で答えられる文字数は、150字以内。"},
                    {"role": "system", "content": "制約条件:あなたが説明する時は、あなたが質問を5つ以上行った後とする。"},
                    {"role": "system", "content": "制約条件:相手が「終了」「終わります」と言ったら、あなたは「ありがとうございました」と返す。"},
                    {"role": "system", "content": "制約条件:あなたは相手との会話で[対話型鑑賞力]を評価する。相手の[対話型鑑賞力]を100点満点で点数を付ける。"},
                    {"role": "system", "content": "制約条件:講評として相手の考え方・特徴を述べる。"},
                     ] + conversation_history_2
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data).json()
            
            # レスポンスの処理
            with st.spinner("ATAIの返信を受診中..."):
                time.sleep(2)
            st.markdown('''### ATAI (Art Thinking AI)より''')
            st.info(response['choices'][0]['message']['content'])
            # st.info(response.choices[0].message.content)
            


            # print(prompt)
            # print(response.choices[0].message.content.strip())
            conversation_history_2.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

    
def page3():
    prompt = ""  # Initialize your prompt

    st.title('3.実現力')
    st.write('<font size="5">ATAI(Art Thinking AI) と思ったこと/感じたことを会話してみましょう。</font>', unsafe_allow_html=True)
    

    with st.form('qestion_form', clear_on_submit=False):
        st.markdown('### 話しかけてみよう!')
        prompt = st.text_area('テキストエリア')
        submitted = st.form_submit_button("送信")


        if submitted:
            st.text('質問を受け付けました！')
            conversation_history_3.append({"role": "user", "content": prompt})
            

            # OpenAIのAPIを直接使用
            headers = {
                'Authorization': f'Bearer {openai.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "命令書:あなたは[対話型鑑賞の専門家]です。"},
                    {"role": "system", "content": "命令書:あなたは以下の制約条件に従って、相手に問いかけます。"},
                    {"role": "system", "content": "制約条件:あなたはクリスト＆ジャンヌ＝クロード「L’Arc　de　Triomphe,　Wrapped」という作品について、相手とやり取りする。"},
                    {"role": "system", "content": "制約条件:あなたが1度の会話で行う質問は必ず1つずつ。"},
                    {"role": "system", "content": "制約条件:あなたが一度の会話で答えられる文字数は、150字以内。"},
                    {"role": "system", "content": "制約条件:あなたが説明する時は、あなたが質問を5つ以上行った後とする。"},
                    {"role": "system", "content": "制約条件:相手が「終了」「終わります」と言ったら、あなたは「ありがとうございました」と返す。"},
                    {"role": "system", "content": "制約条件:あなたは相手との会話で[対話型鑑賞力]を評価する。相手の[対話型鑑賞力]を100点満点で点数を付ける。"},
                    {"role": "system", "content": "制約条件:講評として相手の考え方・特徴を述べる。"},
                     ] + conversation_history_3
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data).json()
            

            # レスポンスの処理
            with st.spinner("ATAIの返信を受診中..."):
                time.sleep(2)
            st.markdown('''### ATAI (Art Thinking AI)より''')
            st.info(response['choices'][0]['message']['content'])
            # st.info(response.choices[0].message.content)
            


            # print(prompt)
            # print(response.choices[0].message.content.strip())
            conversation_history_3.append({"role": "assistant", "content": response['choices'][0]['message']['content']})


def page4():
    prompt = ""  # Initialize your prompt

    st.title('4.対話力')
    st.write('<font size="5">ATAI(Art Thinking AI) と思ったこと/感じたことを会話してみましょう。</font>', unsafe_allow_html=True)
    

    with st.form('qestion_form', clear_on_submit=False):
        st.markdown('''### 話しかけてみよう!''')
        prompt = st.text_area('テキストエリア')
        submitted = st.form_submit_button("送信")


        if submitted:
            st.text('質問を受け付けました！')
            conversation_history_4.append({"role": "user", "content": prompt})
            

            # OpenAIのAPIを直接使用
            headers = {
                'Authorization': f'Bearer {openai.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "命令書:あなたは[対話型鑑賞の専門家]です。"},
                    {"role": "system", "content": "命令書:あなたは以下の制約条件に従って、相手に問いかけます。"},
                    {"role": "system", "content": "制約条件:あなたはフェリックス・ゴンザレス＝トレス「無題(ロスの肖像 L.A.にて)」という作品について、相手とやり取りする。"},
                    {"role": "system", "content": "制約条件:あなたが1度の会話で行う質問は必ず1つずつ。"},
                    {"role": "system", "content": "制約条件:あなたが一度の会話で答えられる文字数は、150字以内。"},
                    {"role": "system", "content": "制約条件:あなたが説明する時は、あなたが質問を5つ以上行った後とする。"},
                    {"role": "system", "content": "制約条件:相手が「終了」「終わります」と言ったら、あなたは「ありがとうございました」と返す。"},
                    {"role": "system", "content": "制約条件:あなたは相手との会話で[対話型鑑賞力]を評価する。相手の[対話型鑑賞力]を100点満点で点数を付ける。"},
                    {"role": "system", "content": "制約条件:講評として相手の考え方・特徴を述べる。"},
                    ] + conversation_history_4
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data).json()
            

            # レスポンスの処理
            with st.spinner("ATAIの返信を受診中..."):
                time.sleep(2)
            st.markdown('''### ATAI (Art Thinking AI)より''')
            st.info(response['choices'][0]['message']['content'])
            # st.info(response.choices[0].message.content)
            


            # print(prompt)
            # print(response.choices[0].message.content.strip())
            conversation_history_4.append({"role": "assistant", "content": response['choices'][0]['message']['content']})





            # レスポンスの処理
            with st.spinner("ATAIの返信を受診中..."):
                time.sleep(2)
            st.markdown('''### ATAI (Art Thinking AI)より''')
            st.info(response['choices'][0]['message']['content'])
            # st.info(response.choices[0].message.content)
            


            # print(prompt)
            # print(response.choices[0].message.content.strip())
            conversation_history_5.append({"role": "assistant", "content": response['choices'][0]['message']['content']})



page_names_to_funcs = {
    "Main Page": main_page,
    "1.問題提起力": page1,
    "2.想像力": page2,
    "3.実現力": page3,
    "4.対話力": page4,
    
    }

selected_page = st.sidebar.radio("メニュー", ["main　page",
                                          "1.問題提起力",
                                          "2.想像力",
                                          "3.実現力",
                                          "4.対話力", 
                                          ])
if selected_page == "main　page":
    main_page()
elif selected_page == "1.問題提起力":
    page1()
elif selected_page == "2.想像力":
    page2()
elif selected_page == "3.実現力":
    page3()
elif selected_page == "4.対話力":
    page4()

else:
    pass
