from pydantic import BaseModel, HttpUrl
from typing import Optional



class PostSchema(BaseModel):
    """Standard Post template used throughout the application"""
    source: str
    guid: str
    title: str
    image: str = ""
    author: Optional[str] = ""
    content: Optional[str] = ""
    description: Optional[str] = ""
    link: Optional[HttpUrl] = None
    url: Optional[HttpUrl] = None  
    cr_color: Optional[int] = None 
    mal_color: Optional[int] = None
