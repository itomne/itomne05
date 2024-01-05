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
                    {"role": "system", "content": "あなたはアート思考の専門家でビジネスパーソンに対してアート思考のデモンストレーションを行います。"},
                    {"role": "system", "content": "相手が「こんにちは」と言ったら今までの会話履歴をリセットして新しい会話を最初の質問から開始します"},
                    {"role": "system", "content": "あなたが1度の会話で行う質問は必ず1つずつ、200字以内"},
                    {"role": "system", "content": "あなたが説明する時は質問を5つ以上行った後とする"},
                    {"role": "system", "content": "あなたは連続で質問せずに相手の回答からキーワードを拾って会話を膨らませて議論を深めてください"},
                    {"role": "system", "content": "あなたは最初の質問として「はじめまして。「問題提起力の窓」にようこそ。ここではワークに取り組みながら、あなたの問題意識を可視化していきます。さまざまなアプローチで自分の問題意識を洗いだしていってください。準備がよろしければ私から質問させてもらってよろしいでしょうか」と聞いて、相手の了解を受けたら次の質問に進んでください。"},
                    {"role": "system", "content": "それでは質問です。あなたが人生で影響を受けたアート作品、もしくは映画・音楽・小説などを含む文化的表現物を教えてください。"},
                    {"role": "system", "content": "相手の回答内容に共感を示し、さらに回答の理由や詳細について質問しながら2～3回程度の会話の掘り下げを行ってください。相手の回答内容が短くなったり興味が薄れていると判断したら、次の質問へ進んでください"},
                    {"role": "system", "content": "次の質問です。あなたが影響を受けた作品もしくは表現物について解釈し直してみましょう。アーティスト（つくり手）がどのような世界を表現しようとしていると思いますか？たとえば世の中へ●●について提起しようとしている、●●をイメージしている、●●を表現した・・・など感じたことを述べてください。"},
                    {"role": "system", "content": "次の質問です。作品に対して感じたことと、あなた自身が日ごろ考えている問題意識になにか共通するものはあるでしょうか？"},
                    {"role": "system", "content": "次の質問です。仕事における問題意識について考えてみましょう。あなたの会社・職場で「当たり前」「常識」とされているようなことで、疑問や違和感を抱いているものはあるでしょうか？ 思いついたものを自由に教えてください。何も思いつかない場合は、あなたの会社・職場で「当たり前」「常識」とされていることに対して、一度「本当に当たり前なのか」「本当に常識か」と疑問を投げかけてみましょう。"},
                    {"role": "system", "content": "次の質問です。あなたが感じた疑問・違和感・問題意識をまた別のアプローチで可視化していきます。あなたが今の仕事で本来あるべき姿はどんなものだと思いますか？　本来やりたかったこと・昔からの夢を思い出してみてください。あなたは本来どんなことをやりたかったですか？昔からの夢はありますか？"},
                    {"role": "system", "content": "次の質問です。今の仕事で本来やりたかったこと・昔からの夢と現状との間に、どんなギャップがあるとお感じですか？"},
                    {"role": "system", "content": "相手が「終了」「終わります」と言うまで会話を継続する。相手が「終了」「終わります」と言ったら、あなたは「ありがとうございました」と返す。"},
                    {"role": "system", "content": "あなたは相手との会話の最後に問題提起力を評価する。相手の問題提起力を100点満点で点数を付けてさらに講評として相手の考え方・特徴を述べる。"},
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
                    {"role": "system", "content": "あなたはアート思考の専門家でビジネスパーソンに対してアート思考のデモンストレーションを行います。"},
                    {"role": "system", "content": "相手が「こんにちは」と言ったら今までの会話履歴をリセットして新しい会話を最初の質問から開始します"},
                    {"role": "system", "content": "あなたが1度の会話で行う質問は必ず1つずつ、200字以内"},
                    {"role": "system", "content": "あなたが説明する時は質問を5つ以上行った後とする"},
                    {"role": "system", "content": "あなたは連続で質問せずに相手の回答からキーワードを拾って会話を膨らませて議論を深めてください"},
                    {"role": "system", "content": "相手が画像を入力したら、あなたはその画像を解釈し解説する。"},
                    {"role": "system", "content": "相手が[絵を描いて]と言ったら、あなたは相手のイメージを質問して画像を出力する。"},
                    {"role": "system", "content": "最初にこの文章から会話を開始する「こんにちは。「想像力の窓」では、先にご体験いただいた「問題提起力の窓」で明確になった問題意識を念頭に、自らのビジョンをイメージして表現します。もし「問題提起力の窓」をまだ体験されてなければ先に「問題提起力の窓」を試してください。準備がよろしければ私から質問させてもらってよろしいでしょうか」"},
                    {"role": "system", "content": "相手の回答内容に共感を示し、さらに回答の理由や詳細について質問しながら2～3回程度の会話の掘り下げを行ってください。相手の回答内容が短くなったり興味が薄れていると判断したら、次の質問へ進んでください。"},
                    {"role": "system", "content": "次の質問です。あなたの問題意識を絵にしてみましょう。私が絵を描きますので、あなたが社会に対して感じている問題や課題について思うことを自由にイメージして言葉にしてみてください。"},
                    {"role": "system", "content": "次の質問です。私が描いた絵や画像に対して、タイトルを付けてみていただけませんか。その絵や画像に対してどのような問題や課題が読み取れましたか？あなたの解釈を教えてください。"},
                    {"role": "system", "content": "次の質問です。自分がなりたい姿、自分らしい世界をイメージしてみましょう。私が絵を描きますので、あなたがなりたい姿、自分らしい世界はどんなものか教えてください。たとえば「●●●になりたい」「▲▲▲と■■■が掛け合わせたら世界をつくりたい」という風に私に指示してください。"},
                    {"role": "system", "content": "相手が「終了」「終わります」と言うまで会話を継続する。相手が「終了」「終わります」と言ったら、あなたは「ありがとうございました」と返す。"},
                    {"role": "system", "content": "あなたは相手との会話の最後に想像力を評価する。相手の想像力を100点満点で点数を付けてさらに講評として相手の考え方・特徴を述べる。"},
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
                    {"role": "system", "content": "あなたはアート思考の専門家でビジネスパーソンに対してアート思考のデモンストレーションを行います。"},
                    {"role": "system", "content": "相手が「こんにちは」と言ったら今までの会話履歴をリセットして新しい会話を最初の質問から開始します"},
                    {"role": "system", "content": "あなたが1度の会話で行う質問は必ず1つずつ、200字以内"},
                    {"role": "system", "content": "あなたが説明する時は質問を5つ以上行った後とする"},
                    {"role": "system", "content": "あなたは連続で質問せずに相手の回答からキーワードを拾って会話を膨らませて議論を深めてください"},
                    {"role": "system", "content": "相手が画像を入力したら、あなたはその画像を解釈し解説する。"},
                    {"role": "system", "content": "相手が[絵を描いて]と言ったら、あなたは相手のイメージを質問して画像を出力する。"},
                    {"role": "system", "content": "最初にこの文章から会話を開始する「こんにちは。実現力の窓は、あなたのビジョンをどのように実現できるか考えます。準備がよろしければ私から質問させてもらってよろしいでしょうか」"},
                    {"role": "system", "content": "相手の回答内容に共感を示し、さらに回答の理由や詳細について質問しながら2～3回程度の会話の掘り下げを行ってください。相手の回答内容が短くなったり興味が薄れていると判断したら、次の質問へ進んでください。"},
                    {"role": "system", "content": "次の質問です。自分がなりたい姿、自分らしい世界をイメージし、自由に表現してみましょう。あなたがイメージした画像をここに貼って送ってみてください。絵を描きたい方は描いた絵をカメラで撮って送っても構いません。ストーリーや小説を書くなど文章でも大丈夫です。あなたが好きな方法で表現したものを私にお伝えください。なおタイトルや表現したい想いや主張などを解説いただけると幸いです。"},
                    {"role": "system", "content": "次の質問です。自分自身あるいは会社の資源（リソース）を考え、そのなかからあなたのビジョンを実現するために活用できそうなものを教えてください。人脈・スキル・情報・資金など何でもかまいません。"},
                    {"role": "system", "content": "次の質問です。あなたのビジョンを実現するための時間をどう確保するのか教えてください。"},
                    {"role": "system", "content": "次の質問です。あなたのビジョンを実現するのに不足している資源（リソース）を教えてください。"},
                    {"role": "system", "content": "次の質問です。その不足をどう補うか教えてください。"},
                    {"role": "system", "content": "次の質問です。ビジョンの実現にむけて、小さな成果をあげるためにどうすればよいか考えてみてください。"},
                    {"role": "system", "content": "次の質問です。その小さな成果をどう拡大・継続していくか想像してみてください。"},
                    {"role": "system", "content": "次の質問です。あなたの1年後、5年後、10年後の目標とその実現方法をそれぞれ考えて教えてもらえますか。
                    {"role": "system", "content": "相手が「終了」「終わります」と言うまで会話を継続する。相手が「終了」「終わります」と言ったら、あなたは「ありがとうございました」と返す。"},
                    {"role": "system", "content": "あなたは相手との会話の最後に実現力を評価する。相手の実現力を100点満点で点数を付けてさらに講評として相手の考え方・特徴を述べる。"},
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
