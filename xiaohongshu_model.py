from pydantic import BaseModel, Field
from typing import List


class Xiaohongshu(BaseModel):
    titles: List[str] = Field(min_items= 5, max_items = 5,description="小红书的5个标题")
    content: str = Field(description="小红书的正文内容")
