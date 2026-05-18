from collections import defaultdict

chat_history = defaultdict(list)


def add_message(session_id: str, role: str, content: str):
    chat_history[session_id].append(
        {
            "role": role,
            "content": content
        }
    )


def get_history(session_id: str):
    return chat_history[session_id]