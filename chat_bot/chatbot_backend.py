from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from google import genai

client = genai.Client(api_key="AIzaSyCXPP9JvKP9QpWpw5yHewYvKHSXKV9P4tQ")

class ChatState(TypedDict):
    user_input: str
    response: str

def fifa_chatbot(state: ChatState) -> ChatState:
    user_message = state["user_input"]

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are a FIFA football expert chatbot.
Answer only football (FIFA World Cup, teams, players, matches).

User question: {user_message}
"""
        )

        state["response"] = response.text

    except Exception as e:
        state["response"] = f"Error: {str(e)}"

    return state

builder = StateGraph(ChatState)

builder.add_node("chatbot", fifa_chatbot)

builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()

def get_response(user_input: str):
    result = graph.invoke({
        "user_input": user_input,
        "response": ""
    })
    return result["response"]

