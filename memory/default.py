"""Default memory module."""


from typing import Optional

from simple_assistant.types import MessageSequence

def load_memory(
    knowledge: Optional[str],
    conversation_history: MessageSequence,
    user_input: str,
    max_tokens: int,
) -> MessageSequence:
    """Load the memory that the assistant has."""
    return conversation_history
