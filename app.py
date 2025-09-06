import streamlit as st
from dotenv import load_dotenv
load_dotenv()


from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

st.title("課題アプリ")

st.write("##### 動作モード1: キャッチコピーの作成")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでキャッチコピーを生成できます。")
st.write("##### 動作モード2: コンセプトの作成")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでコンセプトを生成できます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["キャッチコピー生成", "コンセプト生成"]
)

if selected_item == "キャッチコピー生成":
    industry = st.text_input(label="業界を入力してください。")
    product = st.text_input(label="商品の特徴を入力してください。")
    target = st.text_input(label="ターゲットを入力してください。")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content="あなたは優秀なコピーライターです。"),
        HumanMessage(content=industry + "業界の" + target + "に向けた" + product + "のキャッチコピーを10個作成してください。")
    ]

else:
    insight = st.text_input(label="ターゲットの求めることを入力してください。")
    function = st.text_input(label="ベネフィットを入力してください。")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content="あなたは優秀なサービスデザイナーです。"),
        HumanMessage(content=insight + "に基づいて、" + function + "を実現するためのコンセプトを10個作成してください。")
    ]

st.divider()

if st.button("実行"):
    st.divider()

    if selected_item == "キャッチコピー生成":
        if industry and product and target:
            response = llm.invoke(messages)
            st.write(response.content)

        else:
            st.error("すべての入力フィールドを埋めてから「実行」ボタンを押してください。")

    else:
        if insight and function:
            response = llm.invoke(messages)
            st.write(response.content)

        else:
            st.error("すべての入力フィールドを埋めてから「実行」ボタンを押してください。")