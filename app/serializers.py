import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self, name: str, title_: str, content_: str) -> str:
        pass


class XmlSerializer(Serializer):
    def serialize(self, name: str, title_: str, content_: str) -> str:
        root = ET.Element(name)
        title = ET.SubElement(root, "title")
        title.text = title_
        content = ET.SubElement(root, "content")
        content.text = content_
        return ET.tostring(root, encoding="unicode")


class JsonSerializer(Serializer):
    def serialize(self, name: str, title_: str, content_: str) -> str:
        return json.dumps({"title": title_, "content": content_})
