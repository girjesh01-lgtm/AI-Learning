from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Prompt:
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)