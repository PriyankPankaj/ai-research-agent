from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ResearchState:
    query: str
    subtasks: List[str] = field(default_factory=list)
    sources: List[dict] = field(default_factory=list)
    extracted_notes: List[str] = field(default_factory=list)
    draft_report: Optional[str] = None
    critique: Optional[str] = None
    is_complete: bool = False
    memory_context: List[dict] = field(default_factory=list)