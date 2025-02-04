from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper


def generate_script(subject,video_length,
                    creativity,api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为{subject}这个主题的视频想一个吸引人的标题")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human","""你是一个短视频的博主。根据以下标题和相关信息，为短视频写一个视频脚本。
            视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度遵循视频时长的要求。
            要求开头抓住眼球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头，中间，结尾】分隔。
            整体内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略：
            '''{weikipedia_search}'''""")
        ]
    )
    model = ChatOpenAI(
        openai_api_key = api_key,
        temperature = creativity
    )

    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject":subject}).content

    wikipedia = WikipediaAPIWrapper(lang="zh")
    search_result = wikipedia.run(subject)

    script = script_chain.invoke({"title":title,"duration":video_length,
                                  "weikipedia_search":search_result}).content

    return search_result,title,script

if __name__ == '__main__':
    print(generate_script("新冠病毒",1,0.7,"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"))


