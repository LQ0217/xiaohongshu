from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu

#import os

def generate_xiaohongshu(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    # 初始化语言模型
    model = ChatOpenAI(
        model = "gpt-3.5-turbo",
        api_key = openai_api_key,
        openai_api_base = "https://api.aigc369.com/v1"
    )
    # 初始化输出解析器
    output_parser = PydanticOutputParser(pydantic_object = Xiaohongshu)

    # 创建链：提示 -> 模型 -> 解析器
    chain = prompt | model | output_parser

    # 准备输入
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })

    return result

#print(generate_xiaohongshu("大模型", openai_api_key = os.getenv("OPENAI_API_KEY")))
